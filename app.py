import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data

st.set_page_config(page_title="Economic Development App", layout="wide")

# Hide sidebar to match wireframe (filters are at top, not sidebar)
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
.block-container {padding-top: 3.5rem !important; padding-bottom: 2rem !important; max-width: 1400px !important; padding-left: 1.5rem !important; padding-right: 1.5rem !important;}
header[data-testid="stHeader"] {display: none !important;}
.stApp > header {display: none !important;}
.top-nav {display: flex; gap: 8px; margin-bottom: 16px; margin-top: 8px;}
.nav-btn {flex: 1; padding: 10px; text-align: center; border: 1.5px solid #a8bdd6; border-radius: 6px; background: white; font-size: 14px; cursor: pointer;}
.nav-selected {background: #d6e4f0 !important; font-weight: 700; border-color: #4a6fa5 !important;}
.kpi-card {background:#eaf2fb; border:1.5px solid #a8bdd6; border-radius:12px; padding:18px 10px; text-align:center; height:110px;}
.kpi-title {color:#5a6d8a; font-size:13px; margin:0 0 6px 0;}
.kpi-value {color:#0f2a44; font-size:26px; font-weight:700; margin:0;}
.chart-box {background:white; border:1.5px solid #d0d7e3; border-radius:12px; padding:16px; margin-bottom: 18px;}
</style>
""", unsafe_allow_html=True)

df = load_data()

# --- Top Navigation (like wireframe) ---
if "page" not in st.session_state:
    st.session_state.page = "Overview"

nav_cols = st.columns(6)
pages = ["Overview", "Social Dev.", "Invest. & Tech", "Insights", "Data Table", "About"]
for i, p in enumerate(pages):
    with nav_cols[i]:
        if st.button(p, key=f"nav_{p}", width="stretch", type="primary" if st.session_state.page==p else "secondary"):
            st.session_state.page = p
            st.rerun()

# Highlight selected via custom CSS handled by button type (primary is blue)
# --- Top Filters (like wireframe: Country, Year, Indicator) ---
f1, f2, f3 = st.columns(3)
all_countries = ["All"] + sorted(df["Country Name"].unique())
# For wireframe we show Country: All as default
if "filt_country" not in st.session_state:
    st.session_state.filt_country = "All"
if "filt_year" not in st.session_state:
    st.session_state.filt_year = "2014-2024"
if "filt_indicator" not in st.session_state:
    st.session_state.filt_indicator = "GDP per capita"

with f1:
    sel_country = st.selectbox("Country:", all_countries, key="filt_country", label_visibility="collapsed", placeholder="Country: All")
    # To match wireframe label inside
    st.markdown(f"<div style='margin-top:-18px; margin-left:10px; font-size:12px; color:#333; pointer-events:none'>Country: {sel_country} ▾</div>", unsafe_allow_html=True)
with f2:
    # Flexible year filter inside a rectangle like the other filters
    st.markdown('<div style="border:1.5px solid #a8bdd6; border-radius:8px; background:white; padding:8px 10px 2px 10px; margin-top:4px;">', unsafe_allow_html=True)
    if "filt_year_range" not in st.session_state:
        st.session_state.filt_year_range = (2014, 2024)
    sel_year_range = st.slider("Year:", 2014, 2024, value=st.session_state.filt_year_range, key="filt_year_range", label_visibility="collapsed")
    if sel_year_range[0] == sel_year_range[1]:
        label = f"{sel_year_range[0]}"
    else:
        label = f"{sel_year_range[0]}-{sel_year_range[1]}"
    st.markdown(f"<div style='margin-top:-8px; margin-left:2px; font-size:11px; color:#5a6d8a;'>Year: {label}</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    sel_year = label
with f3:
    all_inds = sorted(df["Series Name"].unique())
    # Shorten for display like wireframe shows GDP per capita
    sel_indicator = st.selectbox("Indicator:", all_inds, key="filt_indicator", label_visibility="collapsed")
    # Show as Indicator: GDP per capita
    short = sel_indicator.split("(")[0].strip() if "(" in sel_indicator else sel_indicator
    if len(short) > 28:
        short = short[:28] + "..."
    st.markdown(f"<div style='margin-top:-18px; margin-left:10px; font-size:12px; color:#333; pointer-events:none'>Indicator: {short} ▾</div>", unsafe_allow_html=True)

st.write("")
# Parse filters
if sel_country == "All":
    filt_countries = sorted(df["Country Name"].unique())
else:
    filt_countries = [sel_country]

# Parse year range from flexible slider
y0, y1 = sel_year_range

filt_indicator = sel_indicator

# Helper
def get_trend(ind):
    return df[(df["Country Name"].isin(filt_countries)) & (df["Series Name"]==ind) & (df["Year"]>=y0) & (df["Year"]<=y1)].dropna(subset=["Value"])

def get_kpi(ind, yr):
    sub = df[(df["Country Name"].isin(filt_countries)) & (df["Series Name"]==ind) & (df["Year"]==yr)].dropna(subset=["Value"])
    return sub["Value"].mean() if not sub.empty else None

# --- PAGE CONTENT ---
if st.session_state.page == "Overview":
    st.markdown("### Home / Overview")
    # KPIs
    latest = y1
    kpi_gdp = get_kpi("GDP per capita (current US$)", latest)
    kpi_unemp = get_kpi("Unemployment, total (% of total labor force) (modeled ILO estimate)", latest)
    kpi_infl = get_kpi("Inflation, consumer prices (annual %)", latest)
    c1, c2, c3 = st.columns(3)
    with c1:
        val = f"${kpi_gdp:,.0f}" if kpi_gdp is not None else "No data"
        st.markdown(f'<div class="kpi-card"><div class="kpi-title">GDP per capita</div><div class="kpi-value">{val}</div></div>', unsafe_allow_html=True)
    with c2:
        val = f"{kpi_unemp:.1f}%" if kpi_unemp is not None else "No data"
        st.markdown(f'<div class="kpi-card"><div class="kpi-title">Unemployment</div><div class="kpi-value">{val}</div></div>', unsafe_allow_html=True)
    with c3:
        val = f"{kpi_infl:.1f}%" if kpi_infl is not None else "No data"
        st.markdown(f'<div class="kpi-card"><div class="kpi-title">Inflation</div><div class="kpi-value">{val}</div></div>', unsafe_allow_html=True)
    st.write("")
    a, b = st.columns(2)
    with a:
        st.markdown('<div class="chart-box">', unsafe_allow_html=True)
        st.markdown("**GDP per capita trend**")
        d = get_trend("GDP per capita (current US$)")
        if not d.empty:
            fig = px.line(d, x="Year", y="Value", color="Country Name", markers=True)
            fig.update_layout(height=280, margin=dict(l=10,r=10,t=10,b=10), plot_bgcolor="white", paper_bgcolor="white", legend=dict(orientation="h", y=-0.2))
            fig.update_xaxes(showgrid=False); fig.update_yaxes(showgrid=True, gridcolor="#eef2f7", title="US$")
            st.plotly_chart(fig, width="stretch")
        else:
            st.info("No data available")
        st.markdown('</div>', unsafe_allow_html=True)
    with b:
        st.markdown('<div class="chart-box">', unsafe_allow_html=True)
        st.markdown("**Unemployment trend**")
        d = get_trend("Unemployment, total (% of total labor force) (modeled ILO estimate)")
        if not d.empty:
            fig = px.line(d, x="Year", y="Value", color="Country Name", markers=True)
            fig.update_layout(height=280, margin=dict(l=10,r=10,t=10,b=10), plot_bgcolor="white", paper_bgcolor="white", legend=dict(orientation="h", y=-0.2))
            fig.update_xaxes(showgrid=False); fig.update_yaxes(showgrid=True, gridcolor="#eef2f7", title="%")
            st.plotly_chart(fig, width="stretch")
        else:
            st.info("No data available")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown("**Inflation trend (Argentina shown separately)**")
    d = get_trend("Inflation, consumer prices (annual %)")
    if not d.empty:
        fig = px.line(d, x="Year", y="Value", color="Country Name", markers=True)
        fig.update_layout(height=320, margin=dict(l=10,r=10,t=10,b=10), plot_bgcolor="white", paper_bgcolor="white", legend=dict(orientation="h", y=-0.25))
        fig.update_xaxes(showgrid=False); fig.update_yaxes(showgrid=True, gridcolor="#eef2f7", title="Annual %")
        st.plotly_chart(fig, width="stretch")
        if "Argentina" in filt_countries and len(filt_countries)>1:
            st.caption("Note: Argentina's scale is much higher, shown as a higher line.")
    else:
        st.info("No data available")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "Social Dev.":
    st.markdown("### Social Development")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="chart-box">', unsafe_allow_html=True)
        st.markdown("**Life expectancy trend**")
        d = get_trend("Life expectancy at birth, total (years)")
        if not d.empty:
            fig = px.line(d, x="Year", y="Value", color="Country Name", markers=True)
            fig.update_layout(height=300, margin=dict(l=10,r=10,t=10,b=10), plot_bgcolor="white", paper_bgcolor="white", legend=dict(orientation="h", y=-0.2))
            fig.update_xaxes(showgrid=False); fig.update_yaxes(showgrid=True, gridcolor="#eef2f7", title="Years")
            st.plotly_chart(fig, width="stretch")
        else:
            st.info("No data available")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="chart-box">', unsafe_allow_html=True)
        st.markdown("**Poverty rate by country (latest year, Brazil excluded)**")
        latest = y1
        d = df[(df["Country Name"].isin(filt_countries)) & (df["Series Name"]=="Poverty headcount ratio at national poverty lines (% of population)") & (df["Year"]==latest)]
        d = d[d["Country Name"]!="Brazil"].dropna(subset=["Value"])
        if not d.empty:
            fig = px.bar(d, x="Country Name", y="Value", color="Country Name")
            fig.update_layout(height=300, margin=dict(l=10,r=10,t=10,b=10), plot_bgcolor="white", paper_bgcolor="white", showlegend=False)
            fig.update_xaxes(showgrid=False); fig.update_yaxes(showgrid=True, gridcolor="#eef2f7", title="% of population")
            st.plotly_chart(fig, width="stretch")
            st.caption(f"Latest year: {latest}. Brazil excluded.")
        else:
            st.info("No data available - Brazil is excluded.")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown("**Secondary school enrollment trend**")
    d = get_trend("School enrollment, secondary (% gross)")
    if not d.empty:
        fig = px.line(d, x="Year", y="Value", color="Country Name", markers=True)
        fig.update_layout(height=360, margin=dict(l=10,r=10,t=10,b=10), plot_bgcolor="white", paper_bgcolor="white", legend=dict(orientation="h", y=-0.2))
        fig.update_xaxes(showgrid=False); fig.update_yaxes(showgrid=True, gridcolor="#eef2f7", title="% gross")
        st.plotly_chart(fig, width="stretch")
    else:
        st.info("No data available")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "Invest. & Tech":
    st.markdown("### Investment & Technology")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="chart-box">', unsafe_allow_html=True)
        st.markdown("**Foreign direct investment trend**")
        d = get_trend("Foreign direct investment, net inflows (% of GDP)")
        if not d.empty:
            fig = px.line(d, x="Year", y="Value", color="Country Name", markers=True)
            fig.update_layout(height=300, margin=dict(l=10,r=10,t=10,b=10), plot_bgcolor="white", paper_bgcolor="white", legend=dict(orientation="h", y=-0.2))
            fig.update_xaxes(showgrid=False); fig.update_yaxes(showgrid=True, gridcolor="#eef2f7", title="% of GDP")
            st.plotly_chart(fig, width="stretch")
        else:
            st.info("No data available")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="chart-box">', unsafe_allow_html=True)
        st.markdown("**Internet access growth**")
        d = get_trend("Individuals using the Internet (% of population)")
        if not d.empty:
            fig = px.line(d, x="Year", y="Value", color="Country Name", markers=True)
            fig.update_layout(height=300, margin=dict(l=10,r=10,t=10,b=10), plot_bgcolor="white", paper_bgcolor="white", legend=dict(orientation="h", y=-0.2))
            fig.update_xaxes(showgrid=False); fig.update_yaxes(showgrid=True, gridcolor="#eef2f7", title="% of population")
            st.plotly_chart(fig, width="stretch")
        else:
            st.info("No data available")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown("**Population by country**")
    latest = y1
    d = df[(df["Country Name"].isin(filt_countries)) & (df["Series Name"]=="Population, total") & (df["Year"]==latest)].dropna(subset=["Value"])
    if not d.empty:
        fig = px.bar(d, x="Country Name", y="Value", color="Country Name")
        fig.update_layout(height=360, margin=dict(l=10,r=10,t=10,b=10), plot_bgcolor="white", paper_bgcolor="white", showlegend=False)
        fig.update_xaxes(showgrid=False); fig.update_yaxes(showgrid=True, gridcolor="#eef2f7", title="Population")
        st.plotly_chart(fig, width="stretch")
        st.caption(f"Latest year: {latest}")
    else:
        st.info("No data available")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "Insights":
    st.markdown("### Insights (16 documented findings)")
    # Theme filter at top like wireframe
    theme_options = ["All", "Economic Growth", "Social Development", "Investment Trends", "Regional Comparison"]
    if "insights_theme_top" not in st.session_state:
        st.session_state.insights_theme_top = "All"
    sel_theme = st.selectbox("Theme:", theme_options, key="insights_theme_top", label_visibility="collapsed")
    st.markdown(f"<div style='margin-top:-18px; margin-left:10px; font-size:12px; color:#333; pointer-events:none'>Theme: {sel_theme} ▾</div>", unsafe_allow_html=True)
    st.write("")
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
    filtered = [i for i in insights if sel_theme=="All" or i["theme"]==sel_theme]
    cols = st.columns(2)
    for idx, ins in enumerate(filtered):
        col = cols[idx % 2]
        with col:
            st.markdown(f'<div style="background:white; border:1.5px solid #d0d7e3; border-radius:12px; padding:16px; height:150px; margin-bottom:14px"><b>Theme: {ins["theme"]}</b><br><br>{ins["text"]}</div>', unsafe_allow_html=True)

elif st.session_state.page == "Data Table":
    st.markdown("### Data Table")
    filtered = df[(df["Country Name"].isin(filt_countries)) & (df["Year"]>=y0) & (df["Year"]<=y1) & (df["Series Name"]==filt_indicator)].copy()
    st.dataframe(filtered.sort_values(["Country Name","Year"])[["Country Name","Series Name","Year","Value"]], width="stretch", height=460)
    st.caption(f"Showing {len(filtered)} rows. Click header to sort.")
    csv = filtered.to_csv(index=False).encode("utf-8")
    # Right align button like wireframe
    c1, c2, c3 = st.columns([6,2,2])
    with c3:
        st.download_button(label="Export CSV", data=csv, file_name="filtered_data.csv", mime="text/csv", type="primary", width="stretch")

elif st.session_state.page == "About":
    st.markdown("### About / Methodology")
    st.markdown('<div style="background:white; border:1.5px solid #d0d7e3; border-radius:12px; padding:20px; line-height:1.7">', unsafe_allow_html=True)
    st.markdown("""
**Data sources**<br>
World Bank Open Data, World Development Indicators. https://data.worldbank.org/<br><br>
**Indicators (12)**<br>
GDP per capita, GDP growth, Inflation, FDI, Unemployment, Poverty, Life expectancy, School enrollment, Population, Urban population, Internet access, Access to electricity.<br><br>
**Methodology**<br>
Cleaned with Python pandas in Google Colab. 792 observations (6 countries x 12 indicators x 11 years) 2014-2024. Long format. Loaded with pandas and st.cache_data.<br><br>
**Limitations**<br>
Descriptive only, no causal claims. Poverty missing for Brazil. Argentina inflation missing before 2018. Ends at 2024.<br><br>
**Missing-data notes**<br>
Missing as No data available, never zero.<br><br>
**Descriptive-only scope**<br>
Shows what happened 2014-2024, no forecast.<br>
""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("")
    c1, c2 = st.columns(2)
    with c1:
        st.link_button("Link: White Paper", "https://github.com/ManarMohammed78/economic-development-latin-america/blob/main/docs/Economic%20Development%20White%20Paper%20.pdf", width="stretch")
    with c2:
        st.link_button("Link: Documentation", "https://github.com/ManarMohammed78/economic-development-latin-america/blob/main/docs/Economic_Development_Documentation.docx", width="stretch")
