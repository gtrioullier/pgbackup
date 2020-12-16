from setuptools import find_packages, setup

with open ('README.md', 'r') as readme_file:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='',
    autho_email='',
    description='A utility for backing up PostgreSQL databases.',
    lond_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github/gtrioullier/pgbackup',
    packages=find_packages('src')
)