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
    st.markdown(
        """
        <style>
        body {
            color: black;
            background-color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def dark_theme():
    st.markdown(
        """
        <style>
        body {
            color: white;
            background-color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
