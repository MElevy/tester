class test:
	def __init__(self,testName):
		self.testName=testName
		self.testno=0
	def test(self,code,output):
		import sys
		import io
		import time
		sT=time.time()
		old_stdout = sys.stdout
		new_stdout = io.StringIO()
		sys.stdout = new_stdout
		exec(code)
		result = new_stdout.getvalue()
		sys.stdout = old_stdout
		eT=time.time()
		tt=eT-sT
		self.testno+=1
		if str(result)==str(output):
			print(f'Success: Test Name: {self.testName}, Test Number: {self.testno}')
			print('-'*20)
			print('code')
			print('-'*20)
			print(f'{code}')
			print('-'*20)
			print('results')
			print('-'*20)
			print(f'{result}')
			print('-'*20)
			print('code list: results')
			print('-'*20)
			print(output.split('\n'))
			print('-'*20)
			print(f'Execution time: {round(tt,7)}')
			print('-'*20)
			print('\n')
			return True
		else:
			print(f'Fail: Test Name: {self.testName}, Test Number: {self.testno}')
			print('-'*20)
			print('code')
			print('-'*20)
			print(f'{code}')
			print('-'*20)
			print('expected results')
			print('-'*20)
			print(f'{output}')
			print('-'*20)
			print('actual results')
			print('-'*20)
			print(f'{result}')
			print('-'*20)
			print('code lists: expected results')
			print('-'*20)
			print(output.split('\n'))
			print('-'*20)
			print('code lists: actual results')
			print('-'*20)
			print(result.split('\n'))
			print('-'*20)
			print(f'Execution time: {round(tt,7)}')
			print('-'*20)
			print('\n')
			return False
	def qtest(self,code, output):
		import sys
		import io
		self.testno+=1
		old_stdout = sys.stdout
		new_stdout = io.StringIO()
		sys.stdout = new_stdout
		exec(code)
		result = new_stdout.getvalue()
		sys.stdout = old_stdout
		if str(result)==str(output):
			return True
		else:
			return False