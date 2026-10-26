# Roman Urdu Toolkit

Roman Urdu text ke liye chhota sa Python toolkit. Karoron log Roman Urdu likhte hain lekin is ke liye koi standard tools nahi — ye gap fill karne ki koshish hai.

## Features

- **normalize()** — text saaf karo: lowercase, repeated letters fix (`bohaaat` → `bohat`), common variants map (`hy` → `hai`)
- **to_urdu()** — Roman Urdu se Urdu script me convert (200+ lafz ki dictionary)
- **analyze_sentiment()** — jazbaat pehchano: positive / negative / neutral (negation handle karta hai, jaise `nahi acha`)
- **suggest() / check()** — spell check aur tajweez

## Install

```bash
pip install flask   # sirf web demo ke liye, toolkit khud zero-dependency hai
```

## Usage

```python
from roman_urdu_toolkit import normalize, to_urdu, analyze_sentiment, check

text = normalize("Ye kitab bohaaat achi hy")
print(text)                    # ye kitab bohat achi hai
print(to_urdu(text))           # یہ کتاب بہت اچھی ہے
print(analyze_sentiment(text))  # {'label': 'positive', 'score': 2}
print(check("ye kitaab achi hy"))
# {'kitaab': ['kitab'], 'hy': ['hai']}
```

## Demo

```bash
python demo.py     # command line demo
python web.py      # web demo -> http://127.0.0.1:5000
python tests/test_toolkit.py   # tests
```

## Roadmap

- ML-based sentiment (TF-IDF + Logistic Regression, apne dataset par trained)
- Bara dictionary + POS tagging
- REST API (FastAPI)

## License

MIT
