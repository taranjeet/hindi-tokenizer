import os
import sys
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

VERSION = __import__('hinditokenizer').__version__

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Programming Language :: Python :: 2.7',
    'Topic :: Software Development :: Build Tools',
]

setup(
    name='hinditokenizer',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Package which implements tokenization for Hindi language',
    long_description=README,
    url='https://github.com/staranjeet/hindi-tokenizer',
    author='Taranjeet Singh',
    author_email='reachtotj@gmail.com',
    keywords="hindi, tokenization, hindi-tokenizer, nlp",
    classifiers=CLASSIFIERS,
)
