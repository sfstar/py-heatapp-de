from distutils.core import setup
setup(
  name = 'py-heatapp-de',         # How you named your package folder (MyLib)
  packages = ['py-heatapp-de'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',
  description = 'HeatApp local api integration library',
  author = 'Sven ten Raa',
  author_email = 'sventenraa@gmail.com',
  url = 'https://github.com/sfstar/py-heatapp-de',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
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
