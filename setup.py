"""Package installer."""
import os
from setuptools import setup
from setuptools import find_packages

LONG_DESCRIPTION = ''
if os.path.exists('README.md'):
    with open('README.md') as fp:
        LONG_DESCRIPTION = fp.read()

scripts = []

setup(
    name='lion',
    version='1.3.0',
    description='Linear infrastructure optimization networks',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author='Nina Wiedemann',
    author_email=('wnina@ethz.ch'),
    url='https://gitlab.ethz.ch/wnina/lion',
    license='MIT',
    install_requires=['numpy', 'numba', 'matplotlib', 'scipy'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=find_packages('.'),
    scripts=scripts
)
