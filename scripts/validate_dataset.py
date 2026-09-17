"""
Validation script for Milestone 3
Run: python scripts/validate_dataset.py
Checks that the cleaned dataset loads and has the expected 792 observations and 12 indicators
as defined in Milestone 1 and Milestone 2.
"""
import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data" / "Latin_America_Economic_Development_Clean.csv"

def main():
    print("Loading dataset from:", DATA_PATH)
    df = pd.read_csv(DATA_PATH)
    
    print("\nColumns:", list(df.columns))
    print("Shape:", df.shape)
    print("Year range:", df["Year"].min(), "to", df["Year"].max())
    print("Countries:", sorted(df["Country Name"].unique()))
    print("Number of indicators:", df["Series Name"].nunique())
    print("Indicators:")
    for ind in sorted(df["Series Name"].unique()):
        print(" -", ind)
    
    # Core checks (Milestone 3 requirement)
    expected_rows = 792
    expected_indicators = 12
    expected_countries = 6
    
    print("\n--- Validation Checks ---")
    checks = []
    
    rows_ok = len(df) == expected_rows
    print(f"{'✓' if rows_ok else '✗'} Total observations: {len(df)} (expected {expected_rows})")
    checks.append(rows_ok)
    
    ind_ok = df["Series Name"].nunique() == expected_indicators
    print(f"{'✓' if ind_ok else '✗'} Indicators: {df['Series Name'].nunique()} (expected {expected_indicators})")
    checks.append(ind_ok)
    
    country_ok = df["Country Name"].nunique() == expected_countries
    print(f"{'✓' if country_ok else '✗'} Countries: {df['Country Name'].nunique()} (expected {expected_countries})")
    checks.append(country_ok)
    
    year_ok = df["Year"].min() == 2014 and df["Year"].max() == 2024
    print(f"{'✓' if year_ok else '✗'} Year range: 2014-2024")
    checks.append(year_ok)
    
    # Known data gaps (documented in Milestone 1)
    argentina_inflation_missing = df[(df["Country Name"]=="Argentina") & (df["Series Name"].str.contains("Inflation")) & (df["Year"]<2018)]["Value"].isna().all()
    print(f"{'✓' if argentina_inflation_missing else '✗'} Argentina inflation missing before 2018 (as documented)")
    
    brazil_poverty_missing = df[(df["Country Name"]=="Brazil") & (df["Series Name"].str.contains("Poverty"))]["Value"].isna().all()
    print(f"{'✓' if brazil_poverty_missing else '✗'} Brazil poverty missing for all years (as documented)")
    
    if all(checks):
        print("\n✓ All core checks passed - dataset is valid for the app.")
    else:
        print("\n✗ Some checks failed - please review the dataset.")
        exit(1)

if __name__ == "__main__":
    main()
