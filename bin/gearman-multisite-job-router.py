#!/usr/bin/env python

import json
import logging
import sys
from argparse import ArgumentParser
from subprocess import Popen

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%s', level=logging.INFO)
logger = logging.getLogger('islandora-job-multisite-router')

parser = ArgumentParser(
    description='Routes a multisite payload from STDIN to the drush islandora_job router.',
    epilog='The exit code will be passed through from drush if the router command successfully ran. In the case we failed to get that far, exits with -1'
)
parser.add_argument('--drush', default='/usr/bin/drush', help='Path to the drush executable (default: %(default)s)')
parser.add_argument('--root', default='/var/www/drupal7', help='Path to the Drupal root (default: %(default)s)')

if __name__ == '__main__':
    args = parser.parse_args()

    try:
        payload = json.loads(sys.stdin.read())
        print(payload)
    except Exception as e:
        logger.error('Failed to load the payload from STDIN as JSON: {0}'.format(e.message))
        exit(-1)

    for param in ['func', 'uid', 'args', 'site']:
        if param not in payload:
            logger.error('Missing {0} from payload'.format(param))
            exit(-1)

    drush_args = [
        args.drush,
        '--root={0}'.format(args.root),
        '--user={0}'.format(payload['uid']),
        '--uri={0}'.format(payload['site']),
        'islandora-job-router',
    ]

    drush = Popen(drush_args, stdin=sys.stdin)
    drush.communicate()
    exit(drush.returncode)
