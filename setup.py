from setuptools import setup, find_packages

setup(
    name="data-finder-pro",
    version="4.0",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'data-finder=finder:main',
        ],
    },
    author="Mamun",
    description="Advanced Security Scanner & Data Auditor",
    url="https://github.com/zxmoon76-sys/Data-Finder-Pro",
)
