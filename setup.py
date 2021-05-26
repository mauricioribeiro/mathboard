from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='mathboard',
    version='0.1.0',
    author='Mauricio Ribeiro',
    author_email='mauricioribeiro1992@gmail.com',
    packages=['mathboard', 'mathboard.test'],
    scripts=[],
    url='http://pypi.python.org/pypi/mathboard/',
    license='LICENSE.txt',
    description='A fun library to make math operations',
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=[],
)

