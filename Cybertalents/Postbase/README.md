# [Postbase](https://cybertalents.com/challenges/cryptography/postbase)
### 🛢Category: Cryptography
### 🌟 50 points
### 👓Level: Easy
### Description:

```
We got this letters and numbers and don't understand them. Can you? R[corrupted]BR3tCNDUzXzYxWDdZXzRSfQ==
```


## 

```python
#!/usr/bin/env python3

import base64, exrex

def Base64_D(base64_message):
    global done
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    if message[:4].upper() =="FLAG" :
        print("\n"+message)

def main():
    for i in B64hash:
        try:
            Base64_D(str(i))
        except:
            pass

if __name__ == "__main__":
    B64hash = exrex.generate('R([A-Za-z0-9+])+BR3tCNDUzXzYxWDdZXzRSfQ==')
    main()
```
