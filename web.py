import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

web_header = "The Best Company"
st.header(web_header)

with open("web.txt", "r") as files:
    content = files.read()
    st.write(content)

st.subheader("our team")

# Make a dataframe with the company members
df = pd.read_csv("data.csv")

# Prepare the column
col1, col2, col3 = st.columns(3)

with col1:
    # Iterate over only the first four rows
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # st.title(row["first name"] + " " + row["last name"]) works as well
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    # Iterate over rows 4 to 7
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    # Iterate over rows 8 to the remaining
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])


