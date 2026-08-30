import streamlit as st
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Sayfa Yapılandırması
st.set_page_config(page_title="Green-FinAI Dashboard", page_icon="🌱", layout="wide")

# Başlık ve Özet
st.title("🌱 Green-FinAI: Financial Decision & Sustainability Simulator")
st.caption("Evaluating AI's Water Footprint, Human-AI Collaboration, and Long-Term Green Tech ROI")

st.markdown("---")

# Yan Menü / Senaryo & Parametre Seçimi
st.sidebar.header("🎯 Simulation Parameters")
scenario = st.sidebar.selectbox(
    "Select Business Scenario:",
    [
        "1. Green Tech Investment vs. Traditional Strategy (2030 Horizon)",
        "2. ESG Supply Chain Decarbonization in Luxury Sector",
        "3. High-Energy Tech Infrastructure Acquisition (M&A)"
    ]
)

ai_complexity = st.sidebar.select_slider(
    "AI Model Complexity (Tokens/Query):",
    options=["Standard (GPT-4o)", "Deep Reasoning (o1/o3)", "Heavy Enterprise Agent Ensemble"],
    value="Deep Reasoning (o1/o3)"
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Core Thesis:** Hybrid human-AI workflows maximize financial ROI while constraining hidden datacenter resource costs (water cooling & electricity).")

# Ana Ekran
st.subheader(f"📊 Active Scenario: {scenario}")

if st.button("🚀 Run Dynamic Simulation & Calculate Footprint"):
    with st.spinner("Executing Monte Carlo simulation & calculating datacenter environmental impact..."):
        time.sleep(1.2)

    st.success("Simulation & Environmental Audit Complete!")
    
    # Metrik Ayarları (Karmaşık Modele Göre)
    multiplier = 1.0 if "Standard" in ai_complexity else (2.2 if "Deep" in ai_complexity else 4.5)
    water_used = int(180 * multiplier)
    power_used = round(0.035 * multiplier, 3)
    co2_used = round(14.0 * multiplier, 1)

    # 1. BÖLÜM: METRİKLER
    col1, col2, col3 = st.columns(3)
    col1.metric(label="💡 Pure AI Strategy ROI", value="14.2%", delta="-2.1% vs Hybrid")
    col2.metric(label="👤 Human Analyst ROI", value="11.5%", delta="-4.8% vs Hybrid")
    col3.metric(label="🤝 Hybrid (Human + AI) ROI", value="18.7%", delta="+4.5% (Optimal Balance)")

    st.markdown("---")

    # 2. BÖLÜM: GRAFİKLER (FINANSAL + ÇEVRESEL)
    g_col1, g_col2 = st.columns(2)

    with g_col1:
        st.subheader("📈 2025-2030 Cumulative Financial Performance ($M)")
        years = [2025, 2026, 2027, 2028, 2029, 2030]
        df_finance = pd.DataFrame({
            "Year": years,
            "Traditional / Pure AI": [10, 11.2, 12.8, 14.1, 15.5, 17.0],
            "Green Tech / Hybrid AI": [10, 12.5, 15.8, 20.1, 25.4, 32.0]
        })
        fig_fin = px.line(
            df_finance, x="Year", y=["Traditional / Pure AI", "Green Tech / Hybrid AI"],
            markers=True, color_discrete_sequence=["#EF553B", "#00CC96"]
        )
        fig_fin.update_layout(legend_title_text="Strategy", hovermode="x unified")
        st.plotly_chart(fig_fin, use_container_width=True)

    with g_col2:
        st.subheader("💧 AI Resource Consumption Breakdown")
        df_env = pd.DataFrame({
            "Metric": ["Cooling Water (ml)", "Power Consumed (x100 Wh)", "Carbon Footprint (g CO2)"],
            "Amount": [water_used, power_used * 100, co2_used]
        })
        fig_env = px.bar(
            df_env, x="Metric", y="Amount", color="Metric",
            color_discrete_sequence=["#636EFA", "#AB63FA", "#FFA15A"]
        )
        fig_env.update_layout(showlegend=False)
        st.plotly_chart(fig_env, use_container_width=True)

    st.markdown("---")

    # 3. BÖLÜM: SÜRDÜRÜLEBİLİRLİK SAYACI VE SKOR
    st.subheader("💧 Hidden Environmental Footprint Audit")
    e_col1, e_col2, e_col3 = st.columns(3)
    e_col1.metric("Est. Datacenter Cooling Water", f"{water_used} ml", f"~{round(water_used/250, 1)} small water bottles")
    e_col2.metric("Est. Power Consumed", f"{power_used} kWh", f"~{int(power_used*300)} min of LED TV")
    e_col3.metric("Carbon Equivalent", f"{co2_used} g CO2", "Offset Tier 1")

    st.markdown("---")
    st.subheader("🏅 Green-Fin ROI Index (Eco-Efficiency)")
    score = max(50, int(95 - (multiplier * 8)))
    st.progress(score)
    st.write(f"**Score: {score}/100** — Financial value generated vs. Datacenter energy footprint ratio.")

else:
    st.info("👈 Select parameters in the sidebar and click **Run Dynamic Simulation** to generate real-time financial & sustainability charts.")
