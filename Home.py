"""Home page — the entry point of the World Cities app.

This is a Streamlit **multipage** app:

    my-streamlit/
    ├── Home.py          <- this file: the main entry point
    ├── pages/
    │   └── app.py       <- the World Cities explorer from the Data App Tutorial
    └── worldcities.csv

Streamlit shows every file in ``pages/`` in the sidebar automatically, so the app page is
reachable from the sidebar as well as from the button below.

Run it from this folder with:

    uv run streamlit run Home.py
"""

import streamlit as st

st.set_page_config(page_title='World Cities', page_icon='🌍')

st.title('World Cities 🌍')

st.markdown("""
Welcome! This app explores **worldcities.csv** — a dataset of the world's major cities,
where every city has a population over one million.

On the **app** page you can:

- filter cities by **population** with a slider,
- choose which kinds of **capital** to keep (primary, admin, minor, or not a capital),
- narrow the map down to a single **country**,
- and see the matching cities on a **map**, in a **table**, and in a **bar chart** of total
  population by country.
""")

st.divider()

if st.button('🌍 Open the World Cities explorer', type='primary'):
    st.switch_page('pages/app.py')

st.caption('BANA409 — Data App Tutorial. Built with Streamlit, pandas and matplotlib.')
