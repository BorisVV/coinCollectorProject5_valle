from setuptools import setup

setup(
    name='CoinCollectorApp_Proj5',
    version='0.1',
    packages=[
        'coinCollectorApp_Proj5',
        'coinSite'],
    install_requires=[
        "requests",
        "psycopg2",],

    author='Boris V',

    packages=find_packages(exclude=['tests*']),

    long_description=open('README.md').read(),
    # ...
)
