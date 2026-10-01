Economic Development in Latin America (2014-2024) - Interactive App
A Streamlit web app to explore economic and social development across six Latin American countries using World Bank data. Built as the app phase of the Living Stones Foundation - Applied Data & Digital Innovation Lab (LATAM) project.

Live App: https://economic-development-latin-america-4kvxjbsczegme3lnpwsb5d.streamlit.app/
Repository: https://github.com/ManarMohammed78/economic-development-latin-america - single source of truth for code, dataset, documentation and configuration.

Overview
This app builds directly on the analysis phase (cleaned dataset, 16 insights and Power BI dashboard). It lets users compare 12 indicators for Argentina, Brazil, Chile, Colombia, Mexico and Peru between 2014 and 2024, without any predictive or causal claims. The analysis is descriptive only.

The MVP is deployed on Streamlit Community Cloud and ready for Foundation review.

MVP Features (Final)
Implemented and tested:

Overview page with headline KPIs and trend charts for GDP per capita, unemployment and inflation (Argentina inflation shown separately)
Social Development page with life expectancy, poverty rate (Brazil excluded) and school enrollment
Investment, Technology and Demographics page with FDI, internet access and population
Insights panel with 16 documented insights, browsable by theme (Economic Growth, Social Development, Investment Trends, Regional Comparison) - descriptive only
Data Table with filtered raw data, sortable columns and CSV export for filtered rows
About and Methodology page with data sources, indicators, methodology, limitations, cutoff and links to White Paper and documentation
Global filters (country, year range, indicator) with persistence across pages, and correct handling of missing data as "No data available"
Postponed (outside MVP, confirmed):

Urbanization and Access to Electricity (no insights, near full coverage, would add clutter)
15 additional data sources reviewed in Milestone 1
Live World Bank API updates (currently static CSV)
Forecasting or predictive features
User accounts or saved views
All Must Have features from Milestone 2 are present. No functionality was implemented differently from the approved scope.

Technology Stack
Frontend + Backend: Streamlit (single Python app)
Data: pandas - loads the cleaned CSV at runtime (no database for v1)
Visualization: Plotly
Hosting: Streamlit Community Cloud (deploys directly from GitHub)
Python: 3.11 (via runtime.txt)
Why this stack: the dataset is small (792 rows) and static, so loading it directly with pandas is the simplest and most reliable approach for the first version, as agreed in Milestone 2.

Data Source
World Bank Open Data - World Development Indicators (https://data.worldbank.org/)

12 indicators included:
GDP per capita (current US$) · GDP growth (annual %) · Inflation, consumer prices (annual %) · Foreign direct investment, net inflows (% of GDP) · Unemployment, total (% of total labor force) · Poverty headcount ratio at national poverty lines · Life expectancy at birth · School enrollment, secondary (% gross) · Population, total · Urban population (% of total population) · Individuals using the Internet (% of population) · Access to electricity (% of population)

Cleaned dataset: 
Latin_America_Economic_Development_Clean.csv

792 observations (6 countries × 12 indicators × 11 years)
Long format: Country Name, Country Code, Series Name, Series Code, Year, Value
Known gaps: Argentina inflation missing before 2018, Brazil poverty missing for all years, ends at 2024
Cutoff: 2014-2024.

Project Structure
text

economic-development-latin-america/
├── app.py                              # Main app with top navigation and global filters
├── data/
│   ├── Latin_America_Economic_Development_Clean.csv
│   └── raw/Latin_America_Economic_Development_WB_2014_2024 (1).xlsx
├── pages/
│   ├── 2_Social_Development.py
│   ├── 3_Investment_Technology_Demographics.py
│   ├── 4_Insights.py
│   ├── 5_Data_Table.py
│   └── 6_About.py
├── utils/
│   ├── data_loader.py
│   └── filters.py
├── .streamlit/config.toml
├── scripts/validate_dataset.py
├── docs/
│   ├── Milestone_3_Progress_Summary.md/pdf
│   ├── Milestone_4_Progress_Summary.md/pdf
│   ├── Economic Development White Paper .pdf
│   └── Economic_Development_Documentation.docx
├── notebooks/Latin_America_Economic_Development.ipynb
├── requirements.txt
├── runtime.txt
└── README.md
Setup and Run Instructions
1. Clone the repository
Bash

git clone https://github.com/ManarMohammed78/economic-development-latin-america.git
cd economic-development-latin-america
2. Create and activate a virtual environment
Bash

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
3. Install dependencies
Bash

pip install -r requirements.txt
4. Verify the dataset
Bash

python scripts/validate_dataset.py
You should see: 792 observations, 12 indicators and confirmation of the two known data gaps.

5. Run the app locally
Bash

streamlit run app.py
Then open the URL shown in the terminal (usually http://localhost:8501).

No database or API keys are needed for this version.

How the App Loads Data
The cleaned CSV is stored in data/ inside the repo
On startup, 
data_loader.py
 loads it once with pandas.read_csv() and caches it with @st.cache_data
Top filters (country, year range, indicator) filter the in-memory DataFrame - global via st.session_state
Missing values are left as NaN and shown in the UI as "No data available"
Plotly draws the charts from the filtered data
Limitations
Static dataset only (no live World Bank API in this MVP)
Descriptive analysis only; no causal claims or forecasting
Poverty data missing for Brazil throughout the period
Argentina inflation data unavailable before 2018
Deployment
Deployed on Streamlit Community Cloud:
Live URL: https://economic-development-latin-america-4kvxjbsczegme3lnpwsb5d.streamlit.app/
The app deploys automatically from the main branch. Any push to main triggers a redeploy.

Author
Manar Mohammed - Volunteer Data Analyst, Living Stones Foundation (LATAM Lab)

License
For educational and portfolio use.
