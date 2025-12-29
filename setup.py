from setuptools import setup, find_packages

setup(
    name='seqdb',
    version='0.1.0',
    description='A database system for managing sequencing data',
    author='Ji Wang',
    author_email='gynecoloji@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pandas>=2.0.0',
        'pyarrow>=12.0.0',
        'duckdb>=0.9.0',
        'click>=8.0.0',
    ],
    entry_points={
        'console_scripts': [
            'seqdb=seqdb.cli:main',  # Command-line tool
        ],
    },
    python_requires='>=3.12',
)