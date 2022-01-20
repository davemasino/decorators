from main import say_whee

def test_whee(capsys):
    say_whee()
    captured = capsys.readouterr()
    assert captured.out == "Something is happening before the function is called.\nWhee!\nSomething is happening after the function is called.\n"
