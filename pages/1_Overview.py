import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

st.title("Overview")
st.caption("Headline trends for GDP per capita, unemployment and inflation. Filters from the sidebar apply to all charts.")

df = load_data()
# This is a placeholder for Milestone 3. Full implementation is in Milestone 4 (see Issue #1).
# For now, it confirms the data loads and shows a simple example chart.
sample = df[df["Series Name"] == "GDP per capita (current US$)"]
fig = px.line(sample, x="Year", y="Value", color="Country Name", title="GDP per capita (sample check)")
st.plotly_chart(fig, use_container_width=True)
st.info("Milestone 3: page structure created. Chart logic to be completed in Milestone 4.")
