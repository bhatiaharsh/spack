# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Mummi(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://code.ornl.gov/v33/pilot2-splash-app"
    git      = "git@code.ornl.gov:v33/pilot2-splash-app.git"

    version('0.3b.0', tag='v0.3b.0') #commit='527f44e4a543f0e44daeab5d1375ce8c610eb9a0')
    version('0.2.0', tag='v0.2.0') #commit='372e85318181530731f191b5a48b747f60bfadd2')
    version('develop', branch='develop')
    version('python3', branch='python3')

    build_directory = 'mummi'

    extends('python@3.7.3')

    # build dependencies
    depends_on('cmake@3.14.5',  type='build')
    depends_on('swig@3.0.12',  type='build')

    # generic
    depends_on('py-numpy@1.16.4')
    depends_on('py-scipy@1.3.0')
    
    # ml
    depends_on('cudnn@7.5.1-10.1-ppc64le')			      	#TODO: these settings are for powerpc
    depends_on('faiss@1.5.3 +python')
    #depends_on('py-theano@1.0.4 +cuda ^cudnn@7.5.1-10.1-ppc64le')	#TODO: these settings are for powerpc
    #depends_on('py-theano@1.0.4 +cuda')
    depends_on('py-keras@2.2.4')
    #depends_on('py-h5py@2.9.0~mpi ^hdf5~mpi+hl')

    # analysis
    depends_on('talass@process-statistics')
    depends_on('py-mdanalysis-mummi@mda0.19.2_with_ddcmd')
    depends_on('py-scikit-learn')
    depends_on('py-matplotlib@3.0.2')

    # gromacs
    depends_on('fftw@3.3.8')			        #TODO: these settings are for powerpc
    depends_on('gromacs@2019.3 ~mpi~cuda~rdtscp simd=IBM_VSX')		#TODO: these settings are for powerpc

    # databroker
    depends_on('databroker@0.6.1 +python build_type=Debug')	    	#TODO: change to release when dbr is fixed

    # flux
    depends_on('flux-sched@0.8.0 +cuda')
