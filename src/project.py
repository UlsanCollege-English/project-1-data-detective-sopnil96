"""Project 1 starter: Data Detective.

Implement the required functions below.
Use standard library only.
"""

from __future__ import annotations
import string
from collections import Counter
from pathlib import Path


def load_text(path: str) -> str:
    """Load and return the full text from a UTF-8 file."""
    # .read_text() is a clean way to handle opening and closing the file
    return Path(path).read_text(encoding="utf-8")


def normalize_text(text: str) -> str:
    """Return a normalized version of the text."""
    # 1. Convert to lowercase
    text = text.lower()
    
    # 2. Remove punctuation using a translation table
    # This replaces every punctuation character with None (deletes it)
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator)
    
    # 3. Collapse extra whitespace
    return " ".join(text.split())


def tokenize(text: str) -> list[str]:
    """Split normalized text into a list of words."""
    # Split by whitespace (handles spaces, tabs, newlines)
    return text.split()


def count_words(words: list[str]) -> dict[str, int]:
    """Count how many times each word appears."""
    # Counter is an optimized standard library dictionary for counting
    return dict(Counter(words))


def top_n_words(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Return the top N words as (word, count) tuples."""
    if n <= 0:
        return []

    # Sort logic: 
    # Primary sort: count (item[1]) descending (negative sign)
    # Secondary sort: word (item[0]) alphabetically (ascending)
    sorted_items = sorted(
        counts.items(), 
        key=lambda item: (-item[1], item[0])
    )
    
    return sorted_items[:n]


def extra_insight(words: list[str], counts: dict[str, int]) -> str:
    """Return the average word length of the dataset."""
    if not words:
        return "0.00"
    
    total_chars = sum(len(word) for word in words)
    avg_length = total_chars / len(words)
    
    return f"Average word length: {avg_length:.2f} characters"


def run_demo(path: str, n: int = 10) -> dict[str, object]:
    """Run the full analysis pipeline and return summary data."""
    text = load_text(path)
    normalized = normalize_text(text)
    words = tokenize(normalized)
    counts = count_words(words)

    return {
        "total_words": len(words),
        "unique_words": len(counts),
        "top_words": top_n_words(counts, n),
        "extra_insight": extra_insight(words, counts),
    }


if __name__ == "__main__":
    # Ensure this points to your actual file in the /data folder
    demo_path = Path("data/sample.txt")
    if demo_path.exists():
        results = run_demo(str(demo_path), n=10)
        print("--- Analysis Results ---")
        for key, value in results.items():
            print(f"{key}: {value}")
    else:
        print(f"No demo file found at {demo_path}")