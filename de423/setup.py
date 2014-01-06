from distutils.core import setup

name = 'de423'
module = __import__(name)
description, long_description = module.__doc__.split('\n', 1)

setup(name = name,
      version = '2010.1',
      description = description,
      long_description = long_description,
      license = 'MIT',
      author = 'Brandon Rhodes',
      author_email = 'brandon@rhodesmill.org',
      classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Topic :: Scientific/Engineering :: Astronomy',
        ],
      packages = [name],
      package_data = {name: ['*.npy',]},
      )
