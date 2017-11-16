# Spiro Ganas
# 11/16/17
#
# This script one-hot encodes the ICD9 data and then applies a Pincipal Components Analysis



import pandas as pd
from sklearn.decomposition import PCA

from MIMIC3py.ICD9_One_Hot_Encoded import ICD9_One_HotEncoded



def ICD9_PCA(numer_of_components = 100, print_details = True, save_as_csv_filename = None):
    """Applies a principal components analysis to the MIMIC III ICD9 Data."""

    # Convert the MIMIC III ICD9 data to a one-hot encoded matrix using the function I created.
    ICD9_data = ICD9_One_HotEncoded()

    # Set up the PCA model
    MyPCA = PCA(n_components=numer_of_components, svd_solver='randomized')

    # trains the PCA using all of the one-hot encoded data
    MyPCA.fit(ICD9_data)

    # Convert the output of the model to a pandas Dataframe
    MyPCA_df = pd.DataFrame(MyPCA.components_)

    # Add column names to the DataFrame
    MyPCA_df.columns = list(ICD9_data.axes[1])



    # Transpose the data to make it easy to sort in microsoft excel
    MyResults = MyPCA_df.transpose()

    # Export the results to a csv file
    if save_as_csv_filename:
        MyResults.to_csv(save_as_csv_filename)
        #MyResults.to_csv("D:\\MIMIC-III Clinical Database\\Data\\output\\PCA_Analysis.csv")

    if print_details:
        #print(MyPCA.n_components_)
        print(MyPCA.explained_variance_ratio_)
        print("Total Variance Captured: ", sum(MyPCA.explained_variance_ratio_))


    return MyResults


if __name__ == "__main__":
    df = ICD9_PCA(numer_of_components = 100, print_details = True, save_as_csv_filename = None)