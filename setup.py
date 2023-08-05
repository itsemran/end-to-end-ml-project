#responsible in creating ml application as a package
#we can install this package ,we can use it 
#we can install this package in other projects


from setuptools import find_packages,setup
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->list[str]:
    #here file_path sates it will be a string
    '''
    THIS FUNCTION WILL RETURN LIST OF REQUIREMENTS
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        # replacing \n with blank as it also get read when we read txt file
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name = 'mlproject',
    version='0.0.1',
    author='emran',
    author_email='itsemrankhan@gmail.com',
    packages= find_packages(),
    #install_requires=['pandas','numpy','seaborn']
# or we can just create a function as it will be very hactic to write all the packages we need
    install_requires=get_requirements('requirement.txt')
    # now lets define this function above 
)
