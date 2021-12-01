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
    st.title('Singular Teams')

    st.header('Enter Team Name')
    team = st.text_input(label = 'Team', value = '')

    if st.button(label = 'Search'):
        st.write('Team Stats')
        team_data = run_query('SELECT * FROM Team WHERE TeamName = ' + "'" + team + "'")
        team_data_df = pd.DataFrame(data = team_data, columns = ['Team Name', 'Wins', 'Losses',
                                                    'City', 'Conference',
                                                    'RPG', 'PPG', 'APG', 'SPG', 'TPG'])
        team_data_df.index = np.arange(1, len(team_data_df) + 1)
        st.dataframe(data = team_data_df.style.format({'RPG': '{:.1f}',
                                                  'PPG': '{:.1f}',
                                                  'APG': '{:.1f}',
                                                  'SPG': '{:.1f}',
                                                  'TPG': '{:.1f}'}))

        st.write('Games')
        game_data = run_query('SELECT * FROM Game WHERE (' + "'" + team + "'" + ' IN (SELECT HomeTeam FROM Team) OR ' + "'" + team + "'" + ' IN (SELECT AwayTeam FROM Team))')
        game_data_df = pd.DataFrame(data = game_data, columns = ['Game ID', 'Home', 'Away',
                                                         'Date', 'Result', 'Score',
                                                         'REB', 'AST', 'PTS', 'TO'])
        game_data_df.index = np.arange(1, len(game_data_df) + 1)
        st.dataframe(data = game_data_df)
