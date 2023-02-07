# [Special summation](https://ctf.eoman.com/competitions/public/coding/special_summation)
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
<p>7+<span style="background-color: rgb(255, 255, 153); --darkreader-inline-bgcolor:#545400;" data-darkreader-inline-bgcolor="">9</span>=<span style="color: rgb(0, 0, 255); --darkreader-inline-color:#337dff;" data-darkreader-inline-color="">16</span><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style="color: rgb(0, 0, 255); --darkreader-inline-color:#337dff;" data-darkreader-inline-color="">16</span>+<span style="background-color: rgb(255, 255, 153); --darkreader-inline-bgcolor:#545400;" data-darkreader-inline-bgcolor="">11</span>=<span style="color: rgb(153, 51, 0); --darkreader-inline-color:#ff9661;" data-darkreader-inline-color="">27</span><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style="color: rgb(153, 51, 0); --darkreader-inline-color:#ff9661;" data-darkreader-inline-color="">27</span>+<span style="background-color: rgb(255, 255, 153); --darkreader-inline-bgcolor:#545400;" data-darkreader-inline-bgcolor="">13</span>=<span style="color: rgb(255, 0, 0); --darkreader-inline-color:#ff1a1a;" data-darkreader-inline-color="">40 </span>(<em><span style="color: rgb(255, 0, 0); --darkreader-inline-color:#ff1a1a;" data-darkreader-inline-color="">skipped because the total 40 ends with 0 </span></em>)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style="color: rgb(128, 0, 128); --darkreader-inline-color:#ff72ff;" data-darkreader-inline-color="">27</span>+<span style="background-color: rgb(255, 255, 153); --darkreader-inline-bgcolor:#545400;" data-darkreader-inline-bgcolor="">15</span>=<span style="color: rgb(128, 0, 128); --darkreader-inline-color:#ff72ff;" data-darkreader-inline-color="">42</span><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style="color: rgb(128, 0, 128); --darkreader-inline-color:#ff72ff;" data-darkreader-inline-color="">42</span>+<span style="background-color: rgb(255, 255, 153); --darkreader-inline-bgcolor:#545400;" data-darkreader-inline-bgcolor="">17</span>=<strong>59</strong></p>

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
