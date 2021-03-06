from setuptools import setup, find_packages
import glob, os
from stat import *

def executable(path):
    st = os.stat(path)[ST_MODE]
    return (st & S_IEXEC) and not S_ISDIR(st)

dependencies = """
Babel
PIL
argparse
BeautifulSoup
DBUtils
genshi
gunicorn
iptools
lxml
psycopg2
pymarc
pytest
python-memcached
pyyaml
simplejson
supervisor
web.py==0.33
pystatsd
eventer
Pygments
OL-GeoIP
mockcache
"""

setup(
    name='openlibrary',
    version='2.0',
    description='Open Library',
    packages=find_packages(exclude=["ez_setup"]),
    scripts=filter(executable, glob.glob('scripts/*')),
    install_requires=dependencies.split()
)

