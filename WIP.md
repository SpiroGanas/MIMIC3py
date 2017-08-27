# Work-in-Progress MIMIC3py

### Data Engineering
1.  Add a function to check if the user has entered a valid username and password.  I need to add some error handling to talke care of bad values.
2.  Add a wrapper to the download function so it can be easily used from the command line
3.  Finish the function to load the data into Pandas data frames.  Maybe store all the dataframes in a class or fictionary?
4.  Add code to create a MySQL database and load all the data.
5.  



### Analysis
1.  Create a sparse matrix storing the ICD codes for each admission ID.  Figure out how to "One-Hot Encode" it for predictive modeling purposes.
2.  Try using PCA or Tensor Factorization to identify major disease groups.
