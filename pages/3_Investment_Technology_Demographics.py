import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data
from utils.filters import get_global_filters, show_missing_data_note

st.set_page_config(page_title="Investment & Technology", layout="wide")
st.markdown("""
<style>
.block-container {padding-top: 1.2rem;}
.chart-box {background:white; border:1.5px solid #d0d7e3; border-radius:12px; padding:12px;}
</style>
""", unsafe_allow_html=True)

df = load_data()
selected_countries, year_range, selected_indicator = get_global_filters(df)
st.markdown("### Investment & Technology")

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown("**Foreign direct investment trend**")
    d = df[(df["Country Name"].isin(selected_countries)) & (df["Series Name"]=="Foreign direct investment, net inflows (% of GDP)") & (df["Year"]>=year_range[0]) & (df["Year"]<=year_range[1])].dropna(subset=["Value"])
    if not d.empty:
        fig = px.line(d, x="Year", y="Value", color="Country Name", markers=True)
        fig.update_layout(height=300, margin=dict(l=10,r=10,t=10,b=10), plot_bgcolor="white", paper_bgcolor="white", legend=dict(orientation="h", y=-0.2))
        fig.update_xaxes(showgrid=False); fig.update_yaxes(showgrid=True, gridcolor="#eef2f7", title="% of GDP")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown("**Internet access growth**")
    d = df[(df["Country Name"].isin(selected_countries)) & (df["Series Name"]=="Individuals using the Internet (% of population)") & (df["Year"]>=year_range[0]) & (df["Year"]<=year_range[1])].dropna(subset=["Value"])
    if not d.empty:
        fig = px.line(d, x="Year", y="Value", color="Country Name", markers=True)
        fig.update_layout(height=300, margin=dict(l=10,r=10,t=10,b=10), plot_bgcolor="white", paper_bgcolor="white", legend=dict(orientation="h", y=-0.2))
        fig.update_xaxes(showgrid=False); fig.update_yaxes(showgrid=True, gridcolor="#eef2f7", title="% of population")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.markdown('<div class="chart-box">', unsafe_allow_html=True)
st.markdown("**Population by country**")
latest = year_range[1]
d = df[(df["Country Name"].isin(selected_countries)) & (df["Series Name"]=="Population, total") & (df["Year"]==latest)].dropna(subset=["Value"])
if not d.empty:
    fig = px.bar(d, x="Country Name", y="Value", color="Country Name")
    fig.update_layout(height=360, margin=dict(l=10,r=10,t=10,b=10), plot_bgcolor="white", paper_bgcolor="white", showlegend=False)
    fig.update_xaxes(showgrid=False); fig.update_yaxes(showgrid=True, gridcolor="#eef2f7", title="Population")
    st.plotly_chart(fig, use_container_width=True)
    st.caption(f"Latest year: {latest}")
else:
    st.info("No data available")
st.markdown('</div>', unsafe_allow_html=True)
st.caption("Urbanization and electricity are postponed as per MVP - only shown if confirmed as part of approved page.")

