"""Setup script for the obsdb package."""
import glob

from setuptools import setup

PACKAGES = ['gotoalert']

REQUIRES = ['numpy',
            'astropy',
            'astroplan',
            'voevent-parse',
            'slacker',
            'slackclient',
            'setuptools',
            ]

# Get the version string
__version__ = None
with open('gotoalert/version.py') as f:
    version = exec(f.read())

setup(name='gotoalert',
      version=__version__,
      description='GOTO Alert manager',
      url='http://github.com/GOTO/goto-alert',
      author='Alex Obradovic',
      author_email='aobr10@student.monash.edu',
      install_requires=REQUIRES,
      packages=PACKAGES,
      package_data={'': ['data/*', 'data/tests/*']},
      include_package_data=True,
      scripts=glob.glob('scripts/*'),
      zip_safe=False,
      )
