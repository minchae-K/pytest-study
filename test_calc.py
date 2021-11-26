#from calc import Calc

import pytest

# @pytest.fixture
# def calc():
#	c = Calc()
#	return c

#conftest.py에서 이미 설정해두었기 때문에 별도의 선언 없이 진행이 가능함

def test_add_two_numbers(calc):
	#c = Calc()
	#res = c.add(4,5) #add의 입력 인수가 3개로 변경되었기 때문에 error 발생
	res = calc.add(4,5,6)
	
	assert res == 15

def test_sub_two_numbers(calc):
	#c = Calc()
	res = calc.sub(5,1)

	assert res == 3

def test_mul_by_zero_raises_exception(calc):
	
	with pytest.raises(ValueError): #ValueError가 발생하기를 바라는 code
		calc.mul(3,0) #0이 입력되었기 때문에 ValueError가 발생하는 것
