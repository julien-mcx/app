import streamlit as st 
import naas_drivers
from naas_drivers import gsheet

SPREADSHEET_URL = "https://docs.google.com//spreadsheets//d//1yQCZqRweD7FLCAEFZagH00WmSQ1Pb8iVWTTnC6X3jLM//edit#gid=452671349"
SHEET_NAME = "FuturesForwards"
df = gsheet.connect(SPREADSHEET_URL)#.get(sheet_name=SHEET_NAME)
st.write(df)
