from setuptools import setup

setup(name='adjusty',
      version='1.1',
      description='A Simplified Python implementation of Adjust API for the KPI service',
      url='http://github.com/techieashish/adjusty',
      author='Ashish Srivastava',
      author_email='ashisharivastava1872@gmail.com',
      packages=['adjusty'],
      install_requires=['requests'],
      zip_safe=False)