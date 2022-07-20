from ex4 import hex_output
from ex4_1 import hex_output as hex_output_1


class TestEx4:
    def test(self):
        assert hex_output("30") == 48

    def test_1(self):
        assert hex_output_1("30") == 48
