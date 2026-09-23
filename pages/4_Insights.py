import streamlit as st
st.set_page_config(page_title="Insights", layout="wide")
st.markdown("""
<style>
.block-container {padding-top: 1.2rem;}
.insight-card {background:white; border:1.5px solid #d0d7e3; border-radius:12px; padding:16px; height:170px;}
</style>
""", unsafe_allow_html=True)

st.sidebar.header("Filters")
theme_options = ["All", "Economic Growth", "Social Development", "Investment Trends", "Regional Comparison"]
selected_theme = st.sidebar.selectbox("Theme", theme_options, key="insights_theme")

st.markdown("### Insights (16 documented findings)")

insights = [
    {"theme": "Economic Growth", "text": "All six countries showed a synchronized drop in GDP per capita in 2020, ranging from 9.5% to 21.7%."},
    {"theme": "Economic Growth", "text": "Argentina had the highest GDP volatility across 2014-2024, linked to its inflation pattern."},
    {"theme": "Economic Growth", "text": "Chile consistently had the highest GDP per capita across the period."},
    {"theme": "Economic Growth", "text": "GDP growth was negative for most countries in 2020, then recovered in 2021."},
    {"theme": "Social Development", "text": "Life expectancy dropped for all countries between 2019 and 2021, with the smallest drop in Chile."},
    {"theme": "Social Development", "text": "Poverty data is missing for Brazil for all years, so Brazil is excluded from poverty comparisons."},
    {"theme": "Social Development", "text": "School enrollment remained above 90% for most countries, showing stable secondary education coverage."},
    {"theme": "Social Development", "text": "Unemployment spiked in 2020 for all six countries, with the sharpest rise in Colombia and Brazil."},
    {"theme": "Investment Trends", "text": "Foreign direct investment as percent of GDP was highest in Chile in most years."},
    {"theme": "Investment Trends", "text": "FDI inflows dropped in 2020 for five of the six countries."},
    {"theme": "Investment Trends", "text": "Internet access grew steadily for all countries, from around 50% in 2014 to over 75% in 2024."},
    {"theme": "Investment Trends", "text": "Population growth showed no consistent relationship with GDP per capita performance."},
    {"theme": "Regional Comparison", "text": "Mexico and Brazil have the largest populations, but not the highest GDP per capita."},
    {"theme": "Regional Comparison", "text": "Urban population share is above 85% for Chile and Argentina, above 75% for all countries."},
    {"theme": "Regional Comparison", "text": "Access to electricity is near 100% for all six countries across the period."},
    {"theme": "Regional Comparison", "text": "Inflation in Argentina rose from about 34% in 2018 to 219.9% in 2024, a separate trajectory."},
]

filtered = [i for i in insights if selected_theme=="All" or i["theme"]==selected_theme]
cols = st.columns(2)
for idx, ins in enumerate(filtered):
    col = cols[idx % 2]
    with col:
        st.markdown(f'<div class="insight-card"><b>Theme: {ins["theme"]}</b><br><br>{ins["text"]}<br><br><span style="color:#8a9bb5; font-size:11px">Descriptive finding - no causal claim.</span></div>', unsafe_allow_html=True)
        st.write("")
st.caption("All insights are descriptive only, based on the cleaned dataset 2014-2024, no predictive claims.")
