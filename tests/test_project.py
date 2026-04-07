from src.project import (
    count_words,
    normalize_text,
    tokenize,
    top_n_words,
)

# --- Normalization Tests ---

def test_normalize_text_lowercases_text() -> None:
    assert normalize_text("Hello WORLD") == "hello world"

def test_normalize_text_removes_punctuation() -> None:
    # Added to ensure your cleaning logic works
    assert normalize_text("Hello, World!") == "hello world"
    assert normalize_text("Data-Detective...") == "datadetective"

def test_normalize_text_handles_empty_string() -> None:
    assert normalize_text("") == ""


# --- Tokenization Tests ---

def test_tokenize_splits_words() -> None:
    assert tokenize("one two three") == ["one", "two", "three"]

def test_tokenize_handles_extra_whitespace() -> None:
    # Ensures that multiple spaces don't result in empty strings in your list
    assert tokenize("one   two\nthree") == ["one", "two", "three"]


# --- Counting Tests ---

def test_count_words_counts_repeated_words() -> None:
    words = ["red", "blue", "red"]
    assert count_words(words) == {"red": 2, "blue": 1}

def test_count_words_empty_list() -> None:
    assert count_words([]) == {}


# --- Top N Sorting Tests ---

def test_top_n_words_returns_most_common_items() -> None:
    counts = {"apple": 3, "banana": 1, "carrot": 2}
    # Should return top 2: apple (3) and carrot (2)
    assert top_n_words(counts, 2) == [("apple", 3), ("carrot", 2)]

def test_top_n_words_tie_breaking() -> None:
    """Requirement: For ties, sort alphabetically."""
    counts = {"zebra": 5, "apple": 5, "banana": 2}
    # Both zebra and apple have 5, but apple comes first alphabetically
    result = top_n_words(counts, 2)
    assert result == [("apple", 5), ("zebra", 5)]

def test_top_n_words_with_non_positive_n_returns_empty_list() -> None:
    counts = {"apple": 3}
    assert top_n_words(counts, 0) == []
    assert top_n_words(counts, -1) == []

def test_top_n_words_requesting_more_than_available() -> None:
    counts = {"apple": 1}
    # If we ask for 5 but only have 1, it should just return the 1
    assert top_n_words(counts, 5) == [("apple", 1)]