from setuptools import setup

setup(
    name='CoinCollectorApp_Proj5',
    version='0.1',
    python = 'python 3.6'
    packages=[
        'coinCollectorApp',
        'coinSite'],
    install_requires=[
        "requests",
        "psycopg2",
        "django",
        "beautifulsoup4",
        "Jinja2",
        ],

    author='Boris V',

    packages=find_packages(exclude=['tests*']),

    long_description=open('README.md').read(),
    # ...
)
