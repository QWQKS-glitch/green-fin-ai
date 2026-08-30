import streamlit as st
import time

# Sayfa Yapılandırması
st.set_page_config(page_title="Green-FinAI Dashboard", page_icon="🌱", layout="wide")

# Başlık ve Özet
st.title("🌱 Green-FinAI: Financial Decision & Sustainability Simulator")
st.caption("Evaluating AI's Water Footprint, Human-AI Collaboration, and Long-Term Green Tech ROI")

st.markdown("---")

# Yan Menü / Senaryo Seçimi
st.sidebar.header("🎯 Business Scenario Selection")
scenario = st.sidebar.selectbox(
    "Choose a Scenario to Simulate:",
    [
        "1. Green Tech Investment vs. Traditional Strategy (2030 Horizon)",
        "2. ESG Supply Chain Decarbonization in Luxury Sector",
        "3. High-Energy Tech Infrastructure Acquisition (M&A)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Project Goal:** Demonstrate that hybrid human-AI decisions optimize financial returns while tracking hidden environmental costs (water & power).")

# Ana Ekran
st.subheader(f"📊 Running Simulation for: {scenario}")

if st.button("🚀 Run Analysis & Calculate Footprint"):
    with st.spinner("Processing financial models & calculating datacenter water/power usage..."):
        time.sleep(1.5) # Simülasyon hissi için kısa bekleme

    st.success("Analysis Complete!")
    
    # 3 Sütunlu Metrik Alanı
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="💡 Pure AI Strategy ROI", value="14.2%", delta="-2.1% (Lacks Human Context)")
    with col2:
        st.metric(label="👤 Human Analyst ROI", value="11.5%", delta="-4.8% (Slower Adaptation)")
    with col3:
        st.metric(label="🤝 Hybrid (Human + AI) ROI", value="18.7%", delta="+4.5% (Optimal Balance)")

    st.markdown("---")
    
    # Sürdürülebilirlik Sayaçları (Sütun B)
    st.subheader("💧 Hidden Environmental Footprint of this AI Query")
    
    e_col1, e_col2, e_col3 = st.columns(3)
    e_col1.metric("Est. Cooling Water Used", "240 ml", "approx. 1 small bottle")
    e_col2.metric("Est. Power Consumed", "0.045 kWh", "15 LED bulbs / 1hr")
    e_col3.metric("Carbon Equivalent", "18.5 g CO2", "Minimal Impact Zone")

    st.markdown("---")

    # Yeşil Verimlilik Skoru (Sütun C)
    st.subheader("🏅 Green-Fin ROI Index")
    st.progress(88)
    st.write("**Score: 88/100 (High Efficiency)** — The financial value gained from this hybrid analysis significantly outweighs its datacenter environmental cost.")

else:
    st.info("Click the button above to run the hybrid financial analysis and calculate the water/energy footprint.")
