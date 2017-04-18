#!/usr/bin/env python

from setuptools import setup, find_packages, Extension
from glob import glob

sources = glob('WiringOP-Zero/devLib/*.c')
sources += glob('WiringOP-Zero/wiringPi/*.c')
sources += ['wiringpi_wrap.c']

sources.remove('WiringOP-Zero/devLib/piFaceOld.c')

_wiringpi = Extension(
    '_wiringpi',
    include_dirs=['WiringOP-Zero/wiringPi','WiringOP-Zero/devLib'],
    sources=sources
)

setup(
    name = 'wiringpi',
    version = '2.32.1',
    author = "Philip Howard",
    author_email = "phil@gadgetoid.com",
    url = 'https://github.com/WiringPi/WiringPi-Python/',
    description = """A python interface to WiringPi 2.0 library which allows for
    easily interfacing with the GPIO pins of the Orange Pi Zero. Also supports
    i2c (and SPI seems not to work)""",
    long_description=open('README.md').read(),
    ext_modules = [ _wiringpi ],
    py_modules = ["wiringpi"],
    install_requires=[],
    headers=glob('WiringOP-Zero/wiringPi/*.h')+glob('WiringOP-Zero/devLib/*.h')
)
