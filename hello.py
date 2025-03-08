
import streamlit as st

st.title(" :rocket: Unit Converter App")
st.markdown("### This app converts length, weight, and time")
st.write("Select the category and enter a value to get your results instantly:blush:.")


category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

if category == "Length":
    unit = st.selectbox("Select conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("Select conversion", ["Seconds to Minutes", "Minutes to Seconds"])

# User input for conversion
value = st.number_input("Enter the value to convert")

# Conversion function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60

# Convert button
if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is :rocket:{result:.2f}")
