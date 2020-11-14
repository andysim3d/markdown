from setuptools import setup, find_packages
setup(
    name='lightmd',
    version='0.0.1',
    description='This is a light-weighted, purly python made markdown parser and render',
    author='andysim3d, jinglongwu, VCneverdie, shawn-lo',
    url='https://github.com/andysim3d/markdown',
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    package_dir={'lightmd': 'lightmd'},
    license="GPL-3.0 License",
)