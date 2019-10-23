 #!/usr/bin/env python

from setuptools import setup, find_packages

if sys.version_info[0] == 2:
    if not sys.version_info >= (2, 7):
        raise ValueError('This package requires Python 2.7 or above')
elif sys.version_info[0] == 3:
    if not sys.version_info >= (3, 2):
        raise ValueError('This package requires Python 3.2 or above')
else:
    raise ValueError('Unrecognized major version of Python')

HERE = os.path.abspath(os.path.dirname(__file__))

try:
    import multiprocessing
except ImportError:
    pass

__project__      = 'Bluetooth-GPIO'
__version__      = '0.0.1'
__author__       = 'AlexProgrammerDE'
__url__          = 'https://github.com/AlexProgrammerDE/Bluetooth-GPIO'
__platforms__    = 'ALL'
__requires__ = [
    'gpiozero',
]
__keywords__ = [
    'raspberrypi',
    'gpio',
    'Bluetooth',
]

def main():
    import io
    with io.open(os.path.join(HERE, 'README.rst'), 'r') as readme:
       setup(
           name                          = __project__,
           version                       = __version__,
           author                        = __author__,
           long_description              = readme.read(),
           url                           = "https://github.com/AlexProgrammerDE/Bluetooth-GPIO",
           packages                      = find_packages(),
           platforms                     = __platforms__,
           include_package_data          = True,
           install_requires              = __requires__
           classifiers                   =[
        "Development Status :: 1 - Alpha",
        "License :: Apache License 2.0",
        "Programming Language :: Python",
        "Topic :: System :: Hardware :: Hardware Drivers :: Bluetooth"
                                   ]
)
