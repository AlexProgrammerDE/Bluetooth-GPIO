 #!/usr/bin/env python

from setuptools import setup, find_packages

__project__      = 'Bluetooth-GPIO'
__version__      = '0.0.1'
__author__       = 'AlexProgrammerDE'
__url__          = 'https://github.com/AlexProgrammerDE/Bluetooth-GPIO'
__platforms__    = 'ALL'
__requires__ = [
    'gpiozero',
]



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
