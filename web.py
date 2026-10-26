"""Web demo: python web.py  ->  http://127.0.0.1:5000"""
from flask import Flask, request, render_template_string
from roman_urdu_toolkit import normalize, to_urdu, analyze_sentiment, check

app = Flask(__name__)

PAGE = """
<!doctype html><html><head><meta charset="utf-8">
<title>Roman Urdu Toolkit</title>
<style>
body{font-family:system-ui;background:#f4f4f5;max-width:640px;margin:40px auto;padding:0 16px}
textarea{width:100%;height:90px;font-size:16px;padding:10px}
button{font-size:16px;padding:8px 18px;margin:6px 4px 0 0;cursor:pointer}
pre{background:#fff;border:1px solid #ddd;padding:14px;white-space:pre-wrap;font-size:15px}
h1{font-size:24px}
</style></head><body>
<h1>Roman Urdu Toolkit</h1>
<form method="post">
<textarea name="text" placeholder="Roman Urdu me kuch likho...">{{ text }}</textarea><br>
<button name="tool" value="all">Sab kuch</button>
<button name="tool" value="normalize">Normalize</button>
<button name="tool" value="urdu">Urdu script</button>
<button name="tool" value="sentiment">Sentiment</button>
<button name="tool" value="spell">Spell check</button>
</form>
{% if result %}<h3>Result</h3><pre>{{ result }}</pre>{% endif %}
</body></html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    text, result = "", ""
    if request.method == "POST":
        text = request.form.get("text", "")
        tool = request.form.get("tool", "all")
        clean = normalize(text)
        out = []
        if tool in ("all", "normalize"):
            out.append("Normalized: " + clean)
        if tool in ("all", "urdu"):
            out.append("Urdu: " + to_urdu(clean))
        if tool in ("all", "sentiment"):
            out.append("Sentiment: " + str(analyze_sentiment(clean)))
        if tool in ("all", "spell"):
            bad = check(clean)
            out.append("Spellcheck: " + (str(bad) if bad else "sab lafz theek hain"))
        result = "\n".join(out)
    return render_template_string(PAGE, text=text, result=result)


if __name__ == "__main__":
    app.run(debug=True)
