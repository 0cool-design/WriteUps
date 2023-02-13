import base64, exrex, re

def decode_base64(base64_message):
    pattern = re.compile(r'^Flag\{\w+\}$', re.IGNORECASE)
    base64_bytes = base64_message.encode('ascii')
    decoded_bytes = base64.b64decode(base64_bytes)
    decoded_message = decoded_bytes.decode('ascii')
    if pattern.match(decoded_message):
        return decode_base64 is not None

def main():
    b64_hashes = exrex.generate('R([A-Za-z0-9+/])+BR3tCNDUzXzYxWDdZXzRSfQ==')
    for hash_value in b64_hashes:
        try:
            decode_base64(str(hash_value))
        except:
            pass

if __name__ == "__main__":
    main()
    