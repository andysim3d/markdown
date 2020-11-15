from os import path
from setuptools import setup, find_packages

# read the contents of your README file
THIS_DIRECTORY = path.abspath(path.dirname(__file__))
with open(path.join(THIS_DIRECTORY, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lightmd',
    version='0.0.1.2',
    description=
    'This is a light-weighted, purly python made markdown parser and render',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='andysim3d, jinglongwu, VCneverdie, shawn-lo',
    url='https://github.com/andysim3d/markdown',
    packages=find_packages(exclude=[
        "tests", "*.tests", "*tests.*", "tests.*", "test", "*.test", "*test.*",
        "test.*"
    ]),
    package_dir={'lightmd': 'lightmd'},
    license="GPL-3.0 License",
)
