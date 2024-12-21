import os

import altair as alt
import pandas as pd
import psycopg2
import streamlit as st
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Lê as variáveis separadas do arquivo .env (sem SSL)
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")


def ler_dados_postgres():
    """Load data from PostgreSQL and return as DataFrame."""
    try:
        conn = psycopg2.connect(
            host=POSTGRES_HOST,
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            port=POSTGRES_PORT,
        )
        query = "SELECT * FROM bitcoin_price WHERE fiat_currency = 'USD' ORDER BY timestamp DESC"
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Error connecting to PostgreSQL: {e}")
        return pd.DataFrame()


def main():
    st.set_page_config(page_title="Bitcoin Price Dashboard", layout="wide")
    st.title("📊 Bitcoin Price Dashboard")
    st.write(
        "This dashboard displays Bitcoin price data collected periodically from a PostgreSQL database."
    )

    df = ler_dados_postgres()

    if not df.empty:
        st.subheader("📋 Dados Recentes")
        st.dataframe(df)

        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.sort_values(by="timestamp")

        st.subheader("📈 Bitcoin Price Timeline Evolution")
        # st.line_chart(data=df, x="timestamp", y="price", use_container_width=True)
        chart_data = (
            alt.Chart(df)
            .mark_line()
            # .encode(x="timestamp", y="price")
            .encode(
                alt.X("timestamp", axis=alt.Axis(title="Time line")),
                alt.Y(
                    "price",
                    axis=alt.Axis(title="Price"),
                    scale=alt.Scale(
                        domain=[
                            df["price"].min() * 0.99,
                            df["price"].max() * 1.01,
                        ]
                    ),
                ),
            )
            .properties(width=600, height=400)
        )
        st.altair_chart(chart_data, use_container_width=True)

        st.subheader("🔢 General Statistics")
        col1, col2, col3 = st.columns(3)
        col1.metric("Current Price", f"${df['price'].iloc[-1]:,.2f}")
        col2.metric("Max Price", f"${df['price'].max():,.2f}")
        col3.metric("Min Price", f"${df['price'].min():,.2f}")
    else:
        st.warning("No data found in PostgreSQL database.")


if __name__ == "__main__":
    main()
