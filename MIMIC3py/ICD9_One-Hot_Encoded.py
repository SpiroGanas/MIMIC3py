# Spiro Ganas
# 11/15/17
#
# One-hot encodes the ICD9 data at a patient level

from MIMIC3py.load_to_pandas import load_mimic_to_pandas
import pandas as pd


Location_of_the_CSV_Files = "D:\\MIMIC-III Clinical Database\\Data\\"
df = load_mimic_to_pandas(CSV_Folder_Location=Location_of_the_CSV_Files, CSV_List=['DIAGNOSES_ICD'], gunzip=False)



# Number of rows in the original data.
#print(len(df['DIAGNOSES_ICD'].index))


x=0

one_hot = {}
for index, row in df['DIAGNOSES_ICD'].iterrows():
    patient = row['SUBJECT_ID']
    icd = row['ICD9_CODE']



    if patient in one_hot:
        if icd not in one_hot[patient]:
            one_hot[patient][icd] = 1
    else:
        one_hot[patient] = {icd : 1}

    #x+=1
    #if x>10000: break



# Convert the sparse "dictionary of dictionaries" to a pandas dataframe.
one_hot_df = pd.DataFrame(one_hot, dtype=int)

# Replace in all the NaN values with 0
one_hot_df = one_hot_df.fillna(0)

# Transpose the DataFrame so rows represent a single patient and each column represents the presence an ICD9 code.
one_hot_df = one_hot_df.transpose()




print("memory used: ", one_hot_df.memory_usage().sum()/1000/1000, " MB")
print()
print(one_hot_df.head())
