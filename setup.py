from setuptools import setup, find_packages

setup(
    name='mypackages',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
    ],
    entry_points={
        'console_scripts': [
            # Define any command-line scripts here
        ],
    },
    author='Himbaza Mugisha',
    description='return top n number of given items in a descending order',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
