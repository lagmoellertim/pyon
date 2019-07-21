import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='pyon-lib',
    version='0.1.3',
    install_requires=requirements,
    license='MIT License',
    author='Tim-Luca Lagmöller',
    author_email='hello@lagmoellertim.de',
    description='Pythonic Object Notation - with native objects and path support',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/lagmoellertim/pyon',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
