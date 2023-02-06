# [Scattered](https://ctf.eoman.com/competitions/public/cryptography/scattered)
### 🛢Category: Cryptography
### 🌟 80 points
### 👓Level: Easy
### Description:

```
The flag is scattered among many files available in the attached zip file.

Try to get things back in order and capture the flag!
```

## Importing libraries

```python
import os, hashlib, exrex, itertools
from PIL import Image
```

## Funcion to bruteforce md5 with regex

```python
def md5_fuck(hash):
    for i in itertools.count(1):
        for s in exrex.generate('([0-9]x[0-9])'):
            if hashlib.md5(s.encode('utf-8')).hexdigest() == hash:
                return s
```

## Rename file (old_name, new_name)

```python
def rename_file(old_name, new_name):
    os.rename(old_name, new_name+'.jpg')
```


## Get all files in the current directory

```python
files = os.listdir()
```

## Iterate through the list of files and rename them

```python
# Initialize the variables to store the number of rows, columns and dimensions of the images
rows, cols, width, height = 0
# Iterate through the list of files to find the maximum row and column values, and also the dimensions of the images
for file in files:
    if file.endswith('.jpg'):
        row, col = file.split('x')[0], file.split('x')[1].split('.')[0]
        img = Image.open(file)
        if int(row) > rows:
            rows = int(row)
        if int(col) > cols:
            cols = int(col)
        if img.width > width:
            width = img.width
        if img.height > height:
            height = img.height
rows, cols += 1
```

## Initialize the blank image

```python
# Create a blank image with the determined dimensions
result = Image.new('RGB', (cols*width, rows*height))
```

## Iterate through the matrix and paste each image onto the blank image
    
```python
for i in range(rows):
    for j in range(cols):
        file = str(i) + 'x' + str(j) + '.jpg'
        if file in files:
            img = Image.open(file)
            result.paste(img, (j*width, i*height))
```

## Save the final image
    
```python
result.show()
#result.save('final.png')
```