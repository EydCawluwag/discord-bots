class func:
	#trig
	def sin(opposite, hypotenuse):
		return opposite/hypotenuse

	def cos(adjacent, hypotenuse):
		return adjacent/hypotenuse
	
	def tan(opposite, adjacent):
		return opposite/adjacent
	
	def sec(hypotenuse, adjacent):
		return hypotenuse/adjacent

	def cosec(hypotenuse, opposite):
		return hypotenuse/opposite

	def cot(adjacent, opposite):
		return adjacent/opposite

def driver(arg):
	if arg[0]=='?sin':return func.sin(int(arg[1]),int(arg[2]))
	elif arg[0]=='?cos':return func.cos(int(arg[1]),int(arg[2]))
	elif arg[0]=='?tan':return func.tan(int(arg[1]),int(arg[2]))
	elif arg[0]=='?sec':return func.sec(int(arg[1]),int(arg[2]))
	elif arg[0]=='?cosec':return func.cosec(int(arg[1]),int(arg[2]))
	elif arg[0]=='?cot':return func.cot(int(arg[1]),int(arg[2]))
 
