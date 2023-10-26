import streamlit as st

def main():
    st.sidebar.title("Theme Demo")
    theme = st.sidebar.radio("Select Theme", ("Light", "Dark"))

    if theme == "Light":
        light_theme()
    elif theme == "Dark":
        dark_theme()

    st.title("Streamlit Theme Demo")
    st.write(f"Selected Theme: {theme}")

def light_theme():
    st.set_page_config(
        page_title="Streamlit Theme Demo",
        page_icon=":sunny:",
        layout="wide",
        initial_sidebar_state="expanded",
        theme="light"
    )

def dark_theme():
    st.set_page_config(
        page_title="Streamlit Theme Demo",
        page_icon=":crescent_moon:",
        layout="wide",
        initial_sidebar_state="expanded",
        theme="dark"
    )

if __name__ == "__main__":
    main()
