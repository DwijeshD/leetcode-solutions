# Word Pattern  ·  Easy

> Leetcode · [Open problem](https://leetcode.com/problems/word-pattern) · synced 2026-08-18

**Language:** python3
**Topics:** Hash Table, String
**Size:** 15 lines · 330 chars
**Revisions:** 9

## Complexity

- **Time:** _not analyzed yet_
- **Space:** _not analyzed yet_

## Solution

See [`Solution.py`](./Solution.py).

```python

            if char in char_to_word and char_to_word[char] != 
            word:
                return False

            if word in word_to_char and word_to_char[word] != 
            char:
                return False

            char_to_word[char] = word
            word_to_char[word] = char

        return True

        

```
