from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt',encoding='utf-8') as req:
        return req.read().splitlines()


setup(
    name='dpl',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'dpl=dpl.cli:cli',
        ],
    },
    author='sokumom',
    author_email='sohamkulkarns@gmail.com',
    description='A simple CLI to add tasks to Google Sheets',
    keywords='cli tasks google-sheets',
    url='https://github.com/sokumon/dpl',  # Replace with your project's URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
