import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from fibs import fibs


class TestFibs:


    def test_first_10_numbers(self):
        expected = [ 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        result = fibs(10)
        assert result == expected

    def test_edge_cases(self):
        assert fibs(0) == []
        assert fibs(1) == [1]
        assert fibs(2) == [1, 1]

    def test_negative_input(self):
        with pytest.raises(ValueError, match="n должно быть неотрицательным числом"):
            fibs(-1)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])