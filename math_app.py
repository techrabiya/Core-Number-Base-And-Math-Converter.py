import streamlit as st

st.set_page_config(page_title="Core Math Converter", page_icon="🔢")

st.title("🔢 Core Number Base Converter")
st.write("Convert decimal numbers into binary, octal, and hexadecimal formats instantly.")

num = st.number_input("Enter a decimal integer:", value=42, step=1)

if st.button("Compute Conversions"):
    binary_val = bin(int(num))
    octal_val = oct(int(num))
    hex_val = hex(int(num))
    
    st.write(f"### Results for integer: {num}")
    st.code(f"Binary (Base 2): {binary_val}\nOctal (Base 8): {octal_val}\nHexadecimal (Base 16): {hex_val}")
    st.balloons()
