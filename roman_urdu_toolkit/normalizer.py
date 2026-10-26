import re
from pathlib import Path

DATA = Path(__file__).parent / "data"

# log aksar jaldi me aise likhte hain, inhe standard form me badlo
VARIANTS = {
    "hy": "hai",
    "rha": "raha",
    "rhi": "rahi",
    "rhy": "rahe",
    "kr": "kar",
    "mujhy": "mujhe",
    "mjhy": "mujhe",
    "tumhy": "tumhe",
    "tumhn": "tumhen",
    "apko": "aapko",
    "nhe": "nahi",
    "ni": "nahi",
}


def _load_known():
    words = set()
    with open(DATA / "wordlist.txt", encoding="utf-8") as f:
        for line in f:
            w = line.strip()
            if w and not w.startswith("#"):
                words.add(w)
    return words


KNOWN = _load_known()


def _fix_repeats(word):
    if word in KNOWN:
        return word
    squashed = re.sub(r"(.)\1+", r"\1", word)  # bohaat -> bohat
    return squashed if squashed in KNOWN else word


def normalize(text):
    """Roman Urdu text ko saaf karo: lowercase, repeated letters fix, variants map."""
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    words = [VARIANTS.get(w, w) for w in text.split(" ")]
    return " ".join(_fix_repeats(w) for w in words)
