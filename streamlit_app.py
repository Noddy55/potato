import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
st.header("Click on this button")
st.write("hello world")
button_clicked= st.button("Click me")
second_button_clicked= st.button("Click not me")
st.write(f'button clicked: {button_clicked}')

if button_clicked:
    st.write("Why hello you")
else:
    st.write("Goodbye")


#day5

st.header("st.write")
st.write("**hello** *world* :sunglasses:")
st.write(1234*56789)
df = pd.DataFrame({'c1':[1,2,3,4,5],'c2':[6,7,8,9,10]})
st.write(df)

st.write("Before", df, "After :tada:")

arr= np.random.randn(200,3)
st.write(arr)
df2=pd.DataFrame(np.random.randn(200,3), columns=["a","b","c"])

c= alt.Chart(df2).mark_circle().encode(x="a", y="b", size="c", color="c").properties(title="hello")
st.write(c)