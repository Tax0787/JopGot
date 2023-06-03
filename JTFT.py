from Tools import s, cd, gets, sets, error, o
from os import getcwd as pwd
from os import listdir as dir
from os import mkdir
from os.path import isfile, isdir, islink

NotSupportError = error('NotSupportError')
PersonalDevSystemError = error('PersonalDevSystemError')
JTFTSyntaxError = error('JTFTSyntaxError')

Arc = lambda x : None
UnArc = lambda x, y : None

def ArcLosic(x: str):
	if isfile(x):
		pass  #bin인지 txt인지 확인 필요
	elif isdir(x):
		return Arc(x)
	elif islink(x):
		raise NotSupportError("We didn't support compress link")
	else:
		raise PersonalDevSystemError("file is delete but we found")


def Arc(root: str):
	path = pwd()
	cd(root)
	ret = {x: ArcLosic(x) for x in dir()}
	cd(path) 
	return ret


def UnArcLosic(name: str, value: str):
	x = type(value)
	match x:
		case dict:
			if not isdir(name): mkdir(name)
			UnArc(value)
		case str:
			with o(name, 'w') as f:
				f.write(value)
		case _:
			raise JTFTSyntaxError(f"Like-Type Error that JTFT didn't support type {x}")

def UnArc(path : str, jftf: dict):
	path2 = pwd()
	cd(path)
	for name, value in jtft.items():
		UnArcLosic(name, value)
	cd(path2)

def tfting(file : str, dir : str):
	ret = Arc(dir)
	ret = sets (file, ret)
	return ret
	
def untfting(file : str, path : str):
	ret = gets(file)
	ret = UnArc(path, ret)
	return ret

def test():
	print("None Event")

def main():
	return test()

if __name__ == '__main__': main()