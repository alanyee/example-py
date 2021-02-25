# -*- coding: utf-8 -*-

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
 
def main(cowsay="Moo!"):
    """Example"""
    print(say(cowsay))

if __name__ == "__main__":
    main()
