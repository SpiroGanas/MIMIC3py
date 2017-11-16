# This function returns the MIMIC-III data as a dictionary of pandas data sets


import pandas as pd
import os.path


def load_mimic_to_pandas(CSV_Folder_Location='/data/', CSV_List=None, gunzip=False):
    """Returns a dictionary where the key is the file name and the value is a Pandas
       dataframe containing the data.
    """
    MIMIC_df = {}

    # Load the dictionary of dtypes from the function below
    dtypes = Mimic_dtypes()

    # if the files are still .gz archive files, set gunzip=True
    # if the files have already been decompressed to .csv format, gunzip should be false
    fileNameExtension = '.csv.gz' if gunzip else '.csv'
    compressionType = 'gzip' if gunzip else None

    # If the user doesn't tell us what tables to load, we load all the tables.
    # Note that some of the tables are very large, so you may need 50+ GB of memory to load them.
    if CSV_List is None:
        CSV_List = ['ADMISSIONS',  # 12 MB
                    'CALLOUT',  # 6.1 MB
                    'CAREGIVERS',  # 199 KB
                    'CHARTEVENTS',  # 33 GB ------BIG!!!
                    'CPTEVENTS',  # 56 MB
                    'DATETIMEEVENTS',  # 502 MB
                    'DIAGNOSES_ICD',  # 19 MB
                    'DRGCODES',  # 11 MB
                    'D_CPT',  # 14 KB
                    'D_ICD_DIAGNOSES',  # 1.4 KB
                    'D_ICD_PROCEDURES',  # 305 KB
                    'D_ITEMS',  # 933 KB
                    'D_LABITEMS',  # 43 KB
                    'ICUSTAYS',  # 6.1 MB
                    'INPUTEVENTS_CV',  # 2.3 GB ------BIG!!!
                    'INPUTEVENTS_MV',  # 931 MB
                    'LABEVENTS',  # 1.8GB ------BIG!!!
                    'MICROBIOLOGYEVENTS',  # 70 MB
                    'NOTEEVENTS',  # 3.8 GB  ------BIG!!!
                    'OUTPUTEVENTS',  # 379 MB
                    'PATIENTS',  # 2.6 MB
                    'PRESCRIPTIONS',  # 735 MB
                    'PROCEDUREEVENTS_MV',  # 47 MB
                    'PROCEDURES_ICD',  # 6.5 MB
                    'SERVICES',  # 3.4 MB
                    'TRANSFERS',  # 24 MB
                    ]

    for MyFile in CSV_List:
        try:
            MIMIC_df[MyFile] = pd.read_csv(os.path.join(CSV_Folder_Location, (MyFile + fileNameExtension)),
                                           dtype=dtypes[MyFile],
                                           parse_dates=True,
                                           sep=',',
                                           index_col='ROW_ID',
                                           compression=compressionType
                                           )
        except:
            print('Unable to load the file: ', MyFile)

    return MIMIC_df


def Mimic_dtypes():
    """Returns a dictionary of dictionaries.
       Each dictionary is a list of column names
       and their pandas data type.
       Note that any numeric field that can contain
       a null must be declared as a float (its a pandas bug).
    """
    dtypes = {}
    dtypes['ADMISSIONS'] = {'ROW_ID': int,
                            'SUBJECT_ID': int,
                            'HADM_ID': float,
                            'ADMITTIME': str,
                            'DISCHTIME': str,
                            'DEATHTIME': str,
                            'ADMISSION_TYPE': str,
                            'ADMISSION_LOCATION': str,
                            'DISCHARGE_LOCATION': str,
                            'INSURANCE': str,
                            'LANGUAGE': str,
                            'RELIGION': str,
                            'MARITAL_STATUS': str,
                            'ETHNICITY': str,
                            'EDREGTIME': str,
                            'EDOUTTIME': str,
                            'DIAGNOSIS': str,
                            'HOSPITAL_EXPIRE_FLAG': float,
                            'HAS_CHARTEVENTS_DATA': float,
                            }
    dtypes['CALLOUT'] = {'ROW_ID': int,
                         'SUBJECT_ID': float,
                         'HADM_ID': float,
                         'SUBMIT_WARDID': float,
                         'SUBMIT_CAREUNIT': str,
                         'CURR_WARDID': float,
                         'CURR_CAREUNIT': str,
                         'CALLOUT_WARDID': float,
                         'CALLOUT_SERVICE': str,
                         'REQUEST_TELE': float,
                         'REQUEST_RESP': float,
                         'REQUEST_CDIFF': float,
                         'REQUEST_MRSA': float,
                         'REQUEST_VRE': float,
                         'CALLOUT_STATUS': str,
                         'CALLOUT_OUTCOME': str,
                         'DISCHARGE_WARDID': float,
                         'ACKNOWLEDGE_STATUS': str,
                         'CREATETIME': str,
                         'UPDATETIME': str,
                         'ACKNOWLEDGETIME': str,
                         'OUTCOMETIME': str,
                         'FIRSTRESERVATIONTIME': str,
                         'CURRENTRESERVATIONTIME': str,
                         }
    dtypes['CAREGIVERS'] = {'ROW_ID': int,
                            'CGID': float,
                            'LABEL': str,
                            'DESCRIPTION': str,
                            }
    dtypes['CHARTEVENTS'] = {'ROW_ID': int,
                             'SUBJECT_ID': float,
                             'HADM_ID': float,
                             'ICUSTAY_ID': float,
                             'ITEMID': float,
                             'CHARTTIME': str,
                             'STORETIME': str,
                             'CGID': float,
                             'VALUE': str,
                             'VALUENUM': float,
                             'VALUEUOM': str,
                             'WARNING': float,
                             'ERROR': float,
                             'RESULTSTATUS': str,
                             'STOPPED': str,
                             }
    dtypes['CPTEVENTS'] = {'ROW_ID': float,
                           'SUBJECT_ID': float,
                           'HADM_ID': float,
                           'COSTCENTER': str,
                           'CHARTDATE': str,
                           'CPT_CD': str,
                           'CPT_NUMBER': float,
                           'CPT_SUFFIX': str,
                           'TICKET_ID_SEQ': float,
                           'SECTIONHEADER': str,
                           'SUBSECTIONHEADER': str,
                           'DESCRIPTION': str,
                           }
    dtypes['DATETIMEEVENTS'] = {'ROW_ID': int,
                                'SUBJECT_ID': float,
                                'HADM_ID': float,
                                'ICUSTAY_ID': float,
                                'ITEMID': float,
                                'CHARTTIME': str,
                                'STORETIME': str,
                                'CGID': float,
                                'VALUE': str,
                                'VALUEUOM': str,
                                'WARNING': float,
                                'ERROR': float,
                                'RESULTSTATUS': str,
                                'STOPPED': str,
                                }
    dtypes['DIAGNOSES_ICD'] = {'ROW_ID': int,
                               'SUBJECT_ID': int,
                               'HADM_ID': float,
                               'SEQ_NUM': float,
                               'ICD9_CODE': str,
                               }
    dtypes['DRGCODES'] = {'ROW_ID': int,
                          'SUBJECT_ID': float,
                          'HADM_ID': float,
                          'DRG_TYPE': str,
                          'DRG_CODE': str,
                          'DESCRIPTION': str,
                          'DRG_SEVERITY': float,
                          'DRG_MORTALITY': float,
                          }
    dtypes['D_CPT'] = {'ROW_ID': int,
                       'CATEGORY': float,
                       'SECTIONRANGE': str,
                       'SECTIONHEADER': str,
                       'SUBSECTIONRANGE': str,
                       'SUBSECTIONHEADER': str,
                       'CODESUFFIX': str,
                       'MINCODEINSUBSECTION': float,
                       'MAXCODEINSUBSECTION': float,
                       }
    dtypes['D_ICD_DIAGNOSES'] = {'ROW_ID': int,
                                 'ICD9_CODE': str,
                                 'SHORT_TITLE': str,
                                 'LONG_TITLE': str,
                                 }
    dtypes['D_ICD_PROCEDURES'] = {'ROW_ID': int,
                                  'ICD9_CODE': str,
                                  'SHORT_TITLE': str,
                                  'LONG_TITLE': str,
                                  }
    dtypes['D_ITEMS'] = {'ROW_ID': int,
                         'ITEMID': float,
                         'LABEL': str,
                         'ABBREVIATION': str,
                         'DBSOURCE': str,
                         'LINKSTO': str,
                         'CATEGORY': str,
                         'UNITNAME': str,
                         'PARAM_TYPE': str,
                         'CONCEPTID': float,
                         }
    dtypes['D_LABITEMS'] = {'ROW_ID': int,
                            'ITEMID': float,
                            'LABEL': str,
                            'FLUID': str,
                            'CATEGORY': str,
                            'LOINC_CODE': str,
                            }
    dtypes['ICUSTAYS'] = {'ROW_ID': int,
                          'SUBJECT_ID': float,
                          'HADM_ID': float,
                          'ICUSTAY_ID': float,
                          'DBSOURCE': str,
                          'FIRST_CAREUNIT': str,
                          'LAST_CAREUNIT': str,
                          'FIRST_WARDID': float,
                          'LAST_WARDID': float,
                          'INTIME': str,
                          'OUTTIME': str,
                          'LOS': float,
                          }
    dtypes['INPUTEVENTS_CV'] = {'ROW_ID': int,
                                'SUBJECT_ID': float,
                                'HADM_ID': float,
                                'ICUSTAY_ID': float,
                                'CHARTTIME': str,
                                'ITEMID': float,
                                'AMOUNT': float,
                                'AMOUNTUOM': str,
                                'RATE': float,
                                'RATEUOM': str,
                                'STORETIME': str,
                                'CGID': float,
                                'ORDERID': float,
                                'LINKORDERID': float,
                                'STOPPED': str,
                                'NEWBOTTLE': float,
                                'ORIGINALAMOUNT': float,
                                'ORIGINALAMOUNTUOM': str,
                                'ORIGINALROUTE': str,
                                'ORIGINALRATE': float,
                                'ORIGINALRATEUOM': str,
                                'ORIGINALSITE': str,
                                }
    dtypes['INPUTEVENTS_MV'] = {'ROW_ID': int,
                                'SUBJECT_ID': float,
                                'HADM_ID': float,
                                'ICUSTAY_ID': float,
                                'STARTTIME': str,
                                'ENDTIME': str,
                                'ITEMID': float,
                                'AMOUNT': float,
                                'AMOUNTUOM': str,
                                'RATE': float,
                                'RATEUOM': str,
                                'STORETIME': str,
                                'CGID': float,
                                'ORDERID': float,
                                'LINKORDERID': float,
                                'ORDERCATEGORYNAME': str,
                                'SECONDARYORDERCATEGORYNAME': str,
                                'ORDERCOMPONENTTYPEDESCRIPTION': str,
                                'ORDERCATEGORYDESCRIPTION': str,
                                'PATIENTWEIGHT': float,
                                'TOTALAMOUNT': float,
                                'TOTALAMOUNTUOM': str,
                                'ISOPENBAG': float,
                                'CONTINUEINNEXTDEPT': float,
                                'CANCELREASON': float,
                                'STATUSDESCRIPTION': str,
                                'COMMENTS_STATUS': str,
                                'COMMENTS_TITLE': str,
                                'COMMENTS_DATE': str,
                                'ORIGINALAMOUNT': float,
                                'ORIGINALRATE': float,
                                }
    dtypes['LABEVENTS'] = {'ROW_ID': int,
                           'SUBJECT_ID': float,
                           'HADM_ID': float,
                           'ITEMID': float,
                           'CHARTTIME': str,
                           'VALUE': str,
                           'VALUENUM': float,
                           'VALUEUOM': str,
                           'FLAG': str,
                           }
    dtypes['MICROBIOLOGYEVENTS'] = {'ROW_ID': int,
                                    'SUBJECT_ID': float,
                                    'HADM_ID': float,
                                    'CHARTDATE': str,
                                    'CHARTTIME': str,
                                    'SPEC_ITEMID': float,
                                    'SPEC_TYPE_CD': str,
                                    'SPEC_TYPE_DESC': str,
                                    'ORG_ITEMID': float,
                                    'ORG_CD': float,
                                    'ORG_NAME': str,
                                    'ISOLATE_NUM': float,
                                    'AB_ITEMID': float,
                                    'AB_CD': float,
                                    'AB_NAME': str,
                                    'DILUTION_TEXT': str,
                                    'DILUTION_COMPARISON': str,
                                    'DILUTION_VALUE': float,
                                    'INTERPRETATION': str,
                                    }
    dtypes['NOTEEVENTS'] = {'ROW_ID': int,
                            'SUBJECT_ID': float,
                            'HADM_ID': float,
                            'CHARTDATE': str,
                            'CATEGORY': str,
                            'DESCRIPTION': str,
                            'CGID': float,
                            'ISERROR': str,
                            'TEXT': str,
                            }
    dtypes['OUTPUTEVENTS'] = {'ROW_ID': int,
                              'SUBJECT_ID': float,
                              'HADM_ID': float,
                              'ICUSTAY_ID': float,
                              'CHARTTIME': str,
                              'ITEMID': float,
                              'VALUE': float,
                              'VALUEUOM': str,
                              'STORETIME': str,
                              'CGID': float,
                              'STOPPED': str,
                              'NEWBOTTLE': float,
                              'ISERROR': float,
                              }
    dtypes['PATIENTS'] = {'ROW_ID': int,
                          'SUBJECT_ID': int,
                          'GENDER': str,
                          'DOB': str,
                          'DOD': str,
                          'DOD_HOSP': str,
                          'DOD_SSN': str,
                          'EXPIRE_FLAG': str,
                          }
    dtypes['PRESCRIPTIONS'] = {'ROW_ID': int,
                               'SUBJECT_ID': float,
                               'HADM_ID': float,
                               'ICUSTAY_ID': float,
                               'STARTTIME': str,
                               'ENDTIME': str,
                               'DRUG_TYPE': str,
                               'DRUG': str,
                               'DRUG_NAME_POE': str,
                               'DRUG_NAME_GENERIC': str,
                               'FORMULARY_DRUG_CD': str,
                               'GSN': str,
                               'NDC': str,
                               'PROD_STRENGTH': str,
                               'DOSE_VAL_RX': str,
                               'DOSE_UNIT_RX': str,
                               'FORM_VAL_DISP': str,
                               'FORM_UNIT_DISP': str,
                               'ROUTE': str,
                               }
    dtypes['PROCEDUREEVENTS_MV'] = {'ROW_ID': int,
                                    'SUBJECT_ID': float,
                                    'HADM_ID': float,
                                    'ICUSTAY_ID': float,
                                    'STARTTIME': str,
                                    'ENDTIME': str,
                                    'ITEMID': float,
                                    'VALUE': float,
                                    'VALUEUOM': str,
                                    'LOCATION': str,
                                    'LOCATIONCATEGORY': str,
                                    'STORETIME': str,
                                    'CGID': float,
                                    'ORDERID': float,
                                    'LINKORDERID': float,
                                    'ORDERCATEGORYNAME': str,
                                    'SECONDARYORDERCATEGORYNAME': str,
                                    'ORDERCATEGORYDESCRIPTION': str,
                                    'ISOPENBAG': float,
                                    'CONTINUEINNEXTDEPT': float,
                                    'CANCELREASON': float,
                                    'STATUSDESCRIPTION': str,
                                    'COMMENTS_EDITEDBY': str,
                                    'COMMENTS_CANCELEDBY': str,
                                    'COMMENTS_DATE': str,
                                    }
    dtypes['PROCEDURES_ICD'] = {'ROW_ID': int,
                                'SUBJECT_ID': float,
                                'HADM_ID': float,
                                'SEQ_NUM': float,
                                'ICD9_CODE': str,
                                }
    dtypes['SERVICES'] = {'ROW_ID': int,
                          'SUBJECT_ID': float,
                          'HADM_ID': float,
                          'TRANSFERTIME': str,
                          'PREV_SERVICE': str,
                          'CURR_SERVICE': str,
                          }
    dtypes['TRANSFERS'] = {'ROW_ID': int,
                           'SUBJECT_ID': int,
                           'HADM_ID': float,
                           'ICUSTAY_ID': float,
                           'DBSOURCE': str,
                           'EVENTTYPE': str,
                           'PREV_CAREUNIT': str,
                           'CURR_CAREUNIT': str,
                           'PREV_WARDID': str,
                           'CURR_WARDID': str,
                           'INTIME': str,
                           'OUTTIME': str,
                           'LOS': float,
                           }
    return dtypes











# TODO: Clean up this part of the MIMIC_Pandas code
if __name__ == '__main__':
    '''This is an example showing how you can load the MIMIC csv files
       into a dictionary of pandas dataframs'''

    # Set this variable to the folder where the .gz files are located
    # On a Windows machine, be sure to use \\ instead of just \ in the file path.
    Location_of_the_CSV_Files = "D:\\MIMIC-III Clinical Database\\Data\\"

    # Comment out any files you don't need for your analysis.
    # I was able to load all the files to memory on a VM that had 64GB of RAM.
    # Loading all the files from their compressed state took over 30 minutes.
    List_of_files_you_want_to_load = [
        ########## one # means it has been tested and works, ## means I haven't tested it yet
        'ADMISSIONS',  # 12 MB
        'CALLOUT',  # 6.1 MB
        'CAREGIVERS',  # 199 KB
        #                    'CHARTEVENTS', # 33 GB ------BIG!!!
        'CPTEVENTS',  # 56 MB
        #                    'DATETIMEEVENTS',  # 502 MB
        'DIAGNOSES_ICD',  # 19 MB
        'DRGCODES',  # 11 MB
        'D_CPT',  # 14 KB
        'D_ICD_DIAGNOSES',  # 1.4 KB
        'D_ICD_PROCEDURES',  # 305 KB
        'D_ITEMS',  # 933 KB
        'D_LABITEMS',  # 43 KB
        'ICUSTAYS',  # 6.1 MB
        #                    'INPUTEVENTS_CV', # 2.3 GB ------BIG!!!
        #                    'INPUTEVENTS_MV', # 931 MB  ------BIG!!!
        #                    'LABEVENTS', # 1.8GB ------BIG!!!
        #                    'MICROBIOLOGYEVENTS',  # 70 MB
        #                    'NOTEEVENTS', # 3.8 GB  ------BIG!!!
        'OUTPUTEVENTS',  # 379 MB
        'PATIENTS',  # 2.6 MB
        #                    'PRESCRIPTIONS',  # 735 MB
        'PROCEDUREEVENTS_MV',  # 47 MB
        'PROCEDURES_ICD',  # 6.5 MB
        'SERVICES',  # 3.4 MB
        'TRANSFERS',  # 24 MB
    ]

    df = load_mimic_to_pandas(CSV_Folder_Location=Location_of_the_CSV_Files, CSV_List=List_of_files_you_want_to_load, gunzip=True)

    # The output is a dictionary where the file names above are the keys and the values are a
    # pandas dataframe containing the data from the file.
    # So you can view the first few lines of a file using code like this:
    print(df['ADMISSIONS'].head())




