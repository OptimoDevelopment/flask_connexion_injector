from setuptools import setup, PEP420PackageFinder
from pip.req import parse_requirements

install_reqs = parse_requirements("requirements.txt", session="hack")
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='flask-optimo-demo',
    version='0.0.1',
    description='A flask connexion and injector project demo',
    url='https://github.com/OptimoDevelopment/flask_connexion_injector',
    author='OptimoDevelopment',
    author_email='developers@optimodevelopment.com',
    license='MIT',
    packages=PEP420PackageFinder.find(where='.', include=('fci'), exclude=('tests',)),
    install_requires=reqs,
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'run-server=fci.app:main',
        ],
    },
)