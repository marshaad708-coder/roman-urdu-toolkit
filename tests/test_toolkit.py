import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from roman_urdu_toolkit import normalize, to_urdu, analyze_sentiment, suggest


def test_normalize():
    assert normalize("Ye BOHAAT achi hy") == "ye bohat achi hai"


def test_transliterate():
    assert to_urdu("ye kitab achi hai") == "یہ کتاب اچھی ہے"


def test_sentiment_positive():
    assert analyze_sentiment("ye din bohat khushgawar hai")["label"] == "positive"


def test_sentiment_negative():
    assert analyze_sentiment("mujhe ye khana pasand nahi aya")["label"] == "negative"


def test_spellcheck():
    assert "kitab" in suggest("kitaabb")
    assert suggest("kitab") == []


if __name__ == "__main__":
    test_normalize()
    test_transliterate()
    test_sentiment_positive()
    test_sentiment_negative()
    test_spellcheck()
    print("all tests passed")
