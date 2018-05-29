from setuptools import setup, find_packages

setup(
    name='some_package',
    description='Demonstrate packaging and distribution',

    version='1.0',
    author='Yung-Jin (Joey) Hu',
    author_email='yungjinhu@gmail.com',
    url='https://github.com/TheGhostHuCodes/PTwP',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
