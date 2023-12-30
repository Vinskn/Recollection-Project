import pandas as pd

file_path = 'Database.csv'
fcsv = pd.read_csv(file_path)

def login (nama, pswd):
    for i, row in fcsv.iterrows():
        if row ['User'] == nama and row['Pswd'] == pswd:
            return i
    return -1


def signup (nama, pswd, email):
    user_baru = nama
    pass_baru = pswd
    nama_email = email

    fcsv.loc[len(fcsv)] = [user_baru, pass_baru, nama_email]
    fcsv.to_csv(file_path, index=False)
