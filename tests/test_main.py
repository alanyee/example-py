from example import main


TEST_COW = """
___________________
< {} >
-------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||
"""

def test_main():
    assert TEST_COW.format("Moo!") == main.say("Moo!")
