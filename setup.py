# See the instructions at:
# https://www.codementor.io/arpitbhayani/host-your-python-package-using-github-on-pypi-du107t7ku


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
    #classifiers = [],
)

