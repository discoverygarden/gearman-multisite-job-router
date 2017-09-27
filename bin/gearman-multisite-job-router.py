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
parser.add_argument('--drush')
parser.add_argument('--root')

if __name__ == '__main__':
    try:
        with open(sys.stdin, 'r') as stdin:
            payload = json.loads(stdin)
    except:
        logger.error('Failed to load the payload from STDIN as JSON')
        exit(-1)

    for param in ['func', 'uid', 'args', 'site']:
        if param not in payload:
            logger.error('Missing %s from payload' % (param))
            exit(-1)

    args = parser.parse_args()

    drush_args = [
        args['drush'],
        '--root=%s' % (args['root']),
        '-u %s' % (payload['uid']),
        '--uri=%s' % (payload['site']),
        'islandora-job-router',
    ]

    drush = Popen(drush_args, stdin=sys.stdin)
    drush.communicate()
    exit(drush.exitcode)
