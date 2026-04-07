# P1: Data Detective

## Summary
This project analyzes a text file, counts word frequencies, shows the top N words, and reports one extra insight.

## Dataset
- **File:** [INSERT_YOUR_FILENAME_HERE.txt]
- **Why I chose it:** I chose this dataset to test the program's ability to handle standard English prose, specifically looking at how common stop-words dominate frequency counts in classical literature.

## How to run
```bash
pytest -q
python -m src.project
```

## Approach
- **Load text:** Utilized `pathlib` to read the file content into a string using UTF-8 encoding.
- **Normalize:** Converted the text to lowercase and used `str.maketrans` to strip punctuation efficiently.
- **Tokenize:** Split the normalized string into a list of words, automatically collapsing extra whitespace.
- **Count frequencies:** Employed `collections.Counter` to generate a frequency dictionary of all unique words.
- **Top N words:** Implemented a sorting algorithm that prioritizes count (descending) and uses alphabetical order as a tie-breaker.
- **Extra insight:** Calculated the average word length across the entire dataset to measure linguistic complexity.

## Complexity

**`count_words`**
- Time: O(N)
- Space: O(U)
- Why: The function iterates through the list of N words exactly once. Space complexity depends on the number of unique words (U) stored in the dictionary.

**`top_n_words`**
- Time: O(U log U)
- Space: O(U)
- Why: Sorting the unique words (U) using Python's built-in Timsort takes O(U log U) time. We store the sorted list of unique entries in memory.

## Edge-case checklist
- [x] empty file
- [x] punctuation-heavy input
- [x] repeated words
- [x] uppercase/lowercase differences
- [x] `n <= 0`

## Assistance & sources
- **AI used? (Y/N):** Y
- **What it helped with:** Gemini assisted in structuring the `top_n_words` tie-breaking logic and providing the complexity analysis.
- **Other sources:** Python Official Documentation for `string.punctuation` and `pathlib`.

## Design note (150–250 words)
The primary goal of this project was to create a robust text analysis pipeline using only the Python Standard Library. My design decisions centered on data cleanliness and predictable output. Specifically, I chose to use a translation table for punctuation removal because it is significantly more performant than multiple `.replace()` calls or manual character checking.

One of the more interesting challenges was the tie-breaking logic in the `top_n_words` function. I decided that if two words appear the same number of times, they should be sorted alphabetically. This ensures that the program's output is consistent every time it runs, which is a best practice in data processing. For the "Extra Insight," I implemented an average word length calculator. This provides a quick statistical snapshot of the text's difficulty level; for example, technical manuals usually have a higher average word length than children's stories.

The most difficult part was ensuring the tokenizer didn't create empty strings when encountering multiple spaces or newlines. By using `.split()` without specific delimiters, I leveraged Python's built-in ability to treat any amount of whitespace as a single separator. If I were to improve this project further, I would add a "Stop-Word" list to filter out common words like "the" and "and," which would make the "Top N" results more meaningful for thematic analysis.