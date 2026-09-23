import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data
from utils.filters import get_global_filters, show_missing_data_note

st.set_page_config(page_title="Social Development", layout="wide")
st.markdown("""
<style>
.block-container {padding-top: 1.2rem;}
.chart-box {background:white; border:1.5px solid #d0d7e3; border-radius:12px; padding:12px;}
</style>
""", unsafe_allow_html=True)

df = load_data()
selected_countries, year_range, selected_indicator = get_global_filters(df)
st.markdown("### Social Development")

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown("**Life expectancy trend**")
    d = df[(df["Country Name"].isin(selected_countries)) & (df["Series Name"]=="Life expectancy at birth, total (years)") & (df["Year"]>=year_range[0]) & (df["Year"]<=year_range[1])].dropna(subset=["Value"])
    if not d.empty:
        fig = px.line(d, x="Year", y="Value", color="Country Name", markers=True)
        fig.update_layout(height=300, margin=dict(l=10,r=10,t=10,b=10), plot_bgcolor="white", paper_bgcolor="white", legend=dict(orientation="h", y=-0.2))
        fig.update_xaxes(showgrid=False); fig.update_yaxes(showgrid=True, gridcolor="#eef2f7", title="Years")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown("**Poverty rate by country (latest year, Brazil excluded)**")
    latest = year_range[1]
    d = df[(df["Country Name"].isin(selected_countries)) & (df["Series Name"]=="Poverty headcount ratio at national poverty lines (% of population)") & (df["Year"]==latest)]
    d = d[d["Country Name"]!="Brazil"].dropna(subset=["Value"])
    if not d.empty:
        fig = px.bar(d, x="Country Name", y="Value", color="Country Name")
        fig.update_layout(height=300, margin=dict(l=10,r=10,t=10,b=10), plot_bgcolor="white", paper_bgcolor="white", showlegend=False)
        fig.update_xaxes(showgrid=False); fig.update_yaxes(showgrid=True, gridcolor="#eef2f7", title="% of population")
        st.plotly_chart(fig, use_container_width=True)
        st.caption(f"Latest year: {latest}. Brazil excluded - no data for this period.")
    else:
        st.info("No data available - Brazil is excluded and other countries have no data for this year.")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.markdown('<div class="chart-box">', unsafe_allow_html=True)
st.markdown("**Secondary school enrollment trend**")
d = df[(df["Country Name"].isin(selected_countries)) & (df["Series Name"]=="School enrollment, secondary (% gross)") & (df["Year"]>=year_range[0]) & (df["Year"]<=year_range[1])].dropna(subset=["Value"])
if not d.empty:
    fig = px.line(d, x="Year", y="Value", color="Country Name", markers=True)
    fig.update_layout(height=360, margin=dict(l=10,r=10,t=10,b=10), plot_bgcolor="white", paper_bgcolor="white", legend=dict(orientation="h", y=-0.2))
    fig.update_xaxes(showgrid=False); fig.update_yaxes(showgrid=True, gridcolor="#eef2f7", title="% gross")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No data available")
st.markdown('</div>', unsafe_allow_html=True)
