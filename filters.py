import streamlit as st
import pandas as pd

def get_global_filters(df: pd.DataFrame):
    """
    Global filters for all pages.
    Uses st.session_state so the selection stays the same when you switch pages.
    This solves the "global filter behavior" task from Milestone 4.
    """
    # Get available options from the data
    all_countries = sorted(df["Country Name"].unique())
    all_years = sorted(df["Year"].unique())
    all_indicators = sorted(df["Series Name"].unique())

    # Initialize session_state only once (keeps filters across pages)
    if "selected_countries" not in st.session_state:
        st.session_state.selected_countries = all_countries
    if "year_range" not in st.session_state:
        st.session_state.year_range = (min(all_years), max(all_years))
    if "selected_indicator" not in st.session_state:
        st.session_state.selected_indicator = all_indicators[0]

    # Sidebar - these widgets update session_state automatically
    st.sidebar.header("Filters")

    selected_countries = st.sidebar.multiselect(
        "Country",
        options=all_countries,
        default=st.session_state.selected_countries,
        key="selected_countries"
    )

    year_min, year_max = min(all_years), max(all_years)
    selected_year_range = st.sidebar.slider(
        "Year range",
        min_value=year_min,
        max_value=year_max,
        value=st.session_state.year_range,
        key="year_range"
    )

    selected_indicator = st.sidebar.selectbox(
        "Indicator",
        options=all_indicators,
        index=all_indicators.index(st.session_state.selected_indicator) if st.session_state.selected_indicator in all_indicators else 0,
        key="selected_indicator"
    )

    return selected_countries, selected_year_range, selected_indicator

def filter_dataframe(df: pd.DataFrame, countries, year_range, indicator):
    """Apply the global filters to the dataframe."""
    filtered = df[
        (df["Country Name"].isin(countries)) &
        (df["Year"] >= year_range[0]) &
        (df["Year"] <= year_range[1]) &
        (df["Series Name"] == indicator)
    ].copy()
    return filtered

def show_missing_data_note(filtered: pd.DataFrame):
    """
    Handle missing data exactly as in Milestone 1.
    Never show missing as zero. Show "No data available" with a note.
    Covers Argentina inflation before 2018 and Brazil poverty for all years.
    """
    if filtered.empty or filtered["Value"].isna().all():
        st.info("No data available for this selection. This matches the documented gaps: Argentina inflation before 2018 and Brazil poverty for all years are shown as No data available, not as zero.")
        return True
    elif filtered["Value"].isna().any():
        missing_years = filtered[filtered["Value"].isna()][["Country Name", "Year"]].head(3).values.tolist()
        st.caption(f"Note: Some years have no data and are shown as gaps. Example missing: {missing_years}. Values are shown as No data available.")
        return False
    return False
