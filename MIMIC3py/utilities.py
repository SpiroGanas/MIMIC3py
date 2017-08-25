# Spiro Ganas
#
# Utility code and other small functions


import os
import hashlib

from MIMIC3py.config import *


def verify_data(file_to_verify, local_save_folder=local_save_folder):
    """Calculates the MD5 value of a downloaded file and returns true if that value
       matches the value in the checksum file"""

    # From the files checksum_md5_unzipped.txt and checksum_md5_zipped.txt, available on physionet.org
    checksums = {
        'ADMISSIONS.csv.gz': 'f301f427b38268ae9b3e129f49484b8d',
        'CALLOUT.csv.gz': 'f9443602f929725d0d240edde9c37848',
        'CAREGIVERS.csv.gz': '14e103974ac30c7e8ec92fa15966730a',
        'CHARTEVENTS.csv.gz': '6322b029b09e75a8aa7c692eec2b656c',
        'CPTEVENTS.csv.gz': '88ec8e5aa63f3f50c49b67482a0a691d',
        'DATETIMEEVENTS.csv.gz': '68b7b786469c66af182bc0d41a4d9e69',
        'D_CPT.csv.gz': '4801e130461a147e647cd4c3e4579208',
        'DIAGNOSES_ICD.csv.gz': '1d8007cc3115fd87a95321df33e1de86',
        'D_ICD_DIAGNOSES.csv.gz': '9c5b6a1e0c6ebe7a96b99441ca9c0499',
        'D_ICD_PROCEDURES.csv.gz': '7927c2e262485b69ae6dd31359faa664',
        'D_ITEMS.csv.gz': '83413729fa45a4d594e9a530bfbad911',
        'D_LABITEMS.csv.gz': '75e79ca14a2b8c02e3535b87498c4f9d',
        'DRGCODES.csv.gz': '34f5b2327cda3ffa53089b6c23b53191',
        'ICUSTAYS.csv.gz': '79f2b70cb07a6598642e04aaa364c27c',
        'INPUTEVENTS_CV.csv.gz': '1d02246e9fd8d379a4e0c41623890c25',
        'INPUTEVENTS_MV.csv.gz': 'f49043f52cd3ee121f36b66e5504a9c0',
        'LABEVENTS.csv.gz': '9d78e309dc5b5fcf80e34803a688a354',
        'MICROBIOLOGYEVENTS.csv.gz': 'b600550677d8dd8d13184f40c5162093',
        'NOTEEVENTS.csv.gz': '90c05ebe5e7e631f0a55f34f568fbfc0',
        'OUTPUTEVENTS.csv.gz': 'c98f08478614282571557017264468c6',
        'PATIENTS.csv.gz': '4383677427d53def256367a7c94a6b31',
        'PRESCRIPTIONS.csv.gz': '15c67d6d84e88ec57044064e170390f6',
        'PROCEDUREEVENTS_MV.csv.gz': '118ab22f1d98ef21de8e75154574d617',
        'PROCEDURES_ICD.csv.gz': 'be9d0a0ce5acf0bbda1b61fe66353c89',
        'SERVICES.csv.gz': '48d2da2ab02aba284a7a10962b93b061',
        'TRANSFERS.csv.gz': '4440b72090dc9207c88368cfb1ae2146',
        'ADMISSIONS.csv': '57d940b69dd066da5ba57e008cc7f92c',
        'CALLOUT.csv': 'cd4e416337e68f6678ff4e091938be58',
        'CAREGIVERS.csv': '258e3c2bc11798c99ffc4f33aa1e9bcd',
        'CHARTEVENTS.csv': '2b5211d1045ffac4c4e345ccb56ccc1b',
        'CPTEVENTS.csv': 'bf32e07ecd2b946a675a0d7cea75d2e7',
        'DATETIMEEVENTS.csv': '6245f2f4f581dce8e05e147228a51522',
        'D_CPT.csv': '49fdda583f5e85e5e0a92686b3106fac',
        'DIAGNOSES_ICD.csv': 'e2c0a05d768a6273038ae84e576186a7',
        'D_ICD_DIAGNOSES.csv': 'd0a7026ca3618f4360d8329643d9041d',
        'D_ICD_PROCEDURES.csv': 'a9707e5361f939f45ca2bc2eb8bd5652',
        'D_ITEMS.csv': '749e350c22531ec8589b7391b4e7b660',
        'D_LABITEMS.csv': '2f77db8fc2f2a21e4fad1a1781d98709',
        'DRGCODES.csv': 'ea61c7dfe180c6d6a1273f220b5e70c5',
        'ICUSTAYS.csv': 'b2a57affcda3c60fa38a022b2df7fcf2',
        'INPUTEVENTS_CV.csv': '5fce8501d6723a470c74affcda32e52b',
        'INPUTEVENTS_MV.csv': '4d57864670f51e7230c0fef52d206049',
        'LABEVENTS.csv': 'bc2fe94983576207758635924c047dbe',
        'MICROBIOLOGYEVENTS.csv': '0a35833252bdecb32b9d1348adec2085',
        'NOTEEVENTS.csv': 'df33ab9764256b34bfc146828f440c2b',
        'OUTPUTEVENTS.csv': '6e137e00d7a7fd14c291d015573ed375',
        'PATIENTS.csv': '3b06f45153c66e2b7c49b35805971145',
        'PRESCRIPTIONS.csv': '43f469da09c65bae252d02a51787ad85',
        'PROCEDUREEVENTS_MV.csv': '8a73340cf7a09d8f42ddd64f4863fff3',
        'PROCEDURES_ICD.csv': 'ed7e6f1efa7e334404f6fb26e4c3c7d2',
        'SERVICES.csv': '52259c657c4fd4bc43bcb35ec5c96d98',
        'TRANSFERS.csv': '136b75c89bec2aab588ca64cd4b582bd'
    }
    try:
        return checksums[file_to_verify] == md5(os.path.join(local_save_folder, file_to_verify))
    except FileNotFoundError:
        # If the file doesn't exist, return false
        return False
    except KeyError:
        # If I don't have an MD5 hash in the dictionary, return false
        return False


def md5(fname):
    """Calculates the MD5 checksum of the file.
       SOURCE:  https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
    """
    try:
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except FileNotFoundError:
        raise FileNotFoundError


def verify_all(local_save_folder=local_save_folder):
    """Loops over every file in the folder and determines if it's a valid MIMIC III file"""
    # TODO:  Implement verifyAll function
    pass


if __name__ == "__main__":
    print(verify_data('D_CPT.csv.gz'))
    print(verify_data('D_CPT.csv.gzsdsdsd'))
    print(verify_data('ADMISSIONS.csv.gz'))
