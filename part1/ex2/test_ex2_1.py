from ex2_1 import sum


class TestEx2_1:
    def test(self):
        assert sum([1, 2, 3]) == 6
        assert sum(1, 2, 3) == 6
        assert sum(*[1, 2, 3]) == 6
        assert sum([1, 2, 3], 4) == 10
        assert sum([1, 2, 3], 4, 5) == 15
        assert sum(4, [1, 2, 3]) == 10
        assert sum(4, 5, [1, 2, 3]) == 15
