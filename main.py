#!/usr/bin/env python3
"""make.fun entry: writes the bundled text to /output/entry.txt. Deterministic, no network."""
import os, shutil
os.makedirs("/output", exist_ok=True)
shutil.copyfile(os.path.join(os.path.dirname(__file__), "entry.txt"), "/output/entry.txt")
print("entry.txt written")
