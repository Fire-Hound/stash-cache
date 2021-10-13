from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Stash helps you to safely persist your function cache.'
LONG_DESCRIPTION = 'Stash gives you your functions the superpower of remembrance. Stash speeds up your functions by stashing their output and only running them when the argument or the body of the function changes.'

# Setting up
setup(
    name="stash-cache",
    version=VERSION,
    author="Vikram Cothur",
    author_email="vcothur7@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    # These are extra/optional dependencies that are required for development and testing
    extras_require={
        "dev": [
            "pytest>=3.7"
        ],
    },

    keywords=['python', 'cache', 'persistent',
              'stash', 'function', 'stash cache'],

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
