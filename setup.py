import setuptools

from os.path import splitext, basename
from glob import glob
from subprocess import check_output


setuptools.setup(
  name = 'py-heatapp-de',
  packages=setuptools.find_packages("src"),
  package_dir={"": "src"},
  version = '0.0.1.3',
  license='GLPv3',
  description = 'HeatApp local api integration library',
  author = 'Sven ten Raa',
  author_email = 'sventenraa@gmail.com',
  url = 'https://github.com/sfstar/py-heatapp-de',
  download_url = 'https://github.com/sfstar/py-heatapp-de/archive/v0.0.1-alpha.tar.gz',
  keywords = ['heatapp', 'api', 'integration'],
  install_requires=[            
          'pycryptodome',
          'urllib3',
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    'Programming Language :: Python :: 3.9',
  ],
)
