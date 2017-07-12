import os
from distutils.command.build_ext import build_ext
from distutils.errors import (CCompilerError, DistutilsExecError,
                              DistutilsPlatformError)

from setuptools import Extension, setup

try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

ext = '.pyx' if USE_CYTHON else '.c'


if bool(os.environ.get('PROFILE_BUILD')):
    macros = [('CYTHON_TRACE', '1')]
else:
    macros = []

extensions = [Extension('prj._mod', ['prj/_mod' + ext], define_macros=macros)]

if USE_CYTHON:
    if bool(os.environ.get('PROFILE_BUILD')):
        directives = {"linetrace": True}
    else:
        directives = {}
    extensions = cythonize(extensions, compiler_directives=directives,
                           gdb_debug=True)


class BuildFailed(Exception):
    pass


class ve_build_ext(build_ext):
    # This class allows C extension building to fail.

    def run(self):
        try:
            build_ext.run(self)
        except (DistutilsPlatformError, FileNotFoundError):
            raise BuildFailed()

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
        except (CCompilerError, DistutilsExecError,
                DistutilsPlatformError, ValueError):
            raise BuildFailed()


args = dict(
    name='prj',
    version='0.0.1',
    packages=['prj'],
    ext_modules=extensions,
    cmdclass=dict(build_ext=ve_build_ext))

try:
    setup(**args)
except BuildFailed:
    print("************************************************************")
    print("Cannot compile C accelerator module, use pure python version")
    print("************************************************************")
    del args['ext_modules']
    del args['cmdclass']
    setup(**args)
