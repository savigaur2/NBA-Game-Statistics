import initial_view
import head_to_head
import conf_teams
import sing_teams
import admin_page
import streamlit as st

PAGES = {
    'Home': initial_view,
    'Head to Head Search': head_to_head,
    'Conference Teams': conf_teams,
    'Singluar Teams': sing_teams,
    'Admin Login': admin_page
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio('Go to', list(PAGES.keys()))
page = PAGES[selection]
page.app()
