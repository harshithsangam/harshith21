import streamlit as st
import datetime
    
def main():
    st.title(' ofir Age Calculator')
    st.write("Welcome to the Age Calculator!")
    
    # The input value from the user will be saved in user_expr.
    
    day= st.int_input('Please enter your Birth Date:')
    month = st.int_input("Please enter your Birth Month:")
    year = st.int_input("Please enter your Birth Year:")
    today = datetime.datetime.now().date()
    date_of_birth = datetime.date(day,month,year)
    age = int((today - date_of_birth)/365.25)
    print("You are", age, " years old!")

main()
