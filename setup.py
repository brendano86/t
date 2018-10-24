try:
    from setuptools import setup
except:
    from distutils.core import setup

from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

pfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pfile['packages'], r=False)
test_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)

setup(
    name='t-gl',
    version='0.0.0',
    author="Brendan O'Leary",
    author_email='boleary@olearycrew.com',
    url='https://gitlab.com/brendan/t-gl',
    install_requires=requirements,
    py_modules=['t', 'helpers'],
    entry_points={
        'console_scripts': [
            't = t:_main',
        ],
    },
)
