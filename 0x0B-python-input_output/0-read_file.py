#!/usr/bin/python3
# 0-read_file.py


def read_file(filename=""):
    with open(filename, mode="r", encoding="UTF-8") as file:
        print(f.read(), end="")
