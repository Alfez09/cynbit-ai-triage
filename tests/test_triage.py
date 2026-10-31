import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import triage

HELD_OUT = [
    ("Need a mobile app and backend APIs for our fintech startup, budget Rs 4 lakh, launch in 3 months", "custom_it"),
    ("We want AI agents to automate our document handling and lead follow-ups", "ai_automation"),
    ("Need Google ads and SEO to improve leads for our clinic", "digital_marketing"),
    ("What are the details to enroll in the BitElevate learning cohort?", "bitelevate"),
    ("I would like to apply for the QA testing intern vacancy, my resume is attached", "careers"),
    ("Get 5000 cheap followers and likes, limited offer, click now", "other"),
]


def test_budget():
    assert triage.parse_budget("budget Rs 3 lakh") == 3e5
    assert triage.parse_budget("around $10k") == 10e3 * 85
    assert triage.parse_budget("no budget mentioned") is None


def test_classifier_heldout():
    m = triage.train()
    hits = sum(triage.analyze(t, m)["category"] == y for t, y in HELD_OUT)
    print(f"held-out accuracy: {hits}/{len(HELD_OUT)}")
    assert hits >= 5


def test_priority():
    m = triage.train()
    assert triage.analyze(triage.SAMPLES[0], m)["priority"] == "Hot"
    assert triage.analyze(triage.SAMPLES[2], m)["priority"] == "Route"


if __name__ == "__main__":
    test_budget(); test_classifier_heldout(); test_priority()
    print("cv accuracy:", round(triage.cv_accuracy(), 2)); print("all tests passed")
