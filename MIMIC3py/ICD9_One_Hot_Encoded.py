# Spiro Ganas
# 11/15/17
#
# One-hot encodes the ICD9 data at a patient level

from MIMIC3py.load_to_pandas import load_mimic_to_pandas
import pandas as pd









def one_hot_encoder(dictionary_of_Dictionaries: dict)-> pd.DataFrame:
    '''Accepts a dictionary of dictionaries and returns a one-hot encoded pandas dataframe.
       The outer key is the subject_id, the inner key is an ICD9 code, and the value is always 1.
       The returned DataFrame has subject_id as the rows and ICD9s as the columns, with 1 meaning
       the patient had that illness and 0 meaning they didn't
       '''

    # Convert the sparse "dictionary of dictionaries" to a pandas dataframe.
    one_hot_df = pd.DataFrame(dictionary_of_Dictionaries, dtype=int)

    # Replace in all the NaN values with 0
    one_hot_df = one_hot_df.fillna(0)

    # Transpose the DataFrame so rows represent a single patient and each column represents the presence an ICD9 code.
    one_hot_df = one_hot_df.transpose()
    return one_hot_df



def get_ICD9_descriptions(filename = None):
    '''Returns a pandas DataFrame containing ICD9 codes and their text descriptions.
       The file comes from CMS:  https://www.cms.gov/Medicare/Coding/ICD9ProviderDiagnosticCodes/codes.html
    '''
    # TODO: Implement this function and move it to a utility module
    pass



def Rollup_ICD9_Code(IDC9_Code: str)-> str:
    '''Rolls up the ICD9 codes to the 3 character level'''
    if str(IDC9_Code)[0]== 'E' or str(IDC9_Code)[0]== 'V':
        return str(IDC9_Code)[:4]  # E and V codes are rolled up to 4-character
    else:
        return str(IDC9_Code)[:3]




def ICD9_One_HotEncoded(Location_of_the_CSV_Files = "D:\\MIMIC-III Clinical Database\\Data\\", print_details = False):
    '''Imports the Subject_IDs and ICD9 Codes from the DIAGNOSES_ICD.csv and outputs the
       data as a one-hot encoded matrix where each row is a patient and each column is
       a disease.
       '''

    df = load_mimic_to_pandas(CSV_Folder_Location=Location_of_the_CSV_Files, CSV_List=['DIAGNOSES_ICD'], gunzip=False)



    one_hot = {}
    for index, row in df['DIAGNOSES_ICD'].iterrows():
        patient = row['SUBJECT_ID']
        icd = Rollup_ICD9_Code(row['ICD9_CODE'])   # I rill up the ICD 9 to the 3-character level

        if patient in one_hot:
            if icd not in one_hot[patient]:
                one_hot[patient][icd] = 1
        else:
            one_hot[patient] = {icd : 1}


    one_hot_df = one_hot_encoder(one_hot)

    # These are the icd9 column names
    My_column_names = list(one_hot_df.axes[1])



    # Print a summary of the one-hot encoded dataframe
    if print_details:
        print("memory used: ", one_hot_df.memory_usage().sum()/1000/1000, " MB")
        print("Shape: ", one_hot_df.shape)
        print()
        print(one_hot_df.head())

    return one_hot_df



#    import MIMIC3py.ICD9_One_Hot_Encoded
#
#    x = MIMIC3py.ICD9_One_Hot_Encoded.MyPCA


