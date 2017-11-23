# Spiro Ganas
# 9/6/17
#
# A tkinter GUI that makes it easy to read patient chart notes.






import MIMIC3py.load_to_pandas
from tkinter import *
import tkinter.messagebox
import tkinter.scrolledtext as ScrolledText

Location_of_the_CSV_Files = "D:\\MIMIC-III Clinical Database\\Data\\"
List_of_files_you_want_to_load = [
    'PATIENTS',
    'CAREGIVERS',
    'NOTEEVENTS', ]

df = MIMIC3py.load_to_pandas.load_mimic_to_pandas(CSV_Folder_Location=Location_of_the_CSV_Files,
                                                  CSV_List=List_of_files_you_want_to_load, gunzip=True)

# Create a list of all the Subject IDs.
# This is used to populate the drop-down box
Patient_list = list(df['PATIENTS']['SUBJECT_ID'])

print(df['NOTEEVENTS'].head())


# example of how to get a value at row 0 column 0
# MIMIC3py.my_gui.df['CAREGIVERS'].iat[0,0]


def load_caregiver(self):
    Row = int(PatientModel.get())
    print("Patient ID was: " + str(Row))

    Patient_df = df['PATIENTS'][df['PATIENTS'].SUBJECT_ID == Row].iloc[0]
    print(Patient_df)

    Notes_df = df['NOTEEVENTS'][df['NOTEEVENTS'].SUBJECT_ID == Row].iloc[0]
    print(Notes_df)

    T2.delete(0, END)
    T2.insert(0, Patient_df.DOB)

    T3.delete(0, END)
    T3.insert(0, Patient_df.GENDER)

    T4.delete('1.0', END)
    T4.insert(INSERT, Notes_df.TEXT)





    # # Load the Caregiver ID
    # CGID.delete(0, END)
    # CGID.insert(0, int(df['CAREGIVERS'].at[Row,'CGID']))
    #
    # # Load the Caregiver ID
    # Description.delete(0, END)
    # Description.insert(0, str(df['CAREGIVERS'].at[Row,'DESCRIPTION']))
    #


# Set up the tkinter form
app = Tk()
app.title("MIMIC3 GUI")
app.geometry("900x600")


def shutdown():
    """This function gets called when the program is closed"""
    if tkinter.messagebox.askokcancel(title="Close the Program?", message="Are you sure you want to quit?"):
        app.destroy()


# Set the behavior for when the program is closed
app.protocol("WM_DELETE_WINDOW", shutdown)

# a drop-down box to let the user select a patient ID
L1 = Label(app, text="Select a Patient ID:")
L1.place(x=5, y=5)

# This is the "Model" that will hold the Patient ID data
PatientModel = StringVar()
PatientModel.set(None)

# The * in front of *Patient_list passes the list contents as individual arguments to the function
Patient_ID = OptionMenu(app, PatientModel, *Patient_list, command=load_caregiver)
Patient_ID.place(x=120, y=5)

L2 = Label(app, text="Date of Birth:")
L2.place(x=5, y=30)
T2 = Entry(app)
T2.place(x=120, y=30)

L3 = Label(app, text="Gender:")
L3.place(x=5, y=55)
T3 = Entry(app)
T3.place(x=120, y=55)

L3 = Label(app, text="Gender:")
L3.place(x=5, y=55)
T3 = Entry(app)
T3.place(x=120, y=55)

L4 = Label(app, text="Chart Notes:")
L4.place(x=5, y=75)
# T4 = Text(app)
# T4.place(x=120, y=75)


T4 = ScrolledText.ScrolledText(
    wrap=tkinter.WORD,
    width=85,
    height=25
)
T4.place(x=120, y=75)

# MyButton = Button(app, text="Click Me to load the Patient!", width=50, command=load_caregiver)
# MyButton.place(x=100, y=500)



# app.pack()
app.mainloop()
