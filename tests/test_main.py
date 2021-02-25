from example import main


TEST_COW = """
___________________
< Moo! >
 -------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""

def test_main():
    assert TEST_COW == main.say("Moo!")
