#!/usr/bin/env python3

import atheris

def TestOneInput(data):
    text = str(data, encoding="utf-8")
    encoded = encode(text)
    assert(decode(encoded) == text)

if __name__ == "__main__":
    with atheris.instrument_imports():
        from encoder import encode, decode
        import sys

    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()