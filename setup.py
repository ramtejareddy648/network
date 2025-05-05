from setuptools import find_packages,setup
from typing import List


get_requirements_list:List[str]=[]
def get_requirements()->List[str]:
    
    try:
        
     with open('requirements.txt','r') as file:
        lines=file.readlines()
        
        for line in lines:
            requirement=line.strip()
            
            if requirement and requirement!='-e .':
                get_requirements_list.append(requirement)
    except FileNotFoundError:
        print('filenotfound')
    
    
    return get_requirements_list



###print(get_requirements())
setup(
    name='network',
    version='0.0.1',
    author='reddy',
    author_email='ramtejareddy2@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
    