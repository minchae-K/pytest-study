from functools import reduce

class Calc:
	#두가지 숫자 더하는 assertion 예제
	#def add(self, a, b):
		#return 9
	
	#세가지 숫자 더하는 assertion 예제
	def add(self, a, b, c):
		return 15

	def sub(self, a, b):
		return 3

	def mul(self, *args):

		if not all(args): #all() : 모든 요소가 참일 경우 True를 return하는 함수
			raise ValueError
		return reduce(lambda x, y: x*y, args)

	def avg(self, it, ut = None):
		if not ut:
			ut = max(it)
		_it = [x for x in it if x <= ut]

		return sum(_it)/len(_it)

