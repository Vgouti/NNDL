import streamlit as st
import numpy as np
import pandas as pd

st.title("Hello this is the first application")


st.write("This works!!!!")

data=pd.DataFrame({
    'Emp_id':['101','102','103'],
    'Emp_name':['Vaibhav','Vidhyam','Ayush']
})

st.write(data)

data1=pd.DataFrame(np.random.randn(25,3),columns=['A','B','C'])
st.line_chart(data1)

