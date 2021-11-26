from calc import Calc

def test_add_two_numbers():
	c = Calc()
	#res = c.add(4,5) #add의 입력 인수가 3개로 변경되었기 때문에 error 발생
	res = c.add(4,5,6)
	
	assert res == 15
