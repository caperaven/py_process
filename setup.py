from setuptools import setup, find_packages

setup(
    name='process_api',
    version='0.0.1',
    description='A extendable library that enables intent driven development by allowing code and json execution of development intent',
    author='caperaven',
    author_email='caperaven@caperaven.co.za',
    license='MIT OR Commercial',
    packages=find_packages(where='process_api'),
)