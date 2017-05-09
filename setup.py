#!/usr/bin/env python
from __future__ import division, absolute_import, print_function

from numpy.distutils.core import Extension

pstl = Extension('pystl', sources = ['stl.f'])
    
if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(name = 'pystl',
	      version = '1.0',
	      author='Harutyun Khachatryan',
	      author_email='kh_harut@yahoo.com',
	      url='https://github.com/khharut/pystl',
	      license='GPL-3',
	      description = 'Loess smoother for python',
	      ext_modules = [pstl],
	      zip_safe=False)
