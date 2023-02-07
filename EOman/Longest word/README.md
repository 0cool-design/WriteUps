# [Longest word](https://ctf.eoman.com/competitions/public/coding/longest_word)
### 🛢Category: Coding
### 🌟 15 points
### 👓Level: Easy
### Description:

```
Your flag is the longest word in the attached article file.
```

## Importing libraries

```python
import functools as ft
```



## read the file and split it into words and find the longest word

```python
# open the file and read it
with open('article.txt', 'r') as f:
    # split the file into words
    s = [y for x in f.readlines() for y in x.split()]
    # find the longest word
    longest = max(s, key=len)
    # print the longest word and its length
    print(longest, "and it is", len(longest), "characters long")

```
