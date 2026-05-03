import streamlit as st 
import pandas as pd

@st.cache_data
def load_data():
    df = pd.DataFrame(
        dict(
            subject = ['Math', 'English', 'Physics', 'Chemistry'],
            score = [52, 52, 54, 61]
        )
    )
    return df

data = load_data()

st.bar_chart(data, x='subject', y='score')