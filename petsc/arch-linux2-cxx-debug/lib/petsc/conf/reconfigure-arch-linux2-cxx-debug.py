#!/usr/bin/python
if __name__ == '__main__':
  import sys
  import os
  sys.path.insert(0, os.path.abspath('config'))
  import configure
  configure_options = [
    '--prefix=/home/mito/usrLocal',
    '--with-clanguage=c++',
    '--with-cxx=g++',
    '--with-fc=gfortran',
    '--with-mpi=0',
    '-download-fblaslapack',
    'PETSC_ARCH=arch-linux2-cxx-debug',
  ]
  configure.petsc_configure(configure_options)
