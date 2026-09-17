import streamlit as st
st.title("About & Methodology")
st.markdown("""
**Economic Development in Latin America (2014–2024)**

- **Data source:** World Bank Open Data, World Development Indicators
- **Dataset:** 792 observations (6 countries × 12 indicators × 11 years), static CSV
- **Scope:** Descriptive only — no causal claims or forecasts
- **Known gaps:** Argentina inflation missing before 2018, Brazil poverty missing for all years, ends at 2024

Full methodology and documentation are in the GitHub repository and the White Paper.
Built with Streamlit, pandas and Plotly. Deployed on Streamlit Community Cloud.
""")
