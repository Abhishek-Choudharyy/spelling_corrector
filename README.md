# Spelling_corrector

Test Data : List of misspelled word (spell_test.csv) where column query is input query and column corr_version is actual spelling

## Version_1 (Probability Model):

Basic idea of spelling corrector is based on Peter Norvig’s excellent tutorial — a spelling corrector in 21 lines of Python code.(http://norvig.com/spell-correct.html)

To estimate the probability of a word, {P(word), by counting the number of times each word appears in a text file of about a million words} we are using big.txt(http://norvig.com/big.txt) which is a concatenation of public domain book excerpts from Project Gutenberg and lists of most frequent words from Wiktionary and the British National Corpus.

### Accuracy = 2743/4729 (58%)

## Phonetic Algorithms

Phonetic algorithms helps us to detect similar-sounding words even if they are spelt differently.There are different algorithms to calculate the sound of a word like Soundex, Metaphone, and the Match Rating codex.Each of these algorithms were designed with a certain language or purpose in mind, and do not fit in each others languages in exactly the same way.We will use multiple algorithms with intial random weight vector to regulate the influence of each specific phonetic algorithm.(https://stackabuse.com/phonetic-similarity-of-words-a-vectorized-approach-in-python/)

**Edit Distance**is the distance whose value describes the minimal number of single-character edits required to transform one string (the source) into another (the target).

There are many algorithms to measure edit distance, which are calculated using a different set of allowable edit operations. For instance,

**Levenshtein distance** allows insertions, deletions or substitutions;<br />
**Damerau–Levenshtein distance**allows insertion, deletion, substitution, and the transposition of two adjacent characters;<br />
**Hamming distance** allows only substitution, hence, it only applies to strings of the same length;<br />
**Jaro distance** allows only transposition.<br />

We will use **Damerau–Levenshtein distance** to find edit distance between source and target(phonetics.py).
 
