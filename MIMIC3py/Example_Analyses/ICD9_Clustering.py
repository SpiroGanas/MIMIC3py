# Spiro Ganas
# 11/18/17
#
# This script one-hot encodes the ICD9 data and then applies a k-means clustering analysis



import pandas as pd
from sklearn.cluster import KMeans

from MIMIC3py.ICD9_One_Hot_Encoded import ICD9_One_HotEncoded



def ICD9_KMeanse(n_clusters = 100, print_details = True, save_as_csv_filename = None):
    """Applies a principal components analysis to the MIMIC III ICD9 Data."""

    # Convert the MIMIC III ICD9 data to a one-hot encoded matrix using the function I created.
    ICD9_data = ICD9_One_HotEncoded()

    # Set up the PCA model
    MyKMeans = KMeans(n_clusters =n_clusters)

    # trains the PCA using all of the one-hot encoded data
    MyKMeans.fit(ICD9_data)

    # Convert the output of the model to a pandas Dataframe
    MyKMeans = pd.DataFrame(MyKMeans.cluster_centers_)

    # Add column names to the DataFrame
    MyKMeans.columns = list(ICD9_data.axes[1])



    # Transpose the data to make it easy to sort in microsoft excel
    MyResults = MyKMeans.transpose()

    # Export the results to a csv file
    if save_as_csv_filename:
        MyResults.to_csv(save_as_csv_filename)
        #MyResults.to_csv("D:\\MIMIC-III Clinical Database\\Data\\output\\MyKMeans_Analysis.csv")

 #   if print_details:
        #print(MyPCA.n_components_)
 #       print(MyKMeans.explained_variance_ratio_)
 #       print("Total Variance Captured: ", sum(MyKMeans.explained_variance_ratio_))


    return MyResults


if __name__ == "__main__":
    df = ICD9_KMeanse(n_clusters = 25, print_details = True, save_as_csv_filename = None)
    print(df)