#!/usr/bin/env python3

import argparse
import base64
import json
import zlib
from cryptography.fernet import Fernet

def encode(str_to_encode: str) -> str:
    key = Fernet.generate_key()
    f = Fernet(key)
    enc = f.encrypt(bytes(str_to_encode, encoding="utf-8"))
    d = {
        "msg": str(enc, encoding="utf-8"),
        "key": str(key, encoding="utf-8"),
    }
    compressed = zlib.compress(
        bytes(json.dumps(d), encoding="utf-8"),
        level=zlib.Z_BEST_COMPRESSION
    )
    b64_bytes = base64.b64encode(compressed)
    b64_str = str(b64_bytes, encoding="utf-8")
    return b64_str

def decode(str_to_decode: str) -> str:
    compressed = base64.b64decode(bytes(str_to_decode, "utf-8"))
    d = json.loads(zlib.decompress(compressed))
    f = Fernet(bytes(d["key"], encoding="utf-8"))
    return f.decrypt(
        bytes(d["msg"], encoding="utf-8")
    ).decode("utf-8")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='encode.py',
        description=f'Encode into base64 string')
    parser.add_argument("input", help="input text or filename if using -f flag")
    parser.add_argument('-f', '--file', action='store_true', help="flag to read input from file")
    parser.add_argument('-d', '--decode', action='store_true', help="flag to decode")
    args = parser.parse_args()
    text = args.input
    if args.file:
        with open(args.input, "r") as f:
            text = f.read()
    
    if args.decode:
        decoded_text = decode(text)
        print(decoded_text)
        assert(decode(encode(decoded_text)) == decoded_text)
    else:
        encoded_text = encode(text)
        print(encoded_text)
        assert(decode(encoded_text) == text)
