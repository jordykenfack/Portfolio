import pandas
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.markdown("""
            <h1 style='font-family: "Times New Roman", Times,serif; font-weight:bold;font-size: 48px; color: #2c3e50;'>
                Donald Jordy
            </h1>
        """, unsafe_allow_html=True)
    content ="""
    Hi, I'm Donald Jordy — a Master's student in Applied Data Science with a passion for transforming data into meaningful insights.
I'm driven by curiosity and a desire to solve real-world problems through data. With a solid foundation in mathematics, programming, and statistical modeling, I'm actively building projects that showcase my ability to turn complex data into actionable results.

Whether it's machine learning, data visualization, or analytics, I aim to bridge the gap between raw data and decision-making. I'm currently expanding my portfolio while preparing to step into the professional world as a data scientist.
    """
    st.info(content)


content1 = """Below you will find some python apps I created."""
st.write(content1 )

col3,empty_col,col4 = st.columns([1.5,0.5,1.5])
df = pd.read_csv("data.csv",sep = ";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({'url'})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({'url'})")
