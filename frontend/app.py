import streamlit as st
import pandas as pd
import numpy as np

st.logo("../logo.png")

st.title("AutoSchedulr")
st.write("A simple schedular to automate ur booring workflow of adding events in Google Calender manually.")
st.divider()

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file:

    df = pd.DataFrame(np.random.randn(50, 5), columns=("col %d" % i for i in range(5)))
    st.dataframe(df)  

st.divider()

st.write("RATE US")
selected = st.feedback("faces")
print(selected)
if selected is not None:
    if selected==0:
        st.markdown("We will try to improve.")
    elif selected==1 or selected==2:
        st.markdown("What is that thing u feel is messed up ?")
        title = st.text_input("Feedback")
        if title !="":
            st.write("Thanks bro")
    else:
        st.markdown("Thank you so much :)")