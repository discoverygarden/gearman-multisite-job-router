# gearman-multisite-job-router

## Introduction

Job routing utility that can be used by a gearman server to interpret job payloads and route them to Drush using the correct URI.

## Requirements

This program requires Python 3.

## Installation

Can be installed either using [pip](https://pypi.python.org/pypi/pip), by running:

```bash
pip install git+https://github.com/discoverygarden/gearman-multisite-job-router
```

Or using [setuptools](https://pypi.python.org/pypi/setuptools), by running:

```bash
git clone https://github.com/discoverygarden/gearman-multisite-job-router
cd gearman-multisite-job-router
python setup.py install
```

## Usage

Installation provides gearman-multisite-job-router.py as an executable.

The router can be provided to [gearman-init](https://github.com/discoverygarden/gearman-init)'s worker service by defining the `ROUTER` variable in `/etc/defaults/gearman-worker`:

```bash
ROUTER="gearman-multisite-job-router.py"
```

Output of gearman-multisite-job-router.py --help:

```
usage: gearman-multisite-job-router.py [-h] [--drush DRUSH] [--root ROOT]

Routes a multisite payload from STDIN to the drush islandora_job router.

optional arguments:
  -h, --help     show this help message and exit
  --drush DRUSH  Path to the drush executable (default: /usr/bin/drush)
  --root ROOT    Path to the Drupal root (default: /var/www/drupal7)

The exit code will be passed through from drush if the router command
successfully ran. In the case we failed to get that far, exits with -1
```

## Maintainers/Sponsors:

Current maintainers:

* [discoverygarden](https://github.com/discoverygarden)

## License:

[GPLv3](http://www.gnu.org/licenses/gpl-3.0.txt)
