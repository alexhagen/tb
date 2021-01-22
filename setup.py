from setuptools import setup

setup(name='tb',
      version=0.1,
      description='Time Blocker',
      author='Alex Hagen',
      author_email='alexhagen6@gmail.com',
      url='https://github.com/alexhagen/tb',
      long_description=open('README.md').read(),
      packages=['tb'],
      scripts=['bin/tb'],
      install_requires=['rumps', 'py2app']
     )