# [Longest word](https://ctf.eoman.com/competitions/public/coding/special_summation)
### 🛢Category: Coding
### 🌟 35 points
### 👓Level: Easy
### Description:

```
Using any programming language, create a function to calculate the total sum of 
all "odd" integers between any two given numbers,
under the condition that any sum total ends with 0 will NOT be counted.
```
```
For example: the sum of all odd integers between 6 and 18 will be:

7+9=16
        16+11=27
                    27+13=40 (skipped because the total 40 ends with 0 )
                    27+15=42
                                  42+17=59

Total is 59
```

## function to calculate the total sum of all "odd" integers between any two given numbers 
```python

def sum_odd(start, end):
    # get all odd numbers between start and end
    odds = [x for x in range(start, end) if x % 2 != 0]
    sum = 0
    temp = odds[0]
    # loop through the odds and add them to the sum
    for i in range(1, len(odds)):
        #
        sum = temp + odds[i]
        # using modulo 10 to check if the sum ends with 0
        # if not add it to the sum
        if sum % 10 != 0:
            temp = sum
    # return the sum
    return sum
```

## get the result

```python
sum_odd(10, 1000)

```
