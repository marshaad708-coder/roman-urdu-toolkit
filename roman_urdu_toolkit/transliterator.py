from pathlib import Path

DATA = Path(__file__).parent / "data"


def _load_dict():
    mapping = {}
    with open(DATA / "roman_to_urdu.txt", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            roman, urdu = line.split("\t")
            mapping[roman.strip()] = urdu.strip()
    return mapping


_DICT = _load_dict()


def to_urdu(text):
    """Roman Urdu -> Urdu script, word by word. Jo lafz na mile wo waisa hi rahega."""
    return " ".join(_DICT.get(w, w) for w in text.split())


def known_words():
    return sorted(_DICT.keys())
