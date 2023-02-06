## Importing libraries


```python
import functools as ft, requests, hashlib, os, sys,exrex, itertools, base64

```

## Escape Encoding


```python
flag = [89, 111, 117, 71, 111, 116, 84, 104, 101, 70, 108, 64, 103]
flag = "".join(map(chr, flag))
print(flag)
```

    YouGotTheFl@g
    

## Strange Strings


```python
file1 = base64.b64decode(open('file1.txt', 'r').read()).decode('utf-8')
file2 = base64.b64decode(open('file2.txt', 'r').read()).decode('utf-8')
flag = "".join([file1[i] for i in range(len(file1)) if file1[i] == file2[i]])
print(flag)
```

    Flag{YoU_DiD_GooD_MaTcHinG}
    
