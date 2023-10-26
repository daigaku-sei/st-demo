import streamlit as st
import bitarray
import os

def create_profile():
    # Get the user's IP address
    ip_address = st.experimental_get_query_params().get("client_ip", [None])[0]

    # Check if the user's IP address already has a profile
    if ip_address and os.path.exists(ip_address):
        st.write("You already have a profile!")

    else:
        # Get the profile name from the user
        profile_name = st.text_input("Enter your profile name")

        # Get the configuration from the user
        configuration = []
        for i in range(8):
            question = st.radio(f"Question {i+1}", ("Yes", "No"))
            configuration.append(question == "Yes")

        # Create a folder for the user's IP address if it doesn't exist
        if not os.path.exists(ip_address):
            os.makedirs(ip_address)

        # Save the profile and configuration for the user's IP address
        profile_path = os.path.join(ip_address, "profile.bin")
        config_path = os.path.join(ip_address, "config.bin")

        with open(profile_path, "wb") as f:
            f.write(profile_name.encode())

        with open(config_path, "wb") as f:
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
    if ip_address and os.path.exists(ip_address):
        profile_path = os.path.join(ip_address, "profile.bin")
        config_path = os.path.join(ip_address, "config.bin")

        with open(profile_path, "rb") as f:
            profile_name = f.read().decode()

        with open(config_path, "rb") as f:
            bit_array = bitarray.bitarray()
            bit_array.fromfile(f)
            configuration = list(bit_array)

        st.write(f"Welcome back, {profile_name}!")
        st.write("You can load your profile here.")
        st.write("Profile details:")
        st.write(f"Profile Name: {profile_name}")
        st.write(f"Configuration: {configuration}")

    else:
        st.write("You don't have a profile yet.")

def main():
    st.title("Profile Creation")

    option = st.radio("Choose an option", ("Create a new profile", "Load an existing profile"))

    if option == "Create a new profile":
        create_profile()
    else:
        load_profile()

if __name__ == "__main__":
    main()
