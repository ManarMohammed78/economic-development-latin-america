import streamlit as st
import pandas as pd
from utils.data_loader import load_data
from utils.filters import get_global_filters

st.set_page_config(page_title="Data Table", layout="wide")
st.markdown("""
<style>
.block-container {padding-top: 1.2rem;}
</style>
""", unsafe_allow_html=True)

df = load_data()
selected_countries, year_range, selected_indicator = get_global_filters(df)
st.markdown("### Data Table")

filtered = df[(df["Country Name"].isin(selected_countries)) & (df["Year"]>=year_range[0]) & (df["Year"]<=year_range[1]) & (df["Series Name"]==selected_indicator)].copy()

st.dataframe(filtered.sort_values(["Country Name","Year"])[["Country Name","Series Name","Year","Value"]], use_container_width=True, height=450)
st.caption(f"Showing {len(filtered)} rows filtered by current dashboard filters. Click column header to sort.")
csv = filtered.to_csv(index=False).encode("utf-8")
st.download_button(label="Export CSV", data=csv, file_name="filtered_data.csv", mime="text/csv", type="primary")
