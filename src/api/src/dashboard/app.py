import streamlit as st, pandas as pd
from sqlalchemy import create_engine
from src.common.config import DB_URL

st.set_page_config(page_title="IntelOps Dashboard", layout="wide")
st.title("🔎 IntelOps Dashboard")

engine = create_engine(DB_URL, future=True)
df = pd.read_sql("SELECT ioc_type,value,source,last_seen,confidence FROM indicators ORDER BY last_seen DESC", engine)

c1,c2,c3 = st.columns(3)
c1.metric("Indicadores", len(df))
c2.metric("Fuentes", df["source"].nunique())
c3.metric("Tipos IoC", df["ioc_type"].nunique())

st.bar_chart(df.groupby("source")["value"].nunique())
st.bar_chart(df.groupby("ioc_type")["value"].nunique())

src = st.selectbox("Filtrar por fuente", ["Todas"] + sorted(df["source"].unique()))
if src != "Todas":
    df = df[df["source"]==src]

st.dataframe(df, use_container_width=True, height=480)
