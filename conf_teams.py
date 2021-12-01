import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector

def init_connection():
    return mysql.connector.connect(user = st.secrets['user'], database = st.secrets['database'], password = st.secrets['password'])

conn = init_connection()

# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

def app():
    st.title('Conference Teams')

    st.header('Eastern Conference')
    east = run_query('SELECT * FROM Team WHERE Conference = "East"')
    east_df = pd.DataFrame(data = east, columns = ['Team Name', 'Wins', 'Losses',
                                                'City', 'Conference',
                                                'RPG', 'PPG', 'APG', 'SPG', 'TPG'])
    east_df.index = np.arange(1, len(east_df) + 1)
    st.dataframe(data = east_df.style.format({'RPG': '{:.1f}',
                                              'PPG': '{:.1f}',
                                              'APG': '{:.1f}',
                                              'SPG': '{:.1f}',
                                              'TPG': '{:.1f}'}))

    st.header('Western Conference')
    west = run_query('SELECT * FROM Team WHERE Conference = "West"')
    west_df = pd.DataFrame(data = west, columns = ['Team Name', 'Wins', 'Losses',
                                                'City', 'Conference',
                                                'RPG', 'PPG', 'APG', 'SPG', 'TPG'])
    west_df.index = np.arange(1, len(west_df) + 1)
    st.dataframe(data = west_df.style.format({'RPG': '{:.1f}',
                                              'PPG': '{:.1f}',
                                              'APG': '{:.1f}',
                                              'SPG': '{:.1f}',
                                              'TPG': '{:.1f}'}))
