import sys
from os import listdir
from os.path import isfile, join, splitext


def parse_argument(argument, query):
	if query in argument:
		query_idx = argument.index(query)
		if query_idx + 1 <= len(argument):
			return argument[query_idx + 1]
	return False


def parse_argument_int(argument, query):
	return int(parse_argument(argument, query))


def get_file_list(path, extension=None):
	if extension is None:
		file_list = [path + f for f in listdir(path) if isfile(join(path, f))]
	else:
		file_list = [path + f for f in listdir(path)
				if isfile(join(path, f)) and splitext(f)[1] == extension]
	file_list.sort()
	return file_list


def get_file_list_from_custom_format(path, format):
	number_of_files = len(get_file_list(path, splitext(format)[1]))
	file_list = []
	for i in range(number_of_files):
		file_list.append("%s/%s" % (path, format % i))
	return file_list
