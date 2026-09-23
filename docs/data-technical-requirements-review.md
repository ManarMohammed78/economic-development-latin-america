# Data & Technical Requirements Review
Economic Development in Latin America — App Phase
Living Stones Foundation, Applied Data & Digital Innovation Lab (LATAM)

## Purpose

Before starting development on the app, I reviewed the project's objectives, the dataset I already built during the analysis phase, and the additional data sources shared for this next phase. The goal is to agree on the data and scope first, so development starts on solid ground.

I reviewed:
- The project White Paper
- The GitHub repository (README, project documentation, the Python notebook, the cleaned dataset, and the Power BI dashboard)
- The list of candidate LATAM databases and APIs shared for the app phase

## Objectives and Scope (from the White Paper)

The project's objective is to analyze the key factors influencing economic development in Latin America through a data-driven approach, to support data-informed decision-making. The scope covers selected economic and social indicators for the region, using World Bank Open Data as the primary source. The analysis is descriptive only, with no causal claims and no predictive or forecasting models.

The deliverables defined in the White Paper were a cleaned dataset, an EDA report, an interactive dashboard, an insights summary, and final documentation. It's worth noting the White Paper covers the analysis and dashboard phase only; it doesn't mention an app.

## The Existing Dataset

The analysis phase produced a cleaned, ready-to-use dataset:

| Property | Value |
|---|---|
| Source | World Bank Open Data, World Development Indicators |
| Countries | Argentina, Brazil, Chile, Colombia, Mexico, Peru (6) |
| Time range | 2014-2024 (11 years) |
| Indicators | 12 |
| Format | Long format (Country, Country Code, Series Name, Series Code, Year, Value) |
| Total data points | 792 (6 x 12 x 11) |
| Tools used | Python/pandas for cleaning and analysis, Power BI for the dashboard |

This dataset is static (a point-in-time export), already cleaned, and already the basis for 16 documented insights and a 3-page Power BI dashboard.

## Review of the Additional Databases

The Foundation also shared 15 additional sources as candidate data for the app. I checked each one directly, its documentation, coverage, and data format, rather than just going by the name:

| Source | Covers | Format / Access | Notes |
|---|---|---|---|
| World Bank Open Data API | Same 6 countries and same or more indicators as the current dataset | REST, JSON/XML, no key needed | The live version of the data already in use. A natural next step after the first version, to make the app refresh automatically instead of relying on a static file |
| CEPALSTAT (ECLAC) | 1,000+ regional indicators for all of LATAM and the Caribbean | REST API, XML, requires developer registration | Broader indicator set, but a different format than the current dataset, so it would need new integration work |
| Latin Macro Watch (IDB) | GDP, CPI, fiscal and external accounts for 26 LAC countries, monthly/quarterly/annual since 1990 | Open datasets, JSON | Adds higher-frequency data than the current annual figures. Useful for later depth, not needed for the first version |
| IDB Open Data | General catalog of IDB research datasets | Mixed formats, not one standardized series | Too unstructured to use directly |
| IMF DataMapper API | GDP, inflation, debt, unemployment, globally, 40+ indicators | REST, JSON, no key | Includes forward-looking projections, which conflicts with the project's descriptive-only scope. Any future use would need the projection years filtered out |
| ArgentinaDatos API | Argentina only, exchange rates and monthly inflation | REST, JSON, community-run, unofficial | More current Argentina inflation data than the annual World Bank figures, but single-country |
| BCRA / INDEC (Argentina) | Argentina only, official central bank and statistics data | Mostly web/report-based, no simple public API found | Harder to integrate directly |
| BrasilAPI | Brazil only, postal codes, banks, holidays, some indicators | REST, JSON | A general utility API, not primarily economic |
| Central Bank of Brazil (SGS) | Brazil only, 30,000+ time series (Selic rate, IPCA inflation, GDP, trade balance) | REST, JSON, well documented, free | Deep Brazil-specific data, but single-country |
| Central Bank of Chile (BDE) | Chile only, macro and financial indicators | Web service, requires registration | Single-country, extra setup |
| FINDIC (Chile) | Chile only, market figures (UF, UTM, currency rates, copper price) | REST, JSON | Financial-market data, not core development indicators |
| API-Colombia | Colombia only, mostly geographic and demographic reference data | REST, JSON | Limited economic content |
| INEGI Banco de Indicadores (Mexico) | Mexico only, official national indicators | SDMX-based API, requires a key | Solid official source, but Mexico-only with a different query structure |
| REST Countries API | Reference data (capitals, population, currencies, flags) for 250+ countries | REST, JSON, no key | Useful for interface details like flags and country names, not historical indicators |
| Latamverse (R package) | Wraps ArgentinaDatos, FINDIC, BrasilAPI, ColombiAPI, REST Countries, and World Bank (5 countries, no Mexico) | R package, not a standalone API | A convenience layer for R users, not a new data source |

None of these 15 sources cover all 6 project countries in one standardized, ready-to-use series the way the existing World Bank export does. The multi-country options (the World Bank's live API, CEPALSTAT, Latin Macro Watch, IMF DataMapper) are the more promising candidates for later expansion, since one integration would cover several countries at once. The national APIs each cover a single country in a different format, so using them now would mean repeating the integration work six times over.

## Recommended Indicators for the First Version

Based on the review above, I recommend using the 12 indicators from the existing cleaned dataset for the first version of the app. It's the only set that already covers all 6 countries in one consistent, cleaned format; none of the additional sources match that on their own.

| Indicator | Category | Use in the app |
|---|---|---|
| GDP per capita (current US$) | Core economic | Headline KPI and trend line per country |
| GDP growth (annual %) | Core economic | Shows year-over-year momentum or contraction, especially the 2020 shock |
| Inflation, consumer prices (annual %) | Core economic | Trend line, with Argentina shown separately due to its scale (see Data Quality below) |
| Foreign direct investment, net inflows (% of GDP) | Core economic | Investment trend, highlights the 2020 investor pullback |
| Unemployment (% of labor force) | Labor market | Trend line, highlights the 2020 spike and each country's recovery speed |
| Poverty headcount ratio (% of population, national lines) | Social development | Most-recent-available-year comparison, Brazil excluded (see Data Quality below) |
| Life expectancy at birth (years) | Social development | Trend line, highlights the 2019-2021 health shock |
| School enrollment, secondary (% gross) | Social development | Trend line, general development indicator |
| Population, total | Infrastructure/demographics | Context metric, country sizing |
| Urban population (% of total) | Infrastructure/demographics | Structural context |
| Internet access (% of population) | Infrastructure/demographics | Trend line, shows the region's "catch-up" growth pattern |
| Access to electricity (% of population) | Infrastructure/demographics | Context metric, mostly near-saturation already |

## Data Quality: Gaps, Inconsistencies, and Limitations

I confirmed these directly against the cleaned dataset (792 rows):

| Issue | Detail | What it means for the app |
|---|---|---|
| Poverty headcount ratio, largest gap | 26 of 66 country-year values are missing. Brazil has none at all (11 of 11 missing). Chile is missing 7 of 11, Mexico 6 of 11, Argentina 2 of 11. Colombia and Peru are complete | Exclude Brazil from poverty views entirely (as the existing dashboard does), and show "no data available" rather than 0 or a blank gap elsewhere |
| Argentina inflation, early years missing | 4 of 11 years missing (before 2018, not available in the source) | The chart should start Argentina's inflation series from 2018, with a visible note, not a silent gap |
| School enrollment, minor scattered gaps | 4 of 66 values missing (Argentina, Brazil, Colombia), likely reporting lag | Low impact; just show "no data" for that point |
| Argentina inflation, scale outlier | Reaches 219.9% in 2024, versus single digits or low teens for the other five countries | A shared linear axis would flatten every other country's trend. The app should keep Argentina separate, the way the existing dashboard does |
| Descriptive, not predictive | An explicit constraint from the White Paper and documentation | The app should not add forecasts, projections, or causal language, only what the data shows |
| The dataset is static | Data ends in 2024, it's not a live feed | The app should clearly label the "as of" date and not imply real-time data |

No other structural inconsistencies came up. The cleaning steps in the documentation (removing placeholder values, reshaping wide to long, checking for duplicates) are sound, and the resulting dataset is internally consistent.

## Proposed Scope for the First Version

What the first version should display, mirroring the structure already validated in the Power BI dashboard:

- Overview: headline KPI cards (GDP per capita, unemployment, inflation), GDP per capita trend, unemployment trend, and inflation trend (Argentina shown separately)
- Social Development: life expectancy trend, poverty rate by country (most recent available year, Brazil excluded), secondary school enrollment trend
- Investment, Technology and Demographics: FDI trend, internet access growth, population by country
- Insights panel: the 16 documented insights, browsable by theme
- Data table and export: the raw values behind any chart, with a CSV export option
- About/methodology page: links back to the White Paper and documentation, and states the descriptive-only scope and the data's "as of 2024" status

Core interactivity: a country filter (multi-select across the 6 countries), a year range filter (2014-2024), and an indicator selector.

Out of scope for now, kept as candidates for later:
- The 15 additional data sources reviewed above
- Forecasting or predictive features
- User accounts, saved views, or personalization
- Real-time or live data refresh

## Next Steps

1. Review this document and confirm or adjust the indicator list, the database review, and how missing data is handled.
2. Once agreed, move on to the technical structure (data layer, front-end approach, hosting) as a separate, smaller step.
