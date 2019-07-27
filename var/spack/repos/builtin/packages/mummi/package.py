# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install mummi
#
# You can edit this file again by typing:
#
#     spack edit mummi
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Mummi(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://code.ornl.gov/v33/pilot2-splash-app"
    git      = "git@code.ornl.gov:v33/pilot2-splash-app.git"

    version('0.3b.0', tag='v0.3b.0') #commit='527f44e4a543f0e44daeab5d1375ce8c610eb9a0')
    version('0.2.0', tag='v0.2.0') #commit='372e85318181530731f191b5a48b747f60bfadd2')
    version('develop', branch='develop')

    #version('1.0.1', tag='v1.0.1')
    #version('2014-10-08', commit='9d38cd4e2c94c3cea97d0e2924814acc')
    #version('1.0', 'f43fb8126c138db96b489655914ed2bd5a469412')

    build_directory = 'pysplash'

    extends('python@3.7.3')

    # build dependencies
    depends_on('cmake@3.14.5',  type='build')
    depends_on('swig@3.0.12',  type='build')

    # generic
    depends_on('py-numpy@1.16.4')
    depends_on('py-scipy@1.3.0')
    
    # ml
    depends_on('cudnn@7.5.1-10.1-ppc64le')
    depends_on('faiss@1.5.3 +python')
    depends_on('py-theano@1.0.4 +gpu ^cudnn@7.5.1-10.1-ppc64le')
    depends_on('py-keras@2.2.4')

    # analysis
    depends_on('talass@process-statistics')
    depends_on('py-mdanalysis-mummi@mda0.19.2_with_ddcmd')
    depends_on('py-scikit-learn')
    depends_on('py-matplotlib@3.0.2 +ipython ~tk')

    # gromacs
    depends_on('fftw@3.3.8 simd=vsx')
    depends_on('gromacs@2019.3+mpi~cuda simd=IBM_VSX') # ^fftw@3.3.8 simd=vsx')

    # databroker
    depends_on('databroker@0.6.1 +python build_type=Debug')

    # flux
    depends_on('flux-sched@0.7.1 +cuda') 
