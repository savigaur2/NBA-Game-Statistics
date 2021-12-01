import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector
cnx = mysql.connector.connect(**st.secrets["mysql"])

def run_query(query):
    with cnx.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

def app ():
    st.title('NBA')

    col1, col2, col3 , col4, col5 = st.columns(5)

    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col3 :
        st.write('Team Statistics')


    # Intial Page
    select_team = run_query("SELECT * FROM TEAM")
    team_df = pd.DataFrame(data = select_team, columns = ['Team Name', 'Wins', 'Losses',
                                                'City', 'Conference',
                                                'RPG', 'PPG', 'APG', 'SPG', 'TPG'])
    team_df.index = np.arange(1, len(team_df) + 1)
    st.dataframe(data = team_df.style.format({'RPG': '{:.1f}',
                                              'PPG': '{:.1f}',
                                              'APG': '{:.1f}',
                                              'SPG': '{:.1f}',
                                              'TPG': '{:.1f}'}))
