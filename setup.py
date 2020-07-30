from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

sourcefiles = ['array_sum.pyx']
ext_modules = [Extension("array_sum_c", 
                          sourcefiles
                          )]

setup(
  name = 'Arraysum',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)