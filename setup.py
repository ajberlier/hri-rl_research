from distutils.core import setup
from setuptools import find_packages

install_requires = [
]

setup(
   name='hrirl_reserach',
   version='0.1',
   description="Adam J. Berlier's Ph.D. research codebase",
   author='Adam J. Berlier',
   author_email='ajberlier@gmail.com',
   packages=find_packages(),
   install_requires=install_requires,
)