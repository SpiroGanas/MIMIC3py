# Spiro Ganas
#
# Test script to make sure my utility functions work property.


import pytest
from MIMIC3.utilities import *


def test_D_CPT_Zipped():
    assert(verifyData('D_CPT.csv.gz')==True)


def test_Bad_Input():
    with pytest.raises(FileNotFoundError):
        md5("BadInput")

