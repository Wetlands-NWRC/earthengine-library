from setuptools import find_packages, setup

if __name__ == "__main__":

    setup(
        name='earth-engine-library',
        author="Ryan Hamilton",
        packages=find_packages(exclude=('tests*'))
    )
