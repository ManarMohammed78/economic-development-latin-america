# Economic Development in Latin America (2014–2024)

A data analysis project examining economic growth, resilience, and social development across six Latin American economies, using World Bank Open Data. Completed as a volunteer Data Analyst project with the Living Stones Foundation's Applied Data & Digital Innovation Lab (LATAM).

## Overview

This project analyzes 12 economic and social indicators across Argentina, Brazil, Chile, Colombia, Mexico, and Peru between 2014 and 2024 (792 data points total), to identify patterns in regional economic development, crisis response, and long-term structural trends.

The analysis is descriptive, not predictive. It identifies correlations and patterns in the data; it does not model or forecast future outcomes.

## Contents

| File | Description |
|---|---|
| Latin_America_Economic_Development.ipynb | Full Python analysis: data cleaning, exploratory data analysis, and 16 documented insights |
| Latin_America_Economic_Development_WB_2014_2024.xlsx | Raw dataset, sourced directly from the World Bank Data Bank |
| Economic_Development_Documentation.docx | Full project documentation: methodology, data cleaning decisions, key findings, and limitations |
| Economic_Development_LatinAmerica_PitchDeck.pptx | Project presentation summarizing the objective, methodology, and key findings |

## Data Source

World Bank Open Data – World Development Indicators (https://data.worldbank.org/), covering:
GDP per capita · GDP growth · Unemployment · Inflation · Life expectancy · Secondary school enrollment · Poverty headcount ratio · Foreign direct investment (FDI) · Population · Urban population · Internet access · Electricity access

## Tools

- Python (pandas, in Google Colab) — data cleaning and exploratory analysis
- Power BI — interactive dashboard (3 pages: Overview, Social Development, Investment/Technology/Demographics)

## Key Findings (Summary)

- All six countries experienced a synchronized GDP per capita decline in 2020 (–9.5% to –21.7%), alongside rising unemployment, falling life expectancy, and reduced FDI, indicating a genuine multi-dimensional regional crisis rather than an isolated economic dip.
- Argentina's inflation followed a separate, accelerating trajectory, from ~34% (2018) to 219.9% (2024), aligned with the highest GDP volatility in the dataset.
- Chile consistently outperformed the other five countries across nearly every indicator: highest GDP per capita, highest FDI inflow, lowest poverty rate, and the smallest life expectancy decline during 2019–2021.
- Population growth showed no consistent relationship with economic performance across the six countries.

Full methodology, data cleaning decisions, and all 16 insights are documented in Economic_Development_Documentation.docx.

## Limitations

- Descriptive analysis only; no causal claims or predictive modeling.
- Poverty data is incomplete for three countries, and unavailable for Brazil throughout the full period (explained in the documentation).
- Argentina's inflation data is unavailable before 2018 in the source dataset.

## Author

Manar Mohammed
Volunteer Data Analyst, Living Stones Foundation — Applied Data & Digital Innovation Lab (LATAM)
