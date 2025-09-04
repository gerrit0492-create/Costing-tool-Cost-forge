from __future__ import annotations
import streamlit as st
import pandas as pd
from utils.safe import guard

def main():
    st.title("💸 Quick Cost Check")
    mats = pd.read_csv("data/materials_db.csv")
    procs = pd.read_csv("data/processes_db.csv")
    bom = pd.read_csv("data/bom_template.csv")

    st.subheader("Materials")
    st.dataframe(mats)
    st.subheader("Processes")
    st.dataframe(procs)
    st.subheader("BOM")
    st.dataframe(bom)

    df = bom.merge(mats, on="material_id", how="left")             .merge(procs, left_on="process_route", right_on="process_id", how="left")

    df["material_cost"] = df["mass_kg"] * df["price_eur_per_kg"]
    df["process_cost"] = df["runtime_h"] * (df["machine_rate_eur_h"] + df["labor_rate_eur_h"])
    df["overhead"] = (df["material_cost"] + df["process_cost"]) * df["overhead_pct"]
    df["base_cost"] = df["material_cost"] + df["process_cost"] + df["overhead"]
    df["margin"] = df["base_cost"] * df["margin_pct"]
    df["total_cost"] = df["base_cost"] + df["margin"]

    st.subheader("Calculated costs")
    st.dataframe(df[["material_id","qty","material_cost","process_cost","overhead","margin","total_cost"]])

    st.metric("📦 Offer total (EUR)", f"{df['total_cost'].sum():,.2f}")

guard(main)
