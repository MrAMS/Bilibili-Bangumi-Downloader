# Bilibili Bangumi Downloader
#
# Attention!
# Must work with you-get

# default settings

LINK_PREFIX = 'https://www.bilibili.com/bangumi/play/ep'
SAVE_FOLDER = '/Users/santiego/Downloads'
COOKIE_FOLDER = '/Users/santiego/Library/Application\ Support/Firefox/Profiles/qbrdrjqq.default-release/cookies.sqlite'
MAX_TRY_TIMES = 10

import os, sys, timeit


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
	return '\033[1;{0};{2}m{1}\033[0m'.format(color, msg, background)

def print_log(msg, newline=True):
	sys.stdout.write(msg+'\n' if newline else msg)

def download(path, url, cookie):
	return os.system("you-get -o {0} {1} -c {2} -l".format(path, url, cookie))

def run():
	print_log(log('Bilibili Bangumi Downloader :)', CYAN))
	print_log(log('By Santiego', WHITE))
	print_log(log('work with you-get', WHITE))
	print_log(log('ep id', BLACK, 47))
	print_log(log('(e.g. ep21272, check your video link and input the ep id to download)', CYAN))
	ep_id=int(str(input())[2:])
	print_log(log('Save in?', BLACK, 47), False)
	print_log(log('(or skip)', CYAN))
	path = input() \
		or SAVE_FOLDER
	print_log(log('Cookies.sqlite path', BLACK, 47))
	print_log(log('(input Firefox\'s Cookies.sqlite file path to download 1080+, or skip)', CYAN))
	cookie = input() \
		or COOKIE_FOLDER
	time_s = timeit.default_timer()
	tried_times=0
	while download(path, LINK_PREFIX+str(ep_id), cookie) != 0 and tried_times <= MAX_TRY_TIMES:
		print_log(log('Fail to download.', 31))
		print_log(log('Trying again...', 31))
		tried_times += 1
	print_log(log('Done in {} mins.'.format(round((timeit.default_timer()-time_s)/60),2), CYAN))

if __name__ == '__main__':
	run()
