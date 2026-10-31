# AI Opportunity Report – Cynbit Technologies
Author: Alfez Khan (github.com/Alfez09) | Task: AI/ML Engineer Intern – Identify an AI Opportunity

## 1. Company snapshot (from cynbit.in pages: Careers, Services, Contact)
- Cynbit Technologies, Pratap Nagar, Jaipur; remote-first; serves clients globally. Tagline: "Engineered for Optimism".
- **Three service lines**
  - *AI Automation Suite:* autonomous agents (lead/coordination assistants), LLM automation (data entry, document handling), AI voice agents, AI stack integration into existing SaaS.
  - *Custom IT:* full-stack web/mobile, backend systems (99.9% uptime goal), AWS/Azure cloud, legacy migration.
  - *Digital Marketing:* performance ads (Google/Meta), technical SEO, CRM automation, funnel optimisation.
- **BitElevate:** flagship training initiative (ecosystem, learning paths, student diaries). Also a Product Suite (a "proprietary SaaS suite" is referenced in a QA internship post) and Case Studies pages – *not reviewed in detail*.
- **Products / case studies named in research notes (names only, not independently verified):** Cynbit Studio, Revio, WizHealth, EContentPrep, Cloudy Tales, Evento, GlobalPay. The notes describe them as spanning AI/ML, LLM apps, backend, data processing and cloud work across several industries. Whether each is an ongoing client engagement, completed engagement, internal demo or portfolio example is **unknown**; I did not review their pages, so no feature or architecture claims are made about them.
- **Hiring:** 12 internships (business, marketing, tech incl. AI/ML Engineer Intern) + 8 full-time roles (growth + core engineering incl. AI Engineer) – all Remote/Jaipur.
- **Inquiry Hub:** one form (Full Name, Email, optional Company, optional Industry, Message) promising a **24 h response** and a "tailored strategic overview before we connect"; plus emails (opportunities@, support@), 3 phone lines and an FAQ. Newsletter claims 25k+ readers (company claim).

## 2. Key observation
Four very different intents – **client projects (3 service lines), BitElevate enrolments, job/internship applications, and support/spam** – arrive through a shared form and shared inboxes. Every message must be read, classified, routed and answered manually within a 24 h promise, and the "strategic overview" needs requirement extraction before the first call. These products suggest the same triage/RAG building blocks could later be reused across Cynbit's own offerings (to be validated with the team). Cynbit also *sells* AI agents, LLM automation and CRM automation, so solving this internally doubles as a live case study.

## 3. Opportunities (ordered by score)
| # | Opportunity | Users | Value | Effort | Data | Risk |
|---|---|---|---|---|---|---|
| 1 | **Inquiry triage: classify, lead-score, route, draft reply** | Sales, HR, BitElevate team | High: faster replies, no lost leads, sellable as a productised agent | Low | Past form/email inquiries (~200) | Misrouting → human review |
| 2 | RAG assistant over services, FAQ, BitElevate and careers pages | Visitors, applicants | Med-High: 24×7 answers, fewer repetitive queries | Med | Site content | Hallucination → cite sources, refuse out-of-scope |
| 3 | Content/SEO engine (drafts, briefs, repurposing for blog/newsletter) | Marketing team | Medium | Med | Existing blog, keyword data | Quality/brand → human edit |
| 4 | Auto "Blueprint" generator: requirement brief → scope, risks, questions, rough estimate | Sales, PMs | High | Med-High | Past proposals, rate cards | Bad estimates → advisory only |
| 5 | Resume/portfolio screening for 20 open roles | HR | Medium | Low-Med | JDs + applications | Bias → explainable, human decides |
| 6 | BitElevate personalised learning paths + drop-off prediction | Program team, learners | Medium (future product) | High | Learner activity data | Cold start |

## 4. Prioritisation
Score = Value (1-5) × Feasibility (1-5) × Data availability (1-5) – my judgement, not measured data.
| # | V | F | D | Score |
|---|---|---|---|---|
| 1 | 5 | 5 | 4 | **100** |
| 2 | 4 | 4 | 5 | 80 |
| 3 | 3 | 4 | 4 | 48 |
| 4 | 5 | 3 | 3 | 45 |
| 5 | 3 | 4 | 3 | 36 |
| 6 | 3 | 2 | 2 | 12 |

## 5. Selected: Inquiry Triage
**Problem:** all inquiry types are read manually, routed by hand and answered late; high-intent client leads wait behind spam, vendor pitches and job-seekers.
**Solution:** intent classification (AI automation / custom IT / digital marketing / BitElevate / careers / other) → extract budget, urgency, timeline, role → explainable lead score (0-100) → route to the right owner (sales leads, HR, BitElevate team, support) → draft reply asking for the missing details, for human approval.
**Why first:** lowest effort, needs little data, plugs into the existing form/inbox, produces labelled data for #2 and #4, and the benefit is measurable against the existing 24 h promise. The extracted fields and "missing info" list are exactly the input for the "strategic overview" Cynbit promises.
**Design note:** "SEO / digital-marketing" is both a Cynbit service (client wants it) and a common spam theme (vendor selling it) – the classifier is trained on both and tested for this confusion.

## 6. KPIs
First-response time (drafts in minutes vs hours); routing accuracy vs human labels (target ≥ 90% on real data); hot-lead recall (target ≥ 95%); lead→discovery-call conversion; sales/HR hours saved per week.

## 7. Risks & controls
Misclassification → confidence threshold + human review. Hallucinated promises → drafts only, no pricing/delivery commitments. PII (name, email, phone) → minimal storage, masked logs. Prompt injection via inquiry text → treated as data. Hiring bias → careers messages are only routed, never scored.

## 8. Roadmap
Wk 1 pilot on historical inquiries → Wk 2-3 integrate with the contact form/inbox + CRM → Month 2 RAG assistant (#2) → Month 3 blueprint generator (#4); package triage as a client offering under AI Automation Suite.
