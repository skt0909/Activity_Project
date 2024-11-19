##Important for Packaging and distributing Project 

from setuptools import find_packages,setup ##Consider folder as packages
from typing import List  ##

def get_requirements()->List[str]:
    """
    Returns list of requirments.txt

    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines() ##Reads lines from the file.
            for line in lines:     ##Processes each line.
                requirement=line.strip()
                if requirement and requirement!= '-e .': ## ignore empty lines and -e . 
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list
print(get_requirements())

setup(
    name="activity",  # Replace with your package name
    version="0.1.0",  # Replace with your version
    author="Saket",
    author_email="saket.lambe@gmail.com",
    packages=find_packages(),  # Automatically find packages
    install_requires=get_requirements()  # Install dependencies
)
