from setuptools import setup
from version import __release__

setup(
        name = 'nptime',
        version = __release__,
        author = 'Thomas Grenfell Smith',
        author_email = 'thomathom@gmail.com',
        description = 'Non-pedantic replacement for datetime.time',
        long_description = open('README.rst').read(),
        license = 'LICENSE.txt',
        keywords = 'time datetime timedelta',
        py_modules = ['nptime'],

        tests_require = ['Nose'],
        )

