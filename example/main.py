# -*- coding: utf-8 -*-
import sys

COW = r"""
___________________
< {} >
-------------------
        \   ^__^
         \  (o )\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""

def say(cowsay: str) -> str:
    """Interpolates what the cow says
    Reference: https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html
    :param cowsay: string for what the cow says
    :type cowsay: str
    
    :return: cow ascii art interpolated with cowsay
    :rtype: str
    """
    return COW.format(cowsay)
 
def main() -> None:
    """Print what the cow says"""
    cowsay = "Moo!"
    if len(sys.argv) > 1:
        cowsay = sys.argv[1]
    print(say(cowsay))

if __name__ == "__main__":
    main()
