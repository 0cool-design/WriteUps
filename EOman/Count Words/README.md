# [Count Words](https://ctf.eoman.com/competitions/public/coding/count_words)
### 🛢Category: Coding
### 🌟 40 points
### 👓Level: Easy
### Description:

```
Your flag is the total number of words in the attached file, given that these words have numbers that add up to 10.
```

### example:
```
t4?@h4re1re → has 4+4+1 = 9 (not counted)

w1?@e2rr1e → has 1+2+1 = 4 (not counted)

t5?@h3ro2usands → has 5+3+2 = 10 (counted)

o4?@f6r → has 4+6 = 10 (counted)

1b1?@a5rd1 → has 1+1+5+1 = 8 (not counted)
```

## 

```python
# function to sum the digits in a string
def sum_digits_string(str1):
    sum_digit = 0
    # sum the digits if the string has digits
    if any(x.isdigit() for x in str1):
        sum_digit = sum(int(x) for x in str1 if x.isdigit())
    return sum_digit

# open the file
with open("dump.txt", 'r') as file:
    count = 0

    for line in file:
        for word in line.split():
            sumdig = sum_digits_string(word)
            if sumdig == 10:
                count += 1
    # print the total number of words
    print(count)

```
