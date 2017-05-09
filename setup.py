#!/usr/bin/env python
from __future__ import division, absolute_import, print_function

from numpy.distutils.core import Extension

pstl = Extension('pystl', sources = ['stl.f'])
    
if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(name = 'pystl',
	      version = '1.0',
	      author='Harutyun Khachatryan',
	      author_email='harutyun.khachatryan@monitis.com',
	      url='http://www.monitis.com/',
	      license='Monitis Inc.',
	      description = 'Loess smoother for python',
	      ext_modules = [pstl],
	      zip_safe=False)