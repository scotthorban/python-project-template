import pytest

pytestmark = pytest.mark.parametrize("input_value, expected_result", [
    ("1+1", 2),
    ("1+2", 3)
])


class TestFunctional:
    """
    Example Functional test class
    """
    class_variable = 123

    def test_example(self, input_value, expected_result):
        """
        Example Functional test
        """
        assert self.class_variable == 123
        assert eval(input_value) == expected_result
