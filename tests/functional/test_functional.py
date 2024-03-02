import pytest

pytestmark = pytest.mark.parametrize("input", "expected_result", [
    ("1+1", 2),
    ("1+2", 3)
])


class FunctionalTest:
    class_variable = 123

    def test_example(self, input, expected_result):
        assert self.class_variable == 123
        assert eval(input) == expected_result
