from ex2_2 import average


class TestEx2_2:
    def test_average(self):
        assert average(1, 2, 3) == 2
        assert average(*[1, 2, 3]) == 2
