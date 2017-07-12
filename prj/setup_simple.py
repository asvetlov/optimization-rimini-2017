from Cython.Build import cythonize
from setuptools import setup

setup(name='prj',
      version='0.0.1',
      packages=['prj'],
      ext_modules=cythonize('prj/_mod.pyx'))
