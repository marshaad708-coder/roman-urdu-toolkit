from pathlib import Path

DATA = Path(__file__).parent / "data"
NEGATIONS = {"nahi", "nahin", "na", "mat"}


def _load_words(name):
    with open(DATA / name, encoding="utf-8") as f:
        return {l.strip() for l in f if l.strip() and not l.startswith("#")}


POS = _load_words("positive_words.txt")
NEG = _load_words("negative_words.txt")


def analyze_sentiment(text):
    """Lexicon based sentiment. negation ('nahi acha') ko bhi handle karta hai."""
    words = text.lower().split()
    score = 0
    negate = False
    for w in words:
        if w in NEGATIONS:
            negate = True
            continue
        val = 0
        if w in POS:
            val = 1
        elif w in NEG:
            val = -1
        if val:
            score += -val if negate else val
            negate = False
    if negate and score:
        score = -score  # 'acha nahi' jaisa case
    if score > 0:
        label = "positive"
    elif score < 0:
        label = "negative"
    else:
        label = "neutral"
    return {"label": label, "score": score}
