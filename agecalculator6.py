import streamlit as st
import datetime
    
def ageCalculator():
    today = datetime.datetime.now().date()
    age = int((today.year - dob.year).date/365.25)
    print("You are", age, " years old!")
    
def main():
    st.title(' ofir Age Calculator')
    st.write("Welcome to the Age Calculator!")
    dob = st.date_input("Please enter your Birth Date:")
    ageCalculator()
    
main()
