import streamlit as st
import datetime

def get_value(dd, mm, yyyy):
    """
    We use eval() to get the value of the expression.
    ref: https://docs.python.org/3/library/functions.html#eval
    """
    return eval(user_expr, {"_builtins_": None})


    
def main():
    st.title(' ofir Age Calculator')
    
    # The input value from the user will be saved in user_expr.
    user_expr = st.int_input('Please enter your Date of Birth ("dd","mm","yyyy")')
    today = datetime.datetime.now().date()
    date_of_birth = datetime.date(dd,mm,yyyy)
    age = int((today - date_of_birth)/365.25)
    print("You are", age, " years old!")


# Entry point
if _name_ == "_main_":
main()
