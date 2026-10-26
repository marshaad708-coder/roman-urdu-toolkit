"""Command line demo: python demo.py"""
from roman_urdu_toolkit import normalize, to_urdu, analyze_sentiment, check

samples = [
    "Ye kitab bohaaat achi hy",
    "mujhy ye khana bilkul pasand nahi aya",
    "aaj mosam kitna khushgawar hai",
    "tumhara dost tumse milne aaya tha",
]

for s in samples:
    clean = normalize(s)
    print("Input:      ", s)
    print("Normalized: ", clean)
    print("Urdu:       ", to_urdu(clean))
    print("Sentiment:  ", analyze_sentiment(clean))
    print("Spellcheck: ", check(clean) or "sab lafz theek hain")
    print("-" * 45)
