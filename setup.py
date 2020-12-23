from distutils.core import setup
setup(
  name = 'py-heatapp-de',
  packages = ['py-heatapp-de'],
  version = '0.0.1',
  license='MIT',
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
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9',
  ],
)
