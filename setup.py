from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Return list of requirements
    """
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Siddhesh',
    author_email='siddheshtripathi236@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)