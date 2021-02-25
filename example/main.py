# -*- coding: utf-8 -*-
import sys

COW = """
___________________
< {} >
-------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||
"""

def say(cowsay):
    return COW.format(cowsay)
 
def main():
    """Example"""
    cowsay = "Moo!"
    if len(sys.argv) > 1:
        cowsay = sys.argv[1]
    print(say(cowsay))

if __name__ == "__main__":
    main()
