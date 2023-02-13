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

# # Connect to Google Sheets
# scope = ['https://www.googleapis.com/auth/spreadsheets',
#          "https://www.googleapis.com/auth/drive"]

# credentials = ServiceAccountCredentials.from_json_keyfile_name("streamlit1202-240ada1c5101.json", scope)
# client = gspread.authorize(credentials)

{
  "type": "service_account",
  "project_id": "streamlit1202",
  "private_key_id": "240ada1c5101212633493cb72fb206e958b37f87",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCyHUcDaHQ7Isdp\n/mGd8bX/3/8ROJAkQG+/mpdA372J3PGDNHwpRdpbYVf9C9TSOKoGpCYMZDp1gHNn\nsCE7XdGpNpBVht/HqxyN0xgx09HytqSz14fmLfhL9w3zhkN+2PJu1aVkPUirEzrN\nAIcfRaYvrHIsn93UJAj272dRcdw/jm5E9crG2J1WxxThjc4TXu80/ijarMYgDL6A\nhKGaXWD+JKRKvlAQNOhBoWbUonZbnaKn96G/LC5+KEC8tIzk7j/gl1ca8kIHvhzS\nFFLbp9kOKVCiJpvFgSdxMS9Cjxl523btYu28tLayMHabm4hBzFUxWujRUUkjqR7J\ntsOt2HtvAgMBAAECggEAA8GGS9YaDV0wY1XP7Sq5scmhcVWGBJ2vPZUe92lAb/XO\nyfuDWsN0VVT6LAXh2QUE4Nr5Sm2apfutc1RNfxj9YNobtRIBCg7brUn0Sqiy1rFv\nS7OR1BLIF6IAE1CTf8tHYXrz3+dC7wiaxtPqBYjMdljml3ZPkTepULu/rAIAqP5o\n2gQARg3J/iDdsx8BYR9yjODzwEo8GjGRr8wEQvj8xjRIYZ5f5D0nllCmX7Q+pkY/\nbXCW2uLGwlCsBeTOUADXOHLeO1MpX0MZbMI5NEmIE4Nzk5Y2TFB39iv1Bf2GiK1j\nzf9bFERALPsBDq6V1cPA5Uehv9J1L9GJMBjqc+YLoQKBgQDtx2/3GJAi822gsf6b\nZVnL9/uQXaZizqti7cl+LBPl/eznRIAh8oJIGN2EZdQAINonEIJATTCwA59TlggD\nuo/xqideWJT3mBLjyFfRdbtgCMRkrtsKLQrLKHOMf6wciyTNUxeJfV5XSonlK9wC\nyj+NeU4JVsDWcZTkWzM7GN8naQKBgQC/w2KT8s9SwyTgvPOBMn90rtbDO9LRpA7D\nbKB0AvzWqJbXt4/Go53pPdamuGq85QRfH2uxkMzhMaf73YlNXmRgf2ex9lf5l/as\nSGmGfX98KWsElH35miw2v08DGF2E3DQqRZxTpVfFzJKOKQ2YqsCGUs/si/A2/1/9\nXu89mDdJFwKBgQDZvZ5MWlPzjZNAan7K8p6uZ6IYa4noRXUwnKu9PMPkAwmkJlhn\nvdmMCCkiCtV+YJck2rtMAuOo60hFlMg2Eeuq07RFczzHFp2FtXqltvglUyH1SSIQ\nSXru21YkvO1xHgJPe9276/AuY3WvROCuNWLJPOI3Lxhbx5sfGlzpqzb+sQKBgGYL\nmFq4vGEDXY2Gn2IiODckjz6niCFtVznhhWUW7ethHZw/n3AKQ48KDD7+JjbM/E2O\nT+XW81/m58ic9GLKl0nOoqTOPbShjG/TvOwHvp6Y/80ZJAx+YYbkuSwhfCqmb9AK\n6QyOES4+FcM2z3htbTRNvz3Wngb2UONo8JDrfogTAoGABPxVGoVrHE6RMqk1U9zS\njoeqiPOc9H+HDxAsAgXu17eJ+Lf6NCmKfDVqHFa6YRCmsGcmhypSx8vgdhdB7JcV\nJiG57C0ofsUTxL50FhvuIIy/a/zMXTwhKz9vytYDtkBL4wDzcDts5wonPcdv+FTG\nAa0zJ/Ly++y4SkLVNKKZ+pI=\n-----END PRIVATE KEY-----\n",
  "client_email": "streamlit1202@streamlit1202.iam.gserviceaccount.com",
  "client_id": "104100431381175034062",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/streamlit1202%40streamlit1202.iam.gserviceaccount.com"
}

gc = gspread.service_account_from_dict(credentials)

sh = gc.open("QuestionsFinancedeMarché")

print(sh.sheet1.get('A1'))
