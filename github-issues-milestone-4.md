# GitHub Issues for Milestone 4

Created for the Economic Development in Latin America app, based on MVP features and wireframes from Milestone 2. Each issue is specific enough to track and assign. Copy these directly into GitHub Issues.

---

### Issue #1: Build Overview Page (Home) — Headline KPIs and Trends
**Labels:** `enhancement`, `Milestone 4`, `page: overview`
**Description:**
Create `pages/1_Overview.py` with headline numbers and trend charts for GDP per capita, unemployment and inflation (as per wireframe).

Tasks:
- Show latest year values (2024) for the three indicators for selected countries
- Add trend line charts (Plotly) with country filter applied
- Handle Argentina inflation separately when needed (scale note)
- Keep filters (country, year range) synced via sidebar
**Acceptance:** Charts update immediately when filters change; missing data shown as "No data available".

---

### Issue #2: Build Social Development Page
**Labels:** `enhancement`, `Milestone 4`, `page: social`
**Description:**
Create `pages/2_Social_Development.py` for life expectancy, poverty rate and school enrollment.

Tasks:
- Line chart for life expectancy (highlight 2019–2021 drop)
- Poverty chart for most recent year only, Brazil excluded with note
- School enrollment trend chart
- Same country/year filters
**Acceptance:** Poverty chart correctly excludes Brazil; tooltip shows exact value, country and year.

---

### Issue #3: Build Investment, Technology and Demographics Page
**Labels:** `enhancement`, `Milestone 4`, `page: investment`
**Description:**
Create `pages/3_Investment_Technology_Demographics.py` with FDI, internet access and population.

Tasks:
- FDI trend (% of GDP) chart
- Internet access growth trend chart
- Population context chart/table
**Acceptance:** All three charts respect shared filters.

---

### Issue #4: Implement Global Filters and Missing Data Handling
**Labels:** `enhancement`, `Milestone 4`, `filters`
**Description:**
Centralize the sidebar filters so they persist across pages (country multi-select, year range slider, indicator selector).

Tasks:
- Use `utils/data_loader.py` cached loader
- Ensure missing values are never shown as zero — show "No data available" caption
- Show note for Argentina inflation (<2018) and Brazil poverty gaps
**Acceptance:** Switching pages keeps filters; no zero filling.

---

### Issue #5: Insights Panel (Browse 16 Documented Insights by Theme)
**Labels:** `enhancement`, `Milestone 4`, `nice-to-have`
**Description:**
Create `pages/4_Insights.py` to display the 16 insights from the analysis phase, browsable by theme (Crisis, Outliers, Long-term trends).

Tasks:
- Store insights as list/dict with theme tag
- Add theme filter and searchable list
**Acceptance:** User can filter insights by theme.

---

### Issue #6: Data Table View with Sort and Filter Sync
**Labels:** `enhancement`, `Milestone 4`, `page: table`
**Description:**
Create `pages/5_Data_Table.py` showing the raw filtered rows behind any chart.

Tasks:
- Display `filtered` DataFrame with sortable columns (Streamlit dataframe)
- Keep synced with sidebar filters
**Acceptance:** Sorting by column header works; table matches current chart filter.

---

### Issue #7: CSV Export for Filtered Data
**Labels:** `enhancement`, `Milestone 4`, `export`
**Description:**
Add "Export CSV" button that downloads exactly the rows currently shown after filtering.

Tasks:
- Add `st.download_button` in table page and optionally on each chart page
- Filename: `filtered_data.csv`
**Acceptance:** Exported file contains only filtered rows.

---

### Issue #8: About and Methodology Page
**Labels:** `documentation`, `Milestone 4`, `page: about`
**Description:**
Create `pages/6_About_Methodology.py` with project info, data source, methodology and links back to White Paper and documentation docs.

Tasks:
- Include data source (World Bank), 792 rows / 12 indicators, limitations, and link to GitHub docs
- Add note that analysis is descriptive only (no forecasts)
**Acceptance:** Page links correctly and lists limitations from Milestone 1.

---

### Issue #9: Navigation and Layout Polish
**Labels:** `enhancement`, `Milestone 4`, `UX`
**Description:**
Ensure consistent navigation bar across all pages and that layout matches low-fidelity wireframes.

Tasks:
- Test navigation between pages keeps filter state
- Check hover tooltips show exact value, country and year
**Acceptance:** Navigation works without resetting filters.

---

### How to create them on GitHub
1. Go to the repo → Issues → New Issue
2. Copy Title and Description above
3. Add labels
4. Create. For bulk creation, you can also use the GitHub CLI:
```bash
gh issue create --title "Build Overview Page (Home) — Headline KPIs and Trends" --body "..." --label "enhancement,Milestone 4"
```

All issues are tied to the MVP defined in Milestone 2 and ready for Milestone 4 development.
