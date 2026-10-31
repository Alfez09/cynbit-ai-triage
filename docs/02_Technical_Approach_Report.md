# Technical Approach Report – Cynbit Inquiry Triage
## 1. Goal
Input: form fields (name, email, optional company/industry, message). Output: category, confidence, budget, lead score + reasons, priority, owner, draft reply (+ optional LLM summary and missing-info list).

## 2. Architecture
```
Inquiry (contact form / email / CSV)
  -> [A] TF-IDF (1-2 grams) + Logistic Regression -> category + confidence
  -> [B] Regex extractors: budget (Rs/INR/₹/$ + lakh/cr/k), urgency, timeline, role, contact
  -> [C] Explainable lead score 0-100 (service fit, budget, urgency, role, detail, company/industry given)
  -> [D] Router: category -> owner (AI / Engineering / Growth leads, BitElevate, HR, support)
  -> [E] Reply: template (offline) OR LLM JSON {summary, missing_info, reply}
  -> Human approves -> send / CRM
confidence < 0.35 -> human review queue
```
Categories mirror Cynbit's site: ai_automation, custom_it, digital_marketing, bitelevate, careers, other. Careers messages are routed only (not scored).

## 3. Model choices
| Part | Choice | Why |
|---|---|---|
| Classifier | TF-IDF + Logistic Regression (scikit-learn) | Fast, cheap, offline, interpretable, fine for small data; baseline before transformers |
| Lead score | Transparent rules | Sales must see *why*; no conversion labels yet |
| Extraction | Regex | Deterministic, unit-tested |
| Summary/reply | Optional LLM via Anthropic API (`CYNBIT_MODEL`, key in env) | Better tone, missing-info questions; auto-fallback to templates |
Upgrade path: sentence embeddings (Hugging Face sentence-transformers) or fine-tuned DistilBERT with ≥ 1-2k real labelled inquiries; learn score weights from conversion outcomes (gradient boosting); Hinglish support.

## 4. Data pipeline
1. Source: contact-form/email export → CSV with a `text` column.
2. PoC data: 42 synthetic labelled inquiries (6 classes × 7) written from the services/careers/BitElevate/FAQ text on cynbit.in. No real Cynbit inquiries were available.
3. Production: log inquiry + model output + human correction → weekly retrain → versioned model.

## 5. Prompt design (LLM layer)
System prompt fixes role, JSON-only schema, ≤ 90-word reply, no pricing/delivery promises. Inquiry is wrapped in `<inquiry>` tags and declared untrusted (prompt-injection guard). Output parsed defensively; any failure → template reply and a visible reason.

## 6. Evaluation (actual results, `python tests/test_triage.py`)
- 3-fold CV on the 42-row synthetic set: **0.40 accuracy** (6 classes, ~14 rows per fold, so weak; chance ≈ 0.17).
- 6 hand-written held-out inquiries (one per class): **6/6 correct**.
- Unit tests: budget parsing, priority/routing.
**Caveat:** tiny synthetic data; the CV number shows the baseline needs more data, and 6/6 is too few samples to claim real accuracy. Real evaluation = per-class precision/recall, hot-lead recall and a confusion matrix (especially SEO client vs SEO spam, BitElevate vs careers internships) on real inquiries, then A/B on response time.

## 7. Deployment
PoC: Streamlit (single inquiry + batch CSV with download). Next: FastAPI `/triage` endpoint, webhook from the contact form/inbox, CRM/Slack push, logging, rate limits, secrets in env.

## 8. Execution plan
| When | Task |
|---|---|
| Wk 1 | Export 200-500 past inquiries, label, measure baseline, tune classes/rules with sales + HR |
| Wk 2 | FastAPI + form/inbox integration, review queue |
| Wk 3 | Pilot; track KPIs against the 24 h response promise |
| Wk 4+ | Embeddings/fine-tune, learn scoring from conversions, add RAG assistant, blueprint generator |

## 9. Limitations
Synthetic data; categories inferred from public pages (Product Suite and Case Studies not reviewed); English-only; regex budgets miss unusual phrasing; LLM replies require human approval; no live integration in the PoC.
