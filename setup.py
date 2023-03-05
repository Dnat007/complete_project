from setuptools import find_packages,setup

from typing import List
dot ='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]

        if dot in requirements:
            requirements.remove(dot)
    return requirements


setup(
    name='complete_project',
    version='0.0.1',
    author='Dnat007',
    author_email='abhishek.singh2_cs19@gla.ac.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)