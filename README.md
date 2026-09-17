# Economic Development in Latin America (2014–2024) — Interactive App

A Streamlit web app to explore economic and social development across six Latin American countries using World Bank data. Built as the app phase of the Living Stones Foundation — Applied Data & Digital Innovation Lab (LATAM) project.

This repository is the single source of truth for the application code, dataset, documentation and configuration.

## Overview

This app builds directly on the analysis phase (cleaned dataset, 16 insights and Power BI dashboard). It lets users compare 12 indicators for Argentina, Brazil, Chile, Colombia, Mexico and Peru between 2014 and 2024, without any predictive or causal claims.

The analysis is descriptive only. The app shows what happened in the data and handles known gaps transparently.

## MVP Scope

**Must have (Milestone 4):**
- Overview page with headline numbers and trend charts for GDP per capita, unemployment and inflation
- Social Development page (life expectancy, poverty rate, school enrollment)
- Investment, Technology and Demographics page (FDI, internet access, population)
- Country filter, year range filter and indicator selector
- Correct handling of missing data — shown as "No data available" rather than zero
- Argentina inflation shown separately due to scale difference

**Nice to have:**
- Insights panel with the 16 documented insights, browsable by theme
- Data table view with sortable columns
- CSV export for filtered rows
- About and Methodology page linking back to White Paper and documentation

**Postponed (later phase):**
- 15 additional data sources reviewed in Milestone 1
- Live World Bank API updates (currently static CSV)
- Forecasting or predictive features
- User accounts or saved views

## Technology Stack

- **Frontend + Backend:** Streamlit (single Python app, no separate backend)
- **Data:** pandas — loads the cleaned CSV at runtime (no database for v1)
- **Visualization:** Plotly (via Streamlit)
- **Hosting:** Streamlit Community Cloud (deploys directly from GitHub)
- **Python:** 3.10+

Why this stack: the dataset is small (792 rows) and static, so loading it directly with pandas is the simplest and most reliable approach for the first version. This is the architecture agreed in Milestone 2.

## Data Source

World Bank Open Data — World Development Indicators (https://data.worldbank.org/)

12 indicators included:
GDP per capita (current US$) · GDP growth (annual %) · Inflation, consumer prices (annual %) · Foreign direct investment, net inflows (% of GDP) · Unemployment, total (% of total labor force) · Poverty headcount ratio at national poverty lines · Life expectancy at birth · School enrollment, secondary (% gross) · Population, total · Urban population (% of total population) · Individuals using the Internet (% of population) · Access to electricity (% of population)

Cleaned dataset: `data/Latin_America_Economic_Development_Clean.csv`
- 792 observations (6 countries × 12 indicators × 11 years)
- Long format: Country Name, Country Code, Series Name, Series Code, Year, Value
- Known gaps documented in Milestone 1: Argentina inflation missing before 2018, Brazil poverty missing for all years, ends at 2024

## Project Structure

```
economic-development-latin-america/
├── app.py                              # Main Streamlit app entry point
├── data/
│   └── Latin_America_Economic_Development_Clean.csv  # Cleaned dataset (792 rows)
├── pages/
│   ├── 1_Overview.py                   # Overview: GDP, unemployment, inflation
│   ├── 2_Social_Development.py         # Life expectancy, poverty, school enrollment
│   ├── 3_Investment_Technology_Demographics.py
│   ├── 4_Insights.py
│   ├── 5_Data_Table.py
│   └── 6_About_Methodology.py
├── utils/
│   └── data_loader.py                  # Cached pandas loader + validation
├── .streamlit/
│   └── config.toml                     # Theme and server config
├── scripts/
│   └── validate_dataset.py             # Checks 792 rows / 12 indicators
├── docs/
│   ├── Milestone_3_Progress_Summary.md
│   ├── github-issues-milestone-4.md
│   └── branching-workflow.md
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/ManarMohammed78/economic-development-latin-america.git
cd economic-development-latin-america
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Verify the dataset
```bash
python scripts/validate_dataset.py
```
You should see: `792 observations, 12 indicators` and confirmation of the two known data gaps.

### 5. Run the app locally
```bash
streamlit run app.py
```
Then open the URL shown in the terminal (usually http://localhost:8501).

No database or API keys are needed for this version.

## How the App Loads Data

1. The cleaned CSV is stored in `data/` inside the repo
2. On startup, `utils/data_loader.py` loads it once with `pandas.read_csv()` and caches it with `@st.cache_data`
3. Sidebar filters (country, year, indicator) filter the in-memory DataFrame — no reload
4. Missing values are left as NaN and shown in the UI as "No data available"
5. Plotly draws the charts from the filtered data

## Branching Workflow

See `docs/branching-workflow.md` for the full workflow. In short: `main` is always deployable, work happens on `feature/*` branches, merged via pull requests.

## Deployment

The app is configured for Streamlit Community Cloud:
1. Push to `main` on GitHub
2. Connect the repo in https://share.streamlit.io
3. Set main file to `app.py`

## Limitations

- Static dataset only (no live World Bank API in v1)
- Wireframes are low-fidelity; colors and mobile layout to be finalized in design phase
- Streamlit Community Cloud is a free tier

## Author

Manar Mohammed — Volunteer Data Analyst, Living Stones Foundation (LATAM Lab)
Link to analysis phase files: `Latin_America_Economic_Development.ipynb`, `Economic_Development_Documentation.docx`

## License

For educational and portfolio use.
