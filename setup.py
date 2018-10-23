try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(
    name='t-gl',
    version='0.0.0',
    author="Brendan O'Leary",
    author_email='boleary@olearycrew.com',
    url='http://bitbucket.org/sjl/t',
    py_modules=['t'],
    entry_points={
        'console_scripts': [
            't = t:_main',
        ],
    },
)
