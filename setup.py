# Notes on releasing the software to pypi
#
# Step 1: Update this file with the new version number.
# Step 2: Make sure everything has been commited and pushed to GitHub.
# Step 3: Create a new release on GitHub.
# Step 4: package the source file by running:  python setup.py sdist
# Step 5: Create an installation "wheel" by running:  python setup.py bdist_wheel
# Step 6: Delete any old files in the dist folder
# Step 7: Do an upload to pypi Test Server by running this in the terminal:
#         C:\ProgramData\Anaconda3\Scripts\twine.exe upload --repository-url https://test.pypi.org/legacy/ dist/*
# Step 8: Upload to the production pypi server by running this in the terminal:
#         C:\ProgramData\Anaconda3\Scripts\twine.exe upload --repository-url https://upload.pypi.org/legacy/ dist/*
# Step 9: Test everything by running: pip install MIMIC3py





import setuptools  #This import allows me to create the wheel file
from distutils.core import setup

setup(
    name = 'MIMIC3py',
    packages = ['MIMIC3py'],
    version = '0.11',  # Ideally should be same as your GitHub release tag varsion
    description = 'A Python library to load and analyze the MIMIC III Critical Care Database.',
    author = 'Spiro Ganas',
    author_email = 'spiroganas@gatech.edu',
    url = 'https://github.com/SpiroGanas/MIMIC3py',
    download_url = 'https://github.com/SpiroGanas/MIMIC3py/archive/v0.11.tar.gz',
    keywords = ['MIMIC', 'Critical Care', 'Informatics'],
    classifiers = [
                    'Development Status :: 2 - Pre-Alpha',
                    'License :: OSI Approved :: MIT License',
                    'Programming Language :: Python :: 3',
                    'Intended Audience :: Healthcare Industry',
                    'Intended Audience :: Science/Research'
                    ],
    install_requires=['pandas', 'numpy', 'scikit-learn', 'requests'],
    python_requires='>=3',
)

