from setuptools import setup, find_packages

# Try to convert markdown README to rst format for PyPI.
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='cohesity_sdk',
    version='1.0.0',
    description='This API provides operations for interfacing with the Cohesity Cluster.',
    long_description=long_description,
    author='Cohesity API Ecosystem Team.',
    author_email='cohesity-api-sdks@cohesity.com',
    url='https://github.com/cohesity/',
    packages=find_packages(),
    install_requires=[
        'requests>=2.9.1, <3.0',
        'jsonpickle>=0.7.1, <1.0',
        'cachecontrol>=0.11.7, <1.0',
        'python-dateutil>=2.5.3, <3.0'
    ]
)