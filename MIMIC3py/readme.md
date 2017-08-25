# Downloading MIMIC III

The code is this library will help you:
1.  Download the MIMIC III files.
2.  Validate the downloaded files by verifying their MD5 hashes.
3.  Load the data into Pandas data frames.


Here's what you need to do:
1.  Get a username and password from the physinnet website:  https://mimic.physionet.org/gettingstarted/access/
2.  Open config.py.
    1.  Fill in your username and password
    2.  Enter the folder where you want the downloaded files to be stored.
    3.  Make sure you un-comment all of the files that you want to download
        * NOTE: some of the files can be HUGE (33 GB!!!!).
    4.  Save the filled-in confi.py file
3.  Run the download.py file.
    * NOTE:  you may need to first: pip install requests
    * See requirements.txt for a list of all the libraries you want need/want to install.

