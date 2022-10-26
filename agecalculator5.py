import streamlit as st
import datetime
    
def ageCalculator(year, month, day):
    today = datetime.datetime.now().date()
    date_of_birth = datetime.date(year,month,day)
    age = int((today - date_of_birth).date/365.25)
    print("You are", age, " years old!")
    
def main():
    st.title(' ofir Age Calculator')
    st.write("Welcome to the Age Calculator!")
    day = st.int_input('Please enter your Birth Date (d or dd):')
    month = st.int_input("Please enter your Birth Month (m or mm):")
    year = st.int_input("Please enter your Birth Year (yyyy):")
    ageCalculator(year, month, date)
    
main()
