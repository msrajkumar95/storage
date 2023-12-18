from setuptools import setup, find_packages


setup(
    name='storage',
    version='0.1',
    description='Storage Assignment for Sacumen',
    long_description=open('README.md').read(),
    author='Rajkumar Srinivasan',
    url='https://github.com/msrajkumar95/storage',
    packages=find_packages(exclude=['tests*']),
    python_requires='>=3.6',
)
