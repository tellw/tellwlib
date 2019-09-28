import random

def gen_rand_charnum_seq(leng):
	"""生成定长随机字符串（字符串由数字或字母组成）.

	Args:
		leng: 随机字符串的长度.

	Returns:
		rec: 该定长随机字符串.
	"""
	char = []
	for i in range(65, 65+26):
	    char.append(chr(i))
	for i in range(97, 97+26):
	    char.append(chr(i))
	for i in range(0, 10):
	    char.append(str(i))
	rec = ''
	for i in range(leng):
	    rc = random.choice(char)
	    rec += rc
	print('generated random string is '+rec)
	return rec