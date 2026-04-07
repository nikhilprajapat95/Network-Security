'''
The setup.py file is an essential part of packaging and 
distributing a Python project. It is used by setuptools
(or distutils in older Python versions) to define the configuratuon
of your project, such as metadata, dependencies, and more.
'''
from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """Reads the requirements from a file and returns them as a list."""
    requirement_lst: List[str] = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirements = line.strip()
                # ignore empty lines and -e.
                if requirements and requirements!="-e .":
                    requirement_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirement_lst 

setup(
    name='NetworkSecurity',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='A machine learning project for network security.',
    author='Nikhil Prajapat',
    author_email='nikhilprajapat955@gmail.com'
)