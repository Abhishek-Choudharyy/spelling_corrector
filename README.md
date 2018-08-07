# Spelling_corrector

Test Data : List of misspelled word (spell_test.csv) where column query is input query and column corr_version is actual spelling

## Version_1:

Basic idea of spelling corrector is based on Peter Norvig’s excellent tutorial — a spelling corrector in 21 lines of Python code.(http://norvig.com/spell-correct.html)

To estimate the probability of a word, {P(word), by counting the number of times each word appears in a text file of about a million words} we are using big.txt(http://norvig.com/big.txt) which is a concatenation of public domain book excerpts from Project Gutenberg and lists of most frequent words from Wiktionary and the British National Corpus.

### Accuracy = 2700/4729
