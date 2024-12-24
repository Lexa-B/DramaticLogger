from setuptools import setup, find_packages

# Read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "readme.md").read_text()

setup(
    name='DramaticLogger',
    version='0.0.1',
    author='Lexa-B',
    author_email='Lexa.40@proton.me',
    description='A dramatic logging tool built on top of Loguru',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Lexa-B/DramaticLogger',
    packages=find_packages(),
    install_requires=[
        'loguru>=0.5.3',  # Specify Loguru version as needed
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Update if using a different license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify your supported Python versions
    entry_points={
        'console_scripts': [
            'dramatic_logger=dramatic_logger.DramaticLogger:main',  # If you have a main function
        ],
    },
)
