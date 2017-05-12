from distutils.core import setup

DESC='A library for creating bots on the Matrix communication network.'

setup(
    name='matrix_bot_api',
    version='0.1',
    author='Shawn Anastasio',
    author_email='see github',
    url='https://github.com/shawnanastasio/python-matrix_bot_api',
    packages=['matrix_bot_api'],
    install_requires=['matrix_client'],
    license='GNU GPL v3',
    summary=DESC,
    long_description=DESC,
)
