from pathlib import Path

DATA = Path(__file__).parent / "data"


def _load_wordlist():
    words = set()
    with open(DATA / "wordlist.txt", encoding="utf-8") as f:
        for line in f:
            w = line.strip()
            if w and not w.startswith("#"):
                words.add(w)
    return words


WORDS = _load_wordlist()


def _distance(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def suggest(word, limit=3, max_distance=2):
    """Ghalat lafz ke liye qareeb tareen sahi lafz tajweez karo."""
    word = word.lower()
    if word in WORDS:
        return []
    scored = []
    for w in WORDS:
        if abs(len(w) - len(word)) > max_distance:
            continue
        d = _distance(word, w)
        if d <= max_distance:
            scored.append((d, w))
    scored.sort()
    return [w for _, w in scored[:limit]]


def check(text):
    """Poore jumle me ghalat lafz dhoondo. {lafz: [tajweez]} dict milta hai."""
    return {w: suggest(w) for w in text.lower().split() if suggest(w)}
