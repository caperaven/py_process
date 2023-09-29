from setuptools import setup, find_packages

setup(
    name='process_api',
    version='0.0.1',
    description='A extendable library that enables intent driven development by allowing code and json execution of development intent',
    author='caperaven',
    author_email='caperaven@caperaven.co.za',
    license='MIT OR Commercial',
    packages=[
        'process_api',
        'process_api.expressions',
        'process_api.modules',
        'process_api.modules.selenium',
        'process_api.modules.selenium.automation',
        'process_api.modules.selenium.condition_callbacks',
        'process_api.modules.selenium.conversions',
        'process_api.modules.selenium.modules',
        'process_api.schema_runner',
        'process_api.utils'
    ]
)