from setuptools import setup, find_packages
import sys
import os
import re
import shutil


def get_version(package):
    """
    Return package version as listed in `__version__` in `__init__.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def read_all(f):
    with open(f, 'r') as f:
        return f.read()


requirements = map(str.strip, read_all('requirements.txt').splitlines())

version = get_version('pyswyft')

if sys.argv[-1] == 'publish':
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree('pyswyft.egg-info')
    sys.exit()

setup(name='pyswyft',
      version=version, 
      description="Python wrapper for Swyftx API",
      long_description=read_all("README.md"),
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers)
      keywords='Swyftx Crypto API wrapper REST',
      author='Lachlan Teale',
      author_email='lachlan.teale@gmail.com',
      url='http://pyswyft.lachlanteale.com/',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      test_suite='tests',
      include_package_data=True,
      zip_safe=False, 
      install_requires=requirements,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )