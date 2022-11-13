import streamlit as st
import pandas as pd
import numpy as np

from scipy import spatial
from datetime import datetime
import csv
from datetime import timedelta

st.title("Marathon Time Predicter")


@st.cache
def load_data(num_user_times):
    rows = []

    actual_times = {}
    t = 0
    with open("marathon_results_2017.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):

            lal = line[0].split(",")

            formatted = [lal[11], lal[12], lal[13], lal[14], lal[16], lal[17], lal[18], lal[19]]

            if "-" in formatted or "" in formatted:
                continue

            times = []

            if t != 0:
                a = datetime.strptime(lal[11], '%H:%M:%S')
                _5k = a.second + a.minute * 60 + a.hour * 3600

                a = datetime.strptime(lal[12], '%H:%M:%S')
                _10k = a.second + a.minute * 60 + a.hour * 3600

                a = datetime.strptime(lal[13], '%H:%M:%S')
                _15k = a.second + a.minute * 60 + a.hour * 3600

                a = datetime.strptime(lal[14], '%H:%M:%S')
                _20k = a.second + a.minute * 60 + a.hour * 3600

                # lal[15] is half

                a = datetime.strptime(lal[16], '%H:%M:%S')
                _25k = a.second + a.minute * 60 + a.hour * 3600

                a = datetime.strptime(lal[17], '%H:%M:%S')
                _30k = a.second + a.minute * 60 + a.hour * 3600

                a = datetime.strptime(lal[18], '%H:%M:%S')
                _35k = a.second + a.minute * 60 + a.hour * 3600

                a = datetime.strptime(lal[19], '%H:%M:%S')
                _40k = a.second + a.minute * 60 + a.hour * 3600

                a = datetime.strptime(lal[22], '%H:%M:%S')
                actual_time = a.second + a.minute * 60 + a.hour * 3600

                row = [_5k, _10k, _15k, _20k, _25k, _30k, _35k, _40k]

                row = row[0:num_user_times]
                str_row = str(row)
                actual_times[str_row] = actual_time

                rows.append(row)

            # don't do the whole thing (for test)
            # if t > 11:
            #     break
            t += 1
    return (rows, actual_times)

data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(3)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

st.markdown(
    """<style>
        input {
            font-size: 3em !important;
            color: red;
        }
        
        label {
        font-size: 1em !important;
        
        </style>""",
    unsafe_allow_html=True,
)


with st.form("my_form"):
   st.write("Enter your splits")
   _5k_split = st.text_input("5K Split (hours:minutes:seconds)", value="00:00:00")
   _10k_split = st.text_input("10K Split (hours:minutes:seconds)", value="00:00:00")
   _15k_split = st.text_input("15K Split (hours:minutes:seconds)", value="00:00:00")
   _20k_split = st.text_input("20K Split (hours:minutes:seconds)", value="00:00:00")
   _25k_split = st.text_input("25K Split (hours:minutes:seconds)", value="00:00:00")
   _30k_split = st.text_input("30K Split (hours:minutes:seconds)", value="00:00:00")
   _35k_split = st.text_input("35K Split (hours:minutes:seconds)", value="00:00:00")
   _40k_split = st.text_input("40K Split (hours:minutes:seconds)", value="00:00:00")



   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       results = [_5k_split, _10k_split, _15k_split, _20k_split, _25k_split, _30k_split, _35k_split, _40k_split]
       user_times = []

       if _5k_split != "00:00:00" and _5k_split != "":
           a = datetime.strptime(_5k_split, '%H:%M:%S')
           _5k_split = a.second + a.minute * 60 + a.hour * 3600
           user_times.append(int(_5k_split))
       if _10k_split != "00:00:00" and _10k_split != "":
           a = datetime.strptime(_10k_split, '%H:%M:%S')
           _10k_split = a.second + a.minute * 60 + a.hour * 3600
           user_times.append(int(_10k_split))
       if _15k_split != "00:00:00" and _15k_split != "":
           a = datetime.strptime(_15k_split, '%H:%M:%S')
           _15k_split = a.second + a.minute * 60 + a.hour * 3600
           user_times.append(int(_15k_split))
       if _20k_split != "00:00:00" and _20k_split != "":
           a = datetime.strptime(_20k_split, '%H:%M:%S')
           _20k_split = a.second + a.minute * 60 + a.hour * 3600
           user_times.append(int(_20k_split))
       if _25k_split != "00:00:00" and _25k_split != "":
           a = datetime.strptime(_25k_split, '%H:%M:%S')
           _25k_split = a.second + a.minute * 60 + a.hour * 3600
           user_times.append(int(_25k_split))
       if _30k_split != "00:00:00" and _30k_split != "":
           a = datetime.strptime(_30k_split, '%H:%M:%S')
           _30k_split = a.second + a.minute * 60 + a.hour * 3600
           user_times.append(int(_30k_split))
       if _35k_split != "00:00:00" and _35k_split != "":
           a = datetime.strptime(_35k_split, '%H:%M:%S')
           _35k_split = a.second + a.minute * 60 + a.hour * 3600
           user_times.append(int(_35k_split))
       if _40k_split != "00:00:00" and _40k_split != "":
           a = datetime.strptime(_40k_split, '%H:%M:%S')
           _40k_split = a.second + a.minute * 60 + a.hour * 3600
           user_times.append(int(_40k_split))

       num_user_times = len(user_times)
       if num_user_times == 0:
           st.write("No times inputted - please try again!")
       else:
           data_load_state = st.text('Running simulation...')
           # Load 10,000 rows of data into the dataframe.
           # Notify the reader that the data was successfully loaded.
           rows_actual_times_tuple = load_data(num_user_times)
           rows = rows_actual_times_tuple[0]
           actual_times = rows_actual_times_tuple[1]

           tree = spatial.KDTree(rows)
           data_load_state.text('')

           final_result = int(str(actual_times[str(rows[tree.query(user_times)[1]])]))

           user_text = st.header("Your predicted time is: " + str(timedelta(seconds=final_result)) + "!")



       # st.write(_5k_split, type(_5k_split), _10k_split, type(_10k_split), _10k_split=="")