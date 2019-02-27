import numpy as np
import copy

class solution():
	'''
	enter 1-9 --> python 0-8
	'''
	def __init__(self, dim=3):
		self.total_num = 0
		self.target = None
		self.dim = dim
		self.record = []
		self.others = [ i for i in range(self.dim*self.dim)]
		if self.dim ==3:
			self.rules = [1,2,5]  ## others for dim-n
		elif self.dim ==4:
			self.rules = [1,2,5,10,13]
		else:
			print ("Sorry, only for dim=3 or 4, please enter again")
			return None
		self.library = [ [] for i in range(self.dim*self.dim)]

		for i in range(self.dim*self.dim):
			i_ID = [i//self.dim, i%self.dim]
			for j in range(self.dim*self.dim):
				if i == j:
					continue
				j_ID = [j//self.dim, j%self.dim]
				distance = (i_ID[0]-j_ID[0])**2 + (i_ID[1]-j_ID[1])**2
				if distance in self.rules:
					self.library[i].append(j)


	def refresh(self):
		self.target = None
		self.record = []
		self.others = [ i for i in range(self.dim*self.dim)]


	def pick(self):
		_candidates = list(set(self.others).intersection(self.library[self.target]))
		if _candidates == []:
			return ''
		else:
			return np.random.choice(_candidates)
		

	def generate(self, head, length=4):
		self.refresh()
		self.target = int(head)-1
		self.record.append(self.target)
		self.others.remove(self.target)

		count = length
		while count-1:
			if not str(self.target).isdigit():
				break
			self.target = self.pick()
			if self.target != '':
				self.record.append(self.target)
				self.others.remove(self.target)
			count -= 1

		password = ''
		for i in self.record:
			password += str(i+1)

		while len(password) != length:
			password = self.generate(head,length)

		return password


	def total(self, min_length=4):
		
		self.refresh()
		self.results = {}
		heads = [i+1 for i in range(self.dim*self.dim//2+1)]
		lengths = [ j for j in range(min_length, self.dim*self.dim+1)]
		for length in lengths:
			self.r1 = length
			for head in heads:
				self.r2 = head
				if head == self.dim*self.dim//2+1:
					tmp = self.generate(head, length)
					self.results[tmp] = '1'
					self.results[tmp+'x'] = ''
				else:
					self.results[self.generate(head, length)] = '1'
		self.refresh()
		return len(self.results.keys())


	def recursive_total(self, nodes, out=[]):
		'''
		low efficient, may be tree search can help get the result
		'''
		if nodes == []:
			return 1
		for i in nodes:
			# _ = copy.copy(nodes[i])
			# recursive_total(copy.copy(self.library[i]).remove(i))
			out.append(i)
			self.total_num += self.recursive_total(list(set(self.library[i]).intersection(set(out))))






if __name__ == '__main__':

	# ## 3*3 keyboards
	# buttons = [ i for i in range(1,10)]
	# _solution = solution(dim=3)

	# ## question-1
	# for i in range(4,10):
	# 	print ('length',i, 'password:\t', _solution.generate(head=np.random.choice(buttons), length=i))

	# ## question-2
	# ## Assume the password min length=4, we have:
	# print ("Total passwords (len>4) in 3*3 keyboards:\t", _solution.total(min_length=4))
	# ## OR
	# print ("Total passwords (len>4) in 3*3 keyboards:\t", _solution.total2(min_length=4))


	# ## question-3
	# _solution_4 = solution(4)
	# print ("Total passwords (len>4) in 4*4 keyboards:\t", _solution_4.total(min_length=4))

	_s = solution()
	_s.recursive_total([0,1,2,3,4,5,6,7,8])
	print ('total:', _s.total_num)
