from src.tools import Tools

def test_reverse_text():
    tools = Tools()
    assert tools.reverse_text("apple") == "elppa"
    assert tools.reverse_text("") == ""
    assert tools.reverse_text("A") == "A"[::-1]