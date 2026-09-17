import streamlit as st
from utils.data_loader import load_data
st.title("Social Development")
st.caption("Life expectancy, poverty and school enrollment. Placeholder for Milestone 4 (Issue #2).")
df = load_data()
st.write(f"Dataset ready: {len(df)} rows. This page will show life expectancy trends and poverty (Brazil excluded).")
