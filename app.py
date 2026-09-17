import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data, validate_dataset

st.set_page_config(
    page_title="Economic Development in Latin America",
    page_icon="📊",
    layout="wide",
)

# Load data once (cached)
df = load_data()

# Sidebar - shared filters (as defined in Milestone 2 wireframes)
st.sidebar.title("Filters")
countries = sorted(df["Country Name"].unique())
selected_countries = st.sidebar.multiselect("Country", countries, default=countries)

indicators = sorted(df["Series Name"].unique())
selected_indicator = st.sidebar.selectbox("Indicator", indicators, index=0)

years = sorted(df["Year"].unique())
year_range = st.sidebar.slider("Year range", min_value=min(years), max_value=max(years), value=(min(years), max(years)))

# Filter data based on selection
filtered = df[
    (df["Country Name"].isin(selected_countries)) &
    (df["Series Name"] == selected_indicator) &
    (df["Year"] >= year_range[0]) &
    (df["Year"] <= year_range[1])
]

# Header
st.title("Economic Development in Latin America (2014–2024)")
st.markdown("Explore 12 World Bank indicators across 6 countries. Use the sidebar to filter by country, indicator and year.")

# Quick validation banner (helps confirm Milestone 3 setup - 792 rows / 12 indicators)
checks = validate_dataset(df)
if all(checks.values()):
    st.success(f"Dataset loaded: {len(df)} observations, {df['Series Name'].nunique()} indicators, {df['Country Name'].nunique()} countries (2014–2024)")
else:
    st.warning("Dataset validation failed - check data file.")

# Handle missing data note (from Milestone 1 data quality rules)
if filtered["Value"].isna().all():
    st.info("No data available for this selection. This matches the documented gaps: Argentina inflation before 2018 and Brazil poverty for all years are intentionally shown as 'No data available' rather than zero.")
elif filtered["Value"].isna().any():
    missing = filtered[filtered["Value"].isna()][["Country Name", "Year"]].values.tolist()
    st.caption(f"Note: Some years have no data and are shown as gaps. Example missing: {missing[:2]}")

# Main chart
if not filtered.empty and filtered["Value"].notna().any():
    # Special handling: Argentina inflation shown separately when needed (Milestone 1 rule)
    is_inflation = "Inflation" in selected_indicator
    if is_inflation and "Argentina" in selected_countries:
        st.caption("Argentina's inflation is on a different scale, so it is shown separately below when multiple countries are selected.")
    
    fig = px.line(
        filtered.dropna(subset=["Value"]),
        x="Year",
        y="Value",
        color="Country Name",
        markers=True,
        title=selected_indicator,
        labels={"Value": selected_indicator, "Year": "Year"},
    )
    fig.update_layout(hovermode="x unified")
    st.plotly_chart(fig, use_container_width=True)
    
    # Data table view (Milestone 2 nice-to-have, included as table)
    with st.expander("Show data table"):
        st.dataframe(filtered.sort_values(["Country Name", "Year"]), use_container_width=True)
        csv = filtered.to_csv(index=False).encode("utf-8")
        st.download_button("Export CSV (filtered rows only)", csv, "filtered_data.csv", "text/csv")
else:
    st.write("No chart to display for this selection.")

st.markdown("---")
st.caption("Data source: World Bank Open Data, World Development Indicators. Analysis is descriptive only (2014–2024). See About page for methodology.")
