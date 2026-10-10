import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")

st.title("World Cities")
st.markdown(
    """
    Welcome to the World Cities app — an interactive Streamlit multipage application.

    Use the button below to open the main app page (app.py) located in the `pages/` folder.
    """
)

st.write("---")

if st.button("Go to App"):
    # Try to navigate to the page by setting the page query param and rerunning.
    # Streamlit's multipage system recognizes a `page` query parameter like `/?page=app`.
    # This will typically switch to the page named `app` (the filename without `.py`).
    st.experimental_set_query_params(page="app")
    st.experimental_rerun()

st.markdown("Or open the app page directly: [Open app page](/?page=app)")
