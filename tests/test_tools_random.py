from src.tools import Tools

def test_get_random_number():
    tools = Tools()

    for _ in range(20):
        n = tools.get_random_number(1, 5)
        assert 1 <= n <= 5