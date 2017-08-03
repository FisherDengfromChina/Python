SUFFIXES={1000:['KB','MB','GB','TB','PB','EB','ZB','YB'],
		  1024:['KiB','MiB','GiB','TiB','PiB','EiB','ZiB','YiB']}

def human-readable(size,size_format):
	if size < 0:
		print('Size must be over zero')
		pass

	if size_format:
		multiple = 1024
	elif not size_format:
		multiple = 1000
		pass

	for suffix in SUFFIXES(multiple):
		size = size/multiple
		pass