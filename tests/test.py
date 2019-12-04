

import pytest

from main import multiply


class TestClass():
    @pytest.mark.parametrize("num", [(3, 4),
                                     (3.0, 4.0)])
    def test_multiply(self, num):
        if not isinstance(num[0], int) or not isinstance(num[1], int):
            pytest.raises(ValueError)
        else:
            multiply(num[0], num[1])
