# Py-Fry 5/17/2013
# Matt Zychowski
# A simple class that will encode a^(-1) as an infinite
# repeating decimal, if a is an integer > 1.

# Make cycles in your numbers!

class Recip:

	def __init__(self, a):
		self.a = a
		self.split_index = 0
		self.digit_array = []
		
		if (a <= 1):
			raise Exception("Must be a positive integer > 1")
		
		rem_history = []
		
		#start long division for 1/a
		remainder = 10
		while (True):
			next_digit = 0
			while ( remainder >= a*(next_digit+1) ):
				next_digit += 1
			self.digit_array.append(next_digit)
			rem_history.append(remainder)
			
			#generate a new remainder for long division
			remainder -= a*next_digit
			if remainder != 0:
				remainder *= 10
			else:
				#non-repeating decimal, stop
				self.split_index = len(self.digit_array)
				return
				
			for i in range(len(rem_history)):
				#if we find the same remainder in the history, we've found a
				#long division cycle and can stop
				if rem_history[i] == remainder:
					self.split_index = i
					return
		#end while
			
	def toString(self):
		sb = "1/" + str(self.a) + " = \n0."
		for i in range(self.split_index):
			sb += str(self.digit_array[i])
		if self.split_index == len(self.digit_array):
			return sb
		for i in range(2):
			sb += " "
			for i in range(self.split_index, len(self.digit_array)):
				sb += str(self.digit_array[i])
		sb += "..."
		return sb