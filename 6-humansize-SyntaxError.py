SUFFIXES={1000:['KB','MB','GB','TB','PB','EB','ZB','YB'],
		  1024:['KiB','mIB','GiB','TiB','PiB','EiB','ZiB','YiB']}

def approximate_size(size,a_kilobyte_is_1024_bytes=True):
	'''Convert a file size to human-readable form.
	Keyword arguments: size-file size in bytes
					   a_kilobyte_is_1024_bytes-if true(default),use multiples of 1024
					   							if false, use multiples of 1000
	Returns: string
	'''
	if size <0:
		print('Number must be non-negative')
		pass

	multiples=1024 if a_kilobyte_is_1024_bytes else 1000

	for suffix in SUFFIXES(multiples):
		size = size / multiples
		if size < multiples:
			return '{0:.1f} {1}'.format(size,suffix)

		raise ValueError('Number is too large')

	'''if __name__=='__main__':'''
print(approximate_size(-100000000000,False))
print(approximate_size(100000000000))