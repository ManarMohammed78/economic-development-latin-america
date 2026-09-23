import streamlit as st
st.set_page_config(page_title="About", layout="wide")
st.markdown("""
<style>
.block-container {padding-top: 1.2rem;}
.about-box {background:white; border:1.5px solid #d0d7e3; border-radius:12px; padding:20px; line-height:1.7;}
</style>
""", unsafe_allow_html=True)

st.markdown("### About / Methodology")
st.markdown('<div class="about-box">', unsafe_allow_html=True)
st.markdown("""
**Data sources**<br>
World Bank Open Data, World Development Indicators. https://data.worldbank.org/<br><br>
**Indicators (12)**<br>
GDP per capita (current US$), GDP growth (annual %), Inflation consumer prices (annual %), Foreign direct investment net inflows (% of GDP), Unemployment total, Poverty headcount ratio, Life expectancy at birth, School enrollment secondary, Population total, Urban population, Individuals using the Internet, Access to electricity.<br><br>
**Methodology**<br>
Cleaned with Python pandas in Google Colab. 792 observations (6 countries x 12 indicators x 11 years) from 2014 to 2024. Long format: Country Name, Country Code, Series Name, Series Code, Year, Value. Loaded with pandas and st.cache_data, filtered in memory.<br><br>
**Limitations**<br>
Descriptive only, no causal or predictive claims. Poverty data missing for Brazil for entire period. Argentina inflation missing before 2018. Dataset ends at 2024.<br><br>
**Missing-data notes**<br>
Missing values are shown as No data available, never as zero. Argentina inflation line has gaps before 2018. Brazil is excluded from poverty charts.<br><br>
**Descriptive-only scope**<br>
Shows what happened between 2014 and 2024. Does not explain why and does not forecast.<br><br>
**2014–2024 cutoff**<br>
All charts and tables are limited to 2014 to 2024.
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.write("")
c1, c2 = st.columns(2)
with c1:
    st.link_button("Link: White Paper", "https://github.com/ManarMohammed78/economic-development-latin-america/blob/main/Economic_Development_Documentation.docx", use_container_width=True)
with c2:
    st.link_button("Link: Documentation", "https://github.com/ManarMohammed78/economic-development-latin-america", use_container_width=True)
