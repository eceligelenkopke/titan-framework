from setuptools import setup, find_packages

setup(
    name='titan_framework',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pytest',
        'pytest-bdd',
        'selenium',
        'requests',
        'pymysql',
        'allure-pytest'
    ]
)