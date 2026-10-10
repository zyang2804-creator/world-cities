# World Cities 🌍

A Streamlit **multipage** app that explores `worldcities.csv` — every city in the dataset has a
population over one million.

Built for the BANA409 *Data App Tutorial*.

## Structure

```
my-streamlit/
├── Home.py            # the main entry point: title, welcome text, button to the app
├── pages/
│   └── app.py         # the World Cities explorer (the tutorial's app-cities.py)
├── worldcities.csv    # 723 cities, population in millions
├── pyproject.toml
└── uv.lock
```

Streamlit turns every file inside `pages/` into a page listed in the sidebar, so `pages/app.py`
is reachable both from the sidebar and from the button on Home.

> The tutorial builds the app as a single file named `app-cities.py`. The project structure
> required here is the multipage one, so that code lives in `pages/app.py` instead — it is the
> same app, unchanged apart from where it is stored.

## Run it locally

```bash
uv run streamlit run Home.py
```

Then open <http://localhost:8501>.

## What the app does

| Widget | Where | Filters on |
|---|---|---|
| `st.slider` | main area | `population >= value` (0–40, default 3.6) |
| `st.multiselect` | sidebar | `capital` (primary / admin / minor / not a capital) |
| `st.text_input` in a `st.form` | sidebar | `country` — type a country name, or `ALL` to reset |

The filtered rows are shown three ways: a world map (`st.map`), a table of city / country /
population, and a bar chart of total population by country.

## Deploy

Publish this folder to a **public** GitHub repository, then create the app on
<https://share.streamlit.io>:

- **Main file path**: `Home.py`
- **Advanced settings → Python version**: `3.14` (Streamlit Cloud defaults to 3.12 and the
  install fails because this project requires 3.14)

No `requirements.txt` is needed — Streamlit Cloud reads `uv.lock` and installs exactly the
packages this project uses.
