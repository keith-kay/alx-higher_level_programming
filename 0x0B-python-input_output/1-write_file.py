#!/usr/bin/python3
# 1-write_file.py


def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="UTF-8") as file:
        return f.write(text)
