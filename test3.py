import streamlit as st 
# import naas_drivers
# from naas_drivers import gsheet

# SPREADSHEET_URL = "https://docs.google.com//spreadsheets//d//1yQCZqRweD7FLCAEFZagH00WmSQ1Pb8iVWTTnC6X3jLM//edit#gid=452671349"
# SHEET_NAME = "FuturesForwards"
# df = gsheet.connect(SPREADSHEET_URL)#.get(sheet_name=SHEET_NAME)
# st.write(df)

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Connect to Google Sheets
scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("streamlit1202-240ada1c5101.json", scope)
client = gspread.authorize(credentials)

# client.open("QuestionsFinancedeMarché").sheet1
Sheet = client.open_by_key("1HMZGbomaWzYrg3V0Hx3sRvmL6g3EFOMRac_ZbrRC32Y").sheet1
st.write(Sheet.shape[0])

sheet = client.create("NewDatabase")
st.write(sheet)

gc = authenticate_google_docs()
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1yQCZqRweD7FLCAEFZagH00WmSQ1Pb8iVWTTnC6X3jLM/edit#gid=452671349') # Open by URL
worksheet = sh.get_worksheet(0) # Select worksheet by index


