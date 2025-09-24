#!/usr/bin/env python

"""
setup.py file for fr_drv_ng
"""

import sys
import os
import glob
import site
from setuptools.command.install import install
from distutils.command.build import build
from distutils.core import setup, Extension
import distutils.command.install as orig

swig_options = ['-module', 'fr_drv_ngx', '-c++', '-modern', '-modernargs', '-builtin']

libraries = ['classic_fr_drv_ngx']


def makeDistLibs():
    dirname = os.path.dirname(__file__)
    result = []
    if (sys.platform == "linux"):
        for lib in libraries:
            result.extend(glob.glob("." + dirname + "/lib" + lib + ".so.*"))
    if (sys.platform == "win32"):
        for lib in libraries:
#            result.extend(glob.glob("." + dirname + "/" + lib + ".dll"))
            result.extend(glob.glob(dirname + "\\dynamic\\" + lib + ".dll"))
    return result


dist_libraries = makeDistLibs()
my_data_files = (("lib/site-packages", dist_libraries)) if sys.platform == "win32" else ((".", ""))

static_link = "--staticlink" in sys.argv
py3 = "--py3" in sys.argv

extra_objects = ['{}/lib{}.a'.format(".", l) for l in libraries] if static_link is True else []

if (sys.platform == "linux"):
    usb = "--usb" in sys.argv
    bluetooth = "--bluetooth" in sys.argv
    if bluetooth:
        libraries.append("bluetooth")
    if usb:
        libraries.append("usb-1.0")
elif (sys.platform == "win32"):
    libraries.extend(['ws2_32', 'Shell32', 'Advapi32'])


class CustomBuild(build):
    def run(self):
        self.run_command('build_ext')
        build.run(self)


if (sys.version_info > (3, 0) and py3):
    swig_options.append('-py3')


class CustomInstall(install):
    user_options = install.user_options + [
        ('staticlink', None, 'link statically'),
        ('py3', None, 'build for python3 maybe faster than universal wrapper (works only if under python3)'),
        ('usb', None, 'link to libusb'),
        ('bluetooth', None, 'link to libbluetooth(linux only)')
    ]

    def initialize_options(self):
        install.initialize_options(self)
        self.staticlink = False
        self.bluetooth = False
        self.usb = False
        self.py3 = False

    def finalize_options(self):
        install.finalize_options(self)

    def run(self):
        self.run_command('build_ext')
        orig.install.run(self)


classic_python_fr_drv_ngx_module = Extension('_fr_drv_ngx', ['classic_api.i'],
                                            swig_opts=swig_options,
                                            # sources=['classic_interface_wrap.cxx'],
                                            include_dirs=['.'],
                                            extra_objects=extra_objects,
                                            libraries=libraries,
                                            library_dirs=['.'],
                                            runtime_library_dirs = [os.path.dirname(__file__)]
                                            )
classic_python_fr_drv_ngx_module_win = Extension('_fr_drv_ngx', ['classic_api.i'],
                                                 swig_opts=swig_options,
                                                 include_dirs=['.'],
                                                 extra_objects=extra_objects,
                                                 libraries=libraries,
                                                 library_dirs=[os.path.join(os.path.dirname(__file__), "dynamic")],
                                                 )

setup(name='fr_drv_ngx',
      version='1.0',
      cmdclass={'build': CustomBuild, 'install': CustomInstall},
      description="""Simple swig wrapper for classic_fr_drv_ngx driver""",
      ext_modules=[classic_python_fr_drv_ngx_module_win if sys.platform == "win32" else classic_python_fr_drv_ngx_module],
      py_modules=["fr_drv_ngx"],
      data_files=[my_data_files],
      )
