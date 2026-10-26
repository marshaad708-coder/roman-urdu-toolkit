from .normalizer import normalize
from .transliterator import to_urdu
from .sentiment import analyze_sentiment
from .spellcheck import suggest, check

__version__ = "0.1.0"
__all__ = ["normalize", "to_urdu", "analyze_sentiment", "suggest", "check"]
