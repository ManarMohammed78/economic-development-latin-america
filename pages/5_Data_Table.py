import streamlit as st
from utils.data_loader import load_data
st.title("Data Table")
st.caption("Raw values behind the charts. Placeholder for Milestone 4 (Issue #6 & #7).")
df = load_data()
st.dataframe(df.head(20))
st.write("CSV export will download filtered rows only.")
