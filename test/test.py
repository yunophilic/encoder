#!/usr/bin/env python3

import os
from pathlib import Path

import encoder

if __name__ == "__main__":
    print("Run test with sample data ...")
    SAMPLE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample")
    directory = Path(SAMPLE_PATH)
    for file in directory.iterdir():
        if file.is_file():
            text = file.read_text()
            encoded = encoder.encode(text)
            assert(encoder.decode(encoded) == text)
    print("All test passed")
