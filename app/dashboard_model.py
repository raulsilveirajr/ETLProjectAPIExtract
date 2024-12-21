import time
from datetime import datetime

import pandas as pd
import streamlit as st

# 1) st.title - Main title
st.title("🚀 Quick Starter Streamlit - Data Engineering Journey")

# 2) st.header - Section
st.header("1. Data Engineering Context")

# 3) st.write - Simple text
st.write(
    """
    This dashboard simulates some elements you would use in a Data Engineering project:
    - Data collection/extraction
    - Transformation and cleaning
    - Visualization of metrics
    - Monitoring of pipelines
    """
)

# 4) st.markdown - Markdown text
st.markdown(
    """
### Topics Covered:
- **Widget creation** for parameter collection
- **DataFrames display** (part of "Transform")
- **Charts** to monitor performance and throughput
- **Metrics** representing ETL pipeline KPIs
"""
)

st.header("2. Pipeline Parameters")

# 5) st.text_input - Text parameter
pipeline_name = st.text_input("Pipeline Name", value="Pipeline Bitcoin Ingestion")

# 6) st.number_input - Number parameter
batch_size = st.number_input(
    "Batch size (lines per ingestion):",
    min_value=100,
    max_value=100000,
    value=1000,
    step=100,
)

# 7) st.slider - Continuous selector
max_latency = st.slider(
    "Maximum Latency (seconds):", min_value=1, max_value=30, value=5
)

# 8) st.selectbox - Select pipeline
pipeline_type = st.selectbox(
    "Pipeline Type:", ["Batch", "Streaming", "Lambda", "Kappa"]
)

# 9) st.multiselect - Multiple choice of processing layers
layers = st.multiselect(
    "Which layers are involved in the pipeline?",
    ["Raw", "Staging", "Trusted", "Analytics", "Sandbox", "Dimensão", "Fato"],
    default=["Raw", "Staging"],
)

# 10) st.checkbox - Check to simulate log activation
activate_logs = st.checkbox("Activate Execution Logs")

st.header("3. Data Display (Transform)")

# 11) Create a fictitious dataset about "pipeline executions"
executions_data = {
    "data_execucao": pd.date_range(end=datetime.now(), periods=5, freq="H"),
    "status": ["Success", "Success", "Failure", "Success", "Success"],
    "processed_lines": [1000, 1200, 900, 1500, 1300],
    "execution_time_sec": [4.2, 5.1, 7.8, 3.9, 4.5],
}
df_executions = pd.DataFrame(executions_data)

# 12) st.dataframe - Interactive table
st.subheader("Recent Pipeline Executions")
st.dataframe(df_executions)

# 13) st.table - Static table
st.subheader("Static Table - Latest Executions")
st.table(df_executions)

# 14) st.metric - Display KPIs metrics
st.subheader("Performance Indicators (KPIs)")
col1, col2, col3 = st.columns(3)
col1.metric("Total of Lines Processed", f"{df_executions['processed_lines'].sum():,}")
col2.metric(
    "Success Executions",
    str(df_executions["status"].value_counts().get("Success", 0)),
)
col3.metric(
    "Failure Executions", str(df_executions["status"].value_counts().get("Failure", 0))
)

st.header("4. Chart Display (Monitor)")

# 15) st.line_chart - Line chart with metrics
st.subheader("Lines Processed per Execution (Line Chart)")
df_ordered_executions = df_executions.sort_values(by="data_execucao")
st.line_chart(data=df_ordered_executions, x="data_execucao", y="processed_lines")

# 16) st.bar_chart - Bar chart
st.subheader("Execution Time per Data (Bar Chart)")
st.bar_chart(data=df_ordered_executions, x="data_execucao", y="execution_time_sec")

st.header("5. Other Useful Resources")

# 17) st.date_input - Date selector
planned_start_date = st.date_input("Start date for new pipeline", datetime.now())

# 18) st.progress - Progress bar (simulation)
st.write("Loading log data...")
progress_bar = st.progress(0)
for i in range(101):
    time.sleep(0.01)
    progress_bar.progress(i)

# 19) Success/error messages
if activate_logs:
    st.success("Execution logs are active.")
else:
    st.warning("Execution logs are inactive.")

# 20) st.button - Button to simulate pipeline trigger
if st.button("Trigger New Execution"):
    st.info(f"Pipeline '{pipeline_name}' triggered in {pipeline_type} mode.")
    st.write(
        f"Batch size configured for {batch_size} lines. Maximum Latency: {max_latency}s"
    )
    st.write(f"Selected layers: {', '.join(layers)}")

st.markdown("___")
st.caption("Quick Starter of Streamlit applied to Data Engineering. © 2024")
