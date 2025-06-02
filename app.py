import streamlit as st

st.title("Power calulator")
st.write("Enter the number which You want to calculate the square and cube of ")

n=int(st.number_input("Enter the integer",value=1,step=1))

square=n*n
cube=n*n*n

st.write(f"The square of {n} is {int(square)}")
st.write(f"The cube of {n} is {int(cube)}")
