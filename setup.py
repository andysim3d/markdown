from setuptools import setup, find_packages
setup(
    name='pymd',
    version='0.0.1',
    description='This is a purly python markdown parser and render',
    author='andysim3d, jinglongwu, VCneverdie, shawn-lo',
    url='https://github.com/andysim3d/markdown',
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    # packages=find_packages(exclude=('*test*')),
    # packages= ['src/render', 'src/blocks', 'src/parser'], 
    package_dir={'pymd': 'pymd'},
    license="GPL-3.0 License",
)