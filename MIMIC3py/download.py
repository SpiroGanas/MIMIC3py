# Spiro Ganas
#
# Python program to download MIMIC III csv files from

import requests
import urllib.parse

from MIMIC3py.config import *
from MIMIC3py.utilities import verify_data


def download_mimic3_files(physionet_filenames=physionet_FILENAMES):
    """ Downloads the MIMIC 3 critical care database csv files.
        The CVS file are zipped in the .gz format.
        You can upzip the files, or just load the .gz file
        directly into a Pandas data frame.
    """

    for file in physionet_filenames:
        url = urllib.parse.urljoin(physionet_BASE_URL, file)
        success = download_file(url)
        print(success)


def download_file(url, save_folder=local_save_folder, username=physionet_USERNAME, password=physionet_PASSWORD):
    """ This code downloads files from a password protected http site.
        https://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
    """

    if not verify_physionet_credentials(username, password): return "Error: Username/Password invalid."



    local_filename = url.split('/')[-1]

    # If the file already exists, don't download it again
    if verify_data(local_filename, save_folder):
        return "Verified existing file: " + local_filename

    # NOTE the stream=True parameter
    r = requests.get(url, auth=(username, password), stream=True)
    with open(save_folder + local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    # If the file already exists, don't download it again
    if verify_data(local_filename, save_folder):
        return "Downloaded and successfully verified: " + local_filename
    else:
        return "Downloaded but FAILED TO VERIFY: " + local_filename





def verify_physionet_credentials(username, password):
    """Returns True if the username and password are valid for the physionet.org website."""
    url = "https://physionet.org/works/MIMICIIIClinicalDatabase/files/"
    r = requests.get(url, auth=(username, password))
    return True if r.status_code == 200 else False




if __name__ == "__main__":
    print("Verifying existing files and downloading any missing files.")
    print("Please Wait...")
    print()
    download_mimic3_files(physionet_FILENAMES)
