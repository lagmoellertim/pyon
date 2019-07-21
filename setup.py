import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='pyon-lib',
    version='0.1.2',
    license='MIT License',
    author='Tim-Luca Lagmöller',
    author_email='hello@lagmoellertim.de',
    description='The Pythonic way to use JSON - with native objects and path support',
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
