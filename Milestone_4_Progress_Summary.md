# Milestone 4 Progress Summary
## Dashboard Implementation, Economic Development in Latin America (App Phase)

**Summary of work completed for Milestone 4, based on the tasks defined for this milestone.**

---

### 1. Dashboard Foundation - Navigation and Global Filters

Built the dashboard foundation that supports all six pages. The structure follows the six wireframes agreed in Milestone 2 and the project setup from Milestone 3.

*   Set up dashboard navigation and page structure with a main Overview page and five pages in the pages folder. The navigation matches the wireframe top bar: Overview, Social Dev, Invest and Tech, Insights, Data Table, About. Streamlit multipage navigation handles switching while keeping the layout consistent.
*   Implemented country selector as a multiselect with all six countries selected by default. Implemented year range selector as a slider from 2014 to 2024. Implemented indicator selector as a selectbox with all 12 World Bank indicators.
*   Implemented global filter behavior using st.session_state. The selected countries, year range and indicator are stored in session state, so when a user switches pages the filters stay the same. This matches the requirement that filters behave consistently across pages.
*   Implemented missing data handling. Missing values are never shown as zero. They are shown as No data available with an info message. This covers the two documented gaps: Argentina inflation before 2018 and Brazil poverty for all years, plus the 2024 cutoff. The logic is centralized in utils/filters.py and used by every page.

### 2. Overview Page - Home

Built the Overview page as the home page, matching the wireframe Home and Overview layout.

*   Implemented headline KPIs for GDP per capita, unemployment and inflation. The cards show the latest year value in the selected range, averaged across the selected countries. If no data is available the card shows No data.
*   Implemented GDP per capita trend as a line chart with Plotly, with one line per selected country and markers for each year.
*   Implemented unemployment trend as a line chart, same interaction as the GDP chart.
*   Implemented inflation trend as a full width line chart. Argentina is shown separately where needed. When Argentina is selected with other countries a note explains that its scale is much higher, matching the wireframe note Inflation trend Argentina shown separately.
*   All charts show hover tooltips with exact value, country and year. This is GitHub Issue 1.

### 3. Social Development Page

Built the Social Development page matching the wireframe with two charts on top and one full width chart below.

*   Implemented life expectancy trend as a line chart across the selected year range, one line per country, showing the 2019 to 2021 change.
*   Implemented poverty rate by country as a bar chart for the latest year in the selected range. Brazil is excluded from this chart for all years, as documented in Milestone 1, with a caption explaining the exclusion. This handles the missing Brazil poverty data requirement.
*   Implemented secondary school enrollment trend as a full width line chart, showing the general development trend. This is GitHub Issue 2.

### 4. Investment, Technology and Demographics Page

Built the Investment and Technology page matching the wireframe with two charts on top and one bar chart below.

*   Implemented foreign direct investment trend as a line chart, showing net inflows as percent of GDP over time.
*   Implemented internet access growth as a line chart, showing the regional growth trend for individuals using the Internet.
*   Implemented population by country as a bar chart for the latest year, showing country size context.
*   Urbanization and electricity are shown only if confirmed as part of the approved MVP page. As defined in Milestone 2 these are marked as postponed for the first version, so the page keeps population as the main demographic chart and notes the postponed items. This is GitHub Issue 3.

### 5. Insights Panel

Built the Insights panel to display the 16 documented insights, organized by theme, with descriptive only content.

*   Implemented the 16 documented insights from the analysis phase. Each insight is stored with a theme tag.
*   Organized insights by theme with a theme filter in the sidebar. Themes are Economic Growth, Social Development, Investment Trends and Regional Comparison. The filter defaults to All.
*   Kept insights descriptive. No causal or predictive claims are made, matching the project scope from the White Paper. Each insight card notes that it is descriptive only.
*   The layout follows the wireframe with a grid of cards, two per row, each showing the theme and the finding. This is GitHub Issue 5.

### 6. Data Table and CSV Export

Built the Data Table page with sorting, filtering sync and CSV export, matching the wireframe.

*   Display filtered raw data in a table that shows Country, Indicator, Year and Value. The table uses Streamlit dataframe which allows sorting by clicking the column header.
*   Synced the table with dashboard filters. The table shows exactly the rows for the selected countries, year range and indicator, the same filters used for the charts.
*   Implemented export of filtered data as CSV with a download button. The button downloads only the currently filtered rows, with the file name filtered_data.csv. This covers GitHub Issues 6 and 7.

### 7. About and Methodology Page

Built the About and Methodology page with all required documentation, matching the wireframe with text sections and two link buttons.

*   Added data sources: World Bank Open Data, World Development Indicators, with the link https://data.worldbank.org.
*   Listed the 12 indicators included in the app, same list as in the README and Milestone 1.
*   Described the methodology: cleaning with Python pandas in Google Colab, 792 observations from 2014 to 2024, long format with six fields, loading with pandas and st.cache_data, filtering in memory.
*   Listed limitations: descriptive only, no causal or predictive claims, poverty data missing for Brazil, Argentina inflation missing before 2018, dataset ends at 2024.
*   Added the 2014 to 2024 cutoff note, missing data notes, descriptive only scope note, and links to the White Paper and project documentation. The page has two buttons: Link White Paper and Link Documentation. This is GitHub Issue 8.

### 8. Navigation and Layout Polish

Refined navigation and layout to ensure consistency across all pages, matching the final wireframe polish task.

*   Refined navigation so the top bar is the same on all six pages and switching pages keeps the selected filters.
*   Ensured consistent page layout with the same filter placement at the top, same chart heights and spacing, following the wireframe structure.
*   Ensured filters behave consistently across pages using the centralized global filter logic. Hover tooltips show exact value, country and year on every chart.
*   Applied the agreed UI and layout decisions from Milestone 2. Colors and branding are kept simple for this version, as noted in the technical decisions. This is GitHub Issue 9.

---

Manar Mohammed, Volunteer Data Analyst, Living Stones Foundation LATAM Lab | September 2026

All pages match the six wireframes provided for Milestone 2 and the tasks for Milestone 4. The app is ready for review and can be run locally with streamlit run app.py and deployed to Streamlit Community Cloud.
