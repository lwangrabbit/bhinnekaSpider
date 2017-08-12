from setuptools import setup
import os


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name='behinnekaSpider',
    packages=['behinnekaSpider'],
    version="1.0",
    author='xxx',
    author_email='xxx@**.com',
    description='bhinneka spider',
    url='',
    license='',
    long_description=read('README.md'),
    install_requires=read('requirements.txt'),
    tests_require=[
        'pytest-runner>=2.11.1',
        'pytest>=3.1.0',
    ],
)
