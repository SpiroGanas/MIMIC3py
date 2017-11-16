# Spiro Ganas
#
# This file contains all the configuration data (username, password, etc.)



# This is the folder where the files will located
local_save_folder = "D:\\MIMIC-III Clinical Database\\Data\\"

############ ENTER YOUR PHYSIONET USERNAME AND PASSWORD HERE ###################
physionet_USERNAME = ""
physionet_PASSWORD = ""
################################################################################

# You may need to update some of these variables if MIMIC III gets updated
physionet_BASE_URL = "https://physionet.org/works/MIMICIIIClinicalDatabase/files/version_1_4/"

# Comment out any file you don't want to download.
# Note that some of the files are very, very big.
physionet_FILENAMES = [
    "ADMISSIONS.csv.gz",  # 12 MB
    "CALLOUT.csv.gz",  # 6.1 MB
    "CAREGIVERS.csv.gz",  # 199 KB
    "CHARTEVENTS.csv.gz",         # 33 GB ------BIG!!!
    "CPTEVENTS.csv.gz",  # 56 MB
    "DATETIMEEVENTS.csv.gz",      # 502 MB
    "D_CPT.csv.gz",  # 14 KB
    "DIAGNOSES_ICD.csv.gz",  # 19 MB
    "D_ICD_DIAGNOSES.csv.gz",  # 1.4 KB
    "D_ICD_PROCEDURES.csv.gz",  # 305 KB
    "D_ITEMS.csv.gz",  # 933 KB
    "D_LABITEMS.csv.gz",  # 43 KB
    "DRGCODES.csv.gz",  # 11 MB
    "ICUSTAYS.csv.gz",  # 6.1 MB
    "INPUTEVENTS_CV.csv.gz",      # 2.3 GB ------BIG!!!
    "INPUTEVENTS_MV.csv.gz",      # 931 MB
    "LABEVENTS.csv.gz",           # 1.8GB ------BIG!!!
    "MICROBIOLOGYEVENTS.csv.gz",  # 70 MB
    "NOTEEVENTS.csv.gz",          # 3.8 GB  ------BIG!!!
    "OUTPUTEVENTS.csv.gz",  # 379 MB
    "PATIENTS.csv.gz",  # 2.6 MB
    "PRESCRIPTIONS.csv.gz",       # 735 MB
    "PROCEDUREEVENTS_MV.csv.gz",  # 47 MB
    "PROCEDURES_ICD.csv.gz",  # 6.5 MB
    "SERVICES.csv.gz",  # 3.4 MB
    "TRANSFERS.csv.gz",  # 24 MB
]
