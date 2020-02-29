import os

# Attention!
# Must work with you-get

# default settings

LINK_PREFIX = 'https://www.bilibili.com/bangumi/play/ep'
SAVE_FOLDER = '/Users/santiego/Movies/番/轻音少女.第一季'
COOKIE_FOLDER = '/Users/santiego/Library/Application\ Support/Firefox/Profiles/qbrdrjqq.default-release/cookies.sqlite'
MAX_TRY_TIMES = 4

def log(msg, color):
	return '\033[0;{};40m{}\033[0m'.format(color, msg)

def download(path, url, cookie):
	print("you-get -o {0} {1} -c {2}".format(path, url, cookie))
	return os.system("you-get -o {0} {1} -c {2}".format(path, url, cookie))

def run():
	print(log('Bilibili Bangumi Downloader :)', 32))
	print(log('work with you-get', 32))
	op=int(str(input(log('*ep id(e.g. ep21272)?', 36)))[2:])
	ed=op+int(input(log('how many?', 36)) or 1)
	path = input(log('Save in?', 36)) \
		or SAVE_FOLDER
	cookie = input(log('Cookies.sqlite?', 36)) \
		or COOKIE_FOLDER
	for cur in range(op, ed+1):
		print(log('Downloading ep{}...'.format(cur), 33))
		for i in range(1, MAX_TRY_TIMES+1):
			if(download(path, LINK_PREFIX+str(cur), cookie) == 0):
				break
			else:
				print(log('Fail to download.', 31))
				print(log('Trying again...', 33))

if __name__ == '__main__':
	run()
