import streamlit as st
import bitarray

def create_profile():
    # Get the user's IP address
    ip_address = st.experimental_get_query_params().get("client_ip", [None])[0]

    # Check if the user's IP address already has a profile
    if ip_address and ip_address in profiles:
        st.write("You already have a profile!")

    else:
        # Get the profile name from the user
        profile_name = st.text_input("Enter your profile name")

        # Get the configuration from the user
        configuration = []
        for i in range(8):
            question = st.radio(f"Question {i+1}", ("Yes", "No"))
            configuration.append(question == "Yes")

        # Save the profile and configuration for the user's IP address
        profiles[ip_address] = {"profile_name": profile_name, "configuration": configuration}
        with open(f"config_{ip_address}.bin", "wb") as f:
            bit_array = bitarray.bitarray(configuration)
            bit_array.tofile(f)

        st.write("Profile created successfully!")
        st.write("Profile details:")
        st.write(f"Profile Name: {profile_name}")
        st.write(f"Configuration: {configuration}")

def load_profile():
    # Get the user's IP address
    ip_address = st.experimental_get_query_params().get("client_ip", [None])[0]

    # Check if the user's IP address has a profile
    if ip_address and ip_address in profiles:
        profile = profiles[ip_address]
        st.write(f"Welcome back, {profile['profile_name']}!")
        st.write("You can load your profile here.")
        st.write("Profile details:")
        st.write(f"Profile Name: {profile['profile_name']}")
        st.write(f"Configuration: {profile['configuration']}")

    else:
        st.write("You don't have a profile yet.")

try:
    profiles = {}
    with open("config.bin", "rb") as f:
        profiles = pickle.load(f)
except FileNotFoundError:
    pass

def main():
    st.title("Profile Creation")

    option = st.radio("Choose an option", ("Create a new profile", "Load an existing profile"))

    if option == "Create a new profile":
        create_profile()
    else:
        load_profile()

if __name__ == "__main__":
    main()
