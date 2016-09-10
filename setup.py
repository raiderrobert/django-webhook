import os
from setuptools import find_packages, setup

VERSION = __import__('webhook').__version__
NAME = 'webhook'
URL = 'https://github.com/raiderrobert/django-webhook/'

def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


setup(
    name=NAME,
    version=VERSION,
    author='Robert Roskam',
    author_email='me@robertroskam.com',
    install_requires=['django>=1.8',],
    packages=find_packages(),
    include_package_data=True,  # declarations in MANIFEST.in
    license='MIT',
    url=URL,
    download_url=URL+'/tarball/'+VERSION,
    description="Make webhooks in Django more easily",
    long_description=read_file('README.md'),
    keywords=['webhooks', 'HTTP callbacks', 'web API'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
