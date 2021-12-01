import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector

@st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)

def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

def app():
    st.title('Head to Head Search')

    st.header('Enter Team Names')
    team_1 = st.text_input(label = 'Team 1', value = '')
    team_2 = st.text_input(label = 'Team 2', value = '')

    if st.button(label = 'Search'):
        st.write('Games Played Between ' + team_1 + ' and ' + team_2)
        games = run_query('SELECT * FROM Game WHERE ((' + "'" + team_1 + "'" + ' IN (SELECT HomeTeam FROM Team) OR ' + "'" + team_1 + "'" + ' IN (SELECT AwayTeam from Team)) AND (' + "'" + team_2 + "'" + ' IN (SELECT HomeTeam FROM Team) OR ' + "'" + team_2 + "'" + ' IN (SELECT AwayTeam FROM Team)))')
        games_df = pd.DataFrame(data = games, columns = ['Game ID', 'Home', 'Away',
                                                         'Date', 'Result', 'Score',
                                                         'REB', 'AST', 'PTS', 'TO'])
        games_df.index = np.arange(1, len(games_df) + 1)
        st.dataframe(data = games_df)
