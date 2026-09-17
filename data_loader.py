import pandas as pd
import streamlit as st
from pathlib import Path

# Path to cleaned dataset - relative to project root
DATA_PATH = Path(__file__).parent.parent / "data" / "Latin_America_Economic_Development_Clean.csv"

@st.cache_data
def load_data():
    """
    Load the cleaned dataset.
    Uses st.cache_data so the CSV is only read once per session.
    Handles the two known data gaps:
    - Argentina inflation missing before 2018 (shown as NaN)
    - Brazil poverty missing for all years (shown as NaN)
    """
    df = pd.read_csv(DATA_PATH)
    
    # Ensure expected columns are present (same 6-field structure from Milestone 1)
    expected_cols = ["Country Name", "Country Code", "Series Name", "Series Code", "Year", "Value"]
    for col in expected_cols:
        if col not in df.columns:
            raise ValueError(f"Missing expected column: {col}")
    
    # Convert Year to int and sort for consistent display
    df["Year"] = df["Year"].astype(int)
    df = df.sort_values(["Country Name", "Series Name", "Year"])
    
    return df

def validate_dataset(df: pd.DataFrame):
    """
    Quick validation used during development.
    Checks the same numbers agreed in Milestone 1:
    792 observations (6 countries * 12 indicators * 11 years)
    12 indicators, 6 countries, 2014-2024
    """
    checks = {
        "total_rows": len(df) == 792,
        "num_indicators": df["Series Name"].nunique() == 12,
        "num_countries": df["Country Name"].nunique() == 6,
        "year_range": (df["Year"].min() == 2014 and df["Year"].max() == 2024),
    }
    return checks

def get_available_filters(df: pd.DataFrame):
    """Helper for sidebar filters - returns sorted lists for UI."""
    countries = sorted(df["Country Name"].unique())
    indicators = sorted(df["Series Name"].unique())
    years = sorted(df["Year"].unique())
    return countries, indicators, years
