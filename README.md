# Cynbit AI Inquiry Triage (PoC)

AI/ML Engineer Intern task: *Identify an AI Opportunity for Cynbit.* — by Alfez Khan ([github.com/Alfez09](https://github.com/Alfez09))
**Chosen opportunity:** automated triage of inbound website inquiries (classify (AI automation / custom IT / digital marketing / BitElevate / careers / other) → lead-score → route → draft reply.

## Deliverables
- `docs/01_AI_Opportunity_Report.md` – opportunity analysis & prioritisation
- `app.py` + `triage.py` – working PoC (Streamlit)
- `docs/02_Technical_Approach_Report.md` – models, pipeline, prompts, evaluation, plan

## Run
```bash
pip install -r requirements.txt
streamlit run app.py            # UI
python tests/test_triage.py     # tests + CV accuracy
```
Works fully offline (TF-IDF + Logistic Regression + rules). Optional LLM layer:
```bash
export ANTHROPIC_API_KEY=...    # optional; CYNBIT_MODEL overrides default model
```
then enable the sidebar toggle for summary, missing-info and a better reply draft.

## Notes
- Training data is a **small synthetic set** (`data/sample_inquiries.csv`, 42 rows) written from assumed Cynbit service lines. Metrics are indicative only; real inquiry logs are needed for real accuracy.
- Replies are drafts; a human approves before sending.
- Inquiry text is treated as untrusted data in the LLM prompt (prompt-injection guard).
