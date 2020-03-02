import os, sys

# Attention!
# Must work with you-get

# default settings

LINK_PREFIX = 'https://www.bilibili.com/bangumi/play/ep'
SAVE_FOLDER = '/Users/santiego/Downloads'
COOKIE_FOLDER = '/Users/santiego/Library/Application\ Support/Firefox/Profiles/qbrdrjqq.default-release/cookies.sqlite'
MAX_TRY_TIMES = 4

WHITE = 37
BLACK = 30
CYAN = 31
GREEN = 32
YELLOW = 33
BLUE = 34
MAGENTA = 35
CYAN = 36
LIGHT_GRAY = 37

def log(msg, color, background=40):
	return '\033[0;{0};{2}m{1}\033[0m'.format(color, msg, background)

def print_log(msg, newline=True):
	sys.stdout.write(msg+'\n' if newline else msg)

def download(path, url, cookie):
	return True
	return os.system("you-get -o {0} {1} -c {2} -l".format(path, url, cookie))

def run():
	print_log(log('Bilibili Bangumi Downloader :)', CYAN))
	print_log(log('By Santiego', WHITE))
	print_log(log('work with you-get', WHITE))
	print_log(log('ep id', BLACK, 47), False)
	print_log(log('(e.g. ep21272)?', CYAN))
	ep_id=int(str(input())[2:])
	print_log(log('Save in?', CYAN))
	path = input() \
		or SAVE_FOLDER
	print_log(log('Cookies.sqlite path', BLACK, 47), False)
	print_log(log('(Firefox\'s Cookies.sqlite file path)', CYAN))
	cookie = input() \
		or COOKIE_FOLDER
	while download(path, LINK_PREFIX+str(ep_id), cookie) != 0:
		for i in range(1, MAX_TRY_TIMES+1):
			if(download(path, LINK_PREFIX+str(ep_id), cookie) == 0):
				print_log(log('Done.', CYAN))
				return
			else:
				print_log(log('Fail to download.', 31))
				print_log(log('Trying again...', 31))

if __name__ == '__main__':
	run()
