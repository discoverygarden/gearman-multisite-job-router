from setuptools import setup

setup(
    name='gearman-multisite-job-router',
    version='1.0',
    description='Routes gearman job payloads to Drush.',
    long_description='Routes gearman job payloads from STDIN to Drush using the correct URI for the multisite stated by the payload.',
    author='Daniel Aitken',
    maintainer='discoverygarden',
    maintainer_email='dev@discoverygarden.ca',
    url='http://github.com/discoverygarden/gearman-multisite-job-router',
    scripts=['bin/gearman-multisite-job-router.py']
)
