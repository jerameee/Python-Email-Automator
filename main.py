from datetime import datetime # core python module
import pandas as pd # pip install pandas
from send_email import send_email # Local python module

# Public Google Sheets URL - not secure!
SHEET_ID = "1yGP2uU9lHoV1yI_Yg3oM_aBaOUASf6nw-iC7W_KjHg"
SHEET_NAME = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

def load_df(url):
    parse_dates = ["due_date", "reminder_date"]
    df = pd.read_csv(url, parse_dates=parse_dates)
    return df


print(load_df(URL))