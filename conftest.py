import pytest
from calc import Calc

@pytest.fixture
def calc():
	calc = Calc()
	return calc
