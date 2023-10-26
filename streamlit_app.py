import streamlit as st

def main():
    st.sidebar.title("Theme Demo")
    theme = st.sidebar.radio("Select Theme", ("Light", "Dark"))
    
    if theme == "Light":
        st.set_theme("light")
    elif theme == "Dark":
        st.set_theme("dark")
    
    st.title("Streamlit Theme Demo")
    st.write(f"Selected Theme: {theme}")

if __name__ == "__main__":
    main()
