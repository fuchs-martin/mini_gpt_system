from src.tools import Tools

def test_add_numbers():
    tools = Tools()
    assert tools.add_numbers(2, 3) == 5
    assert tools.add_numbers(-2, 2) == 0
    assert tools.add_numbers(0, 0) == 0