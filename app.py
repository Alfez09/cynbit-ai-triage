import pandas as pd
import streamlit as st
import triage

st.set_page_config(page_title="Cynbit Inquiry Triage", page_icon="🎯", layout="wide")


@st.cache_resource
def get_model():
    return triage.train()


model = get_model()
st.title("🎯 Cynbit AI Inquiry Triage")
st.caption("Classify → score → route → draft reply for website inquiries (PoC).")
use_llm = st.sidebar.toggle("LLM-enhanced summary/reply (needs ANTHROPIC_API_KEY)", value=False)
if st.sidebar.button("Show CV accuracy"):
    st.sidebar.write(f"{triage.cv_accuracy():.0%} (3-fold, small synthetic set)")

tab1, tab2 = st.tabs(["Single inquiry", "Batch CSV"])

with tab1:
    pick = st.selectbox("Load sample", ["(custom)"] + triage.SAMPLES, format_func=lambda s: s[:80])
    c1, c2, c3 = st.columns(3)
    name = c1.text_input("Full name")
    company = c2.text_input("Company (optional)")
    industry = c3.text_input("Industry (optional)")
    text = st.text_area("Inquiry", value="" if pick == "(custom)" else pick, height=140)
    if st.button("Analyze", type="primary") and text.strip():
        r = triage.analyze(text, model, name, use_llm, company, industry)
        c = st.columns(4)
        c[0].metric("Category", r["category"])
        c[1].metric("Confidence", f"{r['confidence']:.0%}")
        c[2].metric("Lead score", r["lead_score"])
        c[3].metric("Priority", r["priority"])
        st.write(f"**Route to:** {r['route_to']}")
        if r["budget_inr"]:
            st.write(f"**Detected budget:** ≈ ₹{r['budget_inr']:,.0f}")
        if r["needs_human_review"]:
            st.warning("Low confidence – send to human review.")
        st.write("**Score reasons:** " + (", ".join(r["score_reasons"]) or "none"))
        if r.get("summary"):
            st.write(f"**Summary:** {r['summary']}")
        if r.get("missing_info"):
            st.write("**Missing info:** " + ", ".join(r["missing_info"]))
        if r.get("llm_error"):
            st.info(f"LLM skipped: {r['llm_error']} (template reply used)")
        st.text_area("Draft reply (human approves before sending)", r["reply"], height=130)

with tab2:
    up = st.file_uploader("CSV with a 'text' column", type="csv")
    if up:
        df = pd.read_csv(up)
        out = pd.DataFrame([triage.analyze(str(t), model) for t in df["text"]]).drop(columns=["reply", "score_reasons"])
        res = pd.concat([df, out], axis=1)
        st.dataframe(res, use_container_width=True)
        st.download_button("Download results", res.to_csv(index=False), "triage_results.csv")
