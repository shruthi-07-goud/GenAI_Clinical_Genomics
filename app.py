# ======================================================
# AI Powered Genomics Diagnostic Dashboard
# ======================================================

import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------

st.set_page_config(
    page_title="AI Genomics Diagnostic System",
    page_icon="🧬",
    layout="wide"
)

# ------------------------------------------------------
# SIDEBAR MENU
# ------------------------------------------------------

st.sidebar.title("🧬 Genomics AI Dashboard")

menu = st.sidebar.radio(
    "Navigation",
    ["Home", "Patient Analysis", "Gene Database", "About Project"]
)

# ------------------------------------------------------
# GENE DATABASE
# ------------------------------------------------------

GENE_DATABASE = {

    "SCN1A": {"disease": "Dravet Syndrome","phenotypes": ["seizures","epilepsy"]},

    "MECP2": {"disease": "Rett Syndrome","phenotypes": ["developmental delay","intellectual disability"]},

    "SMN1": {"disease": "Spinal Muscular Atrophy","phenotypes": ["muscle weakness","difficulty breathing"]},

    "CFTR": {"disease": "Cystic Fibrosis","phenotypes": ["chronic cough","lung infections"]},

    "HTT": {"disease": "Huntington Disease","phenotypes": ["movement disorder","cognitive decline"]},

    "HBB": {"disease": "Sickle Cell Disease","phenotypes": ["anemia","fatigue"]},

    "PAH": {"disease": "Phenylketonuria","phenotypes": ["seizures","intellectual disability"]},

    "DMD": {"disease": "Duchenne Muscular Dystrophy","phenotypes": ["muscle weakness","difficulty walking"]}

}

# ------------------------------------------------------
# HOME PAGE
# ------------------------------------------------------

if menu == "Home":

    st.title("🧬 AI-Driven Clinical Genomics Platform")

    st.write("""
    This prototype demonstrates how **Artificial Intelligence**
    can assist clinicians in identifying **possible genetic disorders**
    using patient symptoms (phenotypes).
    """)

    col1,col2,col3 = st.columns(3)

    col1.metric("Genes Available", len(GENE_DATABASE))
    col2.metric("Diseases Covered", len(GENE_DATABASE))
    col3.metric("AI Model", "Prototype")

# ------------------------------------------------------
# PATIENT ANALYSIS PAGE
# ------------------------------------------------------

elif menu == "Patient Analysis":

    st.header("🔬 Patient Symptom Analysis")

    # Patient details form
    with st.form("patient_form"):

        name = st.text_input("Patient Name")
        age = st.number_input("Patient Age",1,100)

        symptoms = st.multiselect(
            "Select Observed Symptoms",
            ["seizures","developmental delay","muscle weakness","fatigue",
             "chronic cough","difficulty walking","anemia","lung infections"]
        )

        submit = st.form_submit_button("Run AI Analysis")

    if submit:

        st.success("Patient Data Submitted")

        gene_scores = {}

        for gene,data in GENE_DATABASE.items():

            score = 0

            for s in symptoms:

                if s in data["phenotypes"]:
                    score += 1

            if score > 0:
                gene_scores[gene] = score

        if len(gene_scores) == 0:

            st.error("No gene matches found")

        else:

            df = pd.DataFrame(
                gene_scores.items(),
                columns=["Gene","Score"]
            ).sort_values(by="Score",ascending=False)

            st.subheader("🧬 Candidate Genes")

            st.table(df)

            # BAR CHART
            st.subheader("Gene Ranking Chart")

            fig = px.bar(
                df,
                x="Gene",
                y="Score",
                title="Gene Priority Score"
            )

            st.plotly_chart(fig)

            # PIE CHART
            st.subheader("Disease Probability Distribution")

            fig2 = px.pie(
                df,
                values="Score",
                names="Gene"
            )

            st.plotly_chart(fig2)

# ------------------------------------------------------
# GENE DATABASE PAGE
# ------------------------------------------------------

elif menu == "Gene Database":

    st.header("🧬 Gene Knowledge Base")

    gene_search = st.text_input("Search Gene")

    for gene,data in GENE_DATABASE.items():

        if gene_search.upper() in gene:

            st.write("###",gene)
            st.write("Disease:",data["disease"])
            st.write("Symptoms:",data["phenotypes"])

# ------------------------------------------------------
# ABOUT PAGE
# ------------------------------------------------------

elif menu == "About Project":

    st.header("📚 About This Project")

    st.write("""
    This project demonstrates how **Generative AI**
    can assist clinical genomics research by
    prioritizing genes based on patient phenotypes.

    Technologies Used:
    • Python  
    • Streamlit  
    • AI-assisted phenotype analysis  

    This is a prototype for educational purposes.
    """)
