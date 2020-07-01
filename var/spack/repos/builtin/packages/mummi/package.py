# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Mummi(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    NEW_REPO = True

    # -------------------------------------------------------------------
    if not NEW_REPO:
        homepage = "https://code.ornl.gov/v33/pilot2-splash-app"
        git      = "git@code.ornl.gov:v33/pilot2-splash-app.git"

        version('0.3b.0', tag='v0.3b.0') #commit='527f44e4a543f0e44daeab5d1375ce8c610eb9a0')
        version('0.2.0', tag='v0.2.0') #commit='372e85318181530731f191b5a48b747f60bfadd2')
        version('develop', branch='develop')
        version('python3', branch='python3')
        version('python3_merged', commit='33ca89df')

        #version('port', branch='port/splash', git='igit@code.ornl.gov:bhatiah/mummi.git')
        #build_directory = 'mummi'
        #version('1.0.1', tag='v1.0.1')
        #version('2014-10-08', commit='9d38cd4e2c94c3cea97d0e2924814acc')
        #version('1.0', 'f43fb8126c138db96b489655914ed2bd5a469412')

    else:
        homepage = "https://code.ornl.gov/bhatiah/mummi"
        git      = "git@code.ornl.gov:bhatiah/mummi.git"

        version('develop', branch='develop')

        variant('cudaml', default=False, description='Build ML framework with Cuda')


    '''
    ## To install, pass mpi, cuda, etc. explicitly

    lassen:
        spack install mummi@develop +cudaml ^cudnn@7.6.5.32-10.2-ppc64le ^cuda@10.1.243 ^spectrum-mpi@2019.06.24 %gcc@7.3.1
        spack install mummi@develop +cudaml ^cudnn@7.6.5.32-10.2-ppc64le ^cuda@10.2.89  ^spectrum-mpi@2019.06.24 %gcc@7.3.1
        spack install mummi@develop                                      ^cuda@10.1.243 ^spectrum-mpi@2019.06.24 %gcc@7.3.1
        spack install mummi@develop                                      ^cuda@10.2.89  ^spectrum-mpi@2019.06.24 %gcc@7.3.1
    '''
    # -------------------------------------------------------------------
    extends('python@3.7:') #.7.6')

    # build dependencies
    depends_on('cmake',  type='build')
    depends_on('swig',  type='build')

    # generic
    depends_on('py-numpy') #@1.16.4')
    depends_on('py-scipy') #@1.3.0')
    
    # ml
    depends_on('py-h5py +mpi')
    depends_on('faiss@1.6.3 +python+tests+cuda')

    
    # these settings are for powerpc (actually, only cudann only for lassen)
    #depends_on('cudnn@7.6.5.32-10.2-ppc64le', when='+cudaml')
    #depends_on('cudnn@7.5.1-10.1-ppc64le', when='+cudaml')
    #depends_on('py-theano@1.0.4 +cuda ^cudnn@7.5.1-10.1-ppc64le', when='+cudaml')

    depends_on('py-theano +cuda', when='+cudaml')
    depends_on('py-keras@2.2.4')

    # analysis
    depends_on('talass@process-statistics')
    depends_on('py-mdanalysis-mummi@mda0.19.2_ddcmd_lessmem')
    depends_on('py-scikit-learn')
    depends_on('py-matplotlib') #@3.0.2')

    depends_on('dssp@3.1.4')

    # macro
    depends_on('gridsim2d')

    # micro
    depends_on('ddcmdconverter@1.0.4')

    # gromacs
    depends_on('fftw@3.3.8 precision=double,float')
    depends_on('gromacs@2019.6 ~mpi~cuda~double~double_precision~rdtscp')

    # databroker
    depends_on('databroker@0.6.1 +python build_type=Debug')	    	#TODO: change to release when dbr is fixed

    # flux
    depends_on('flux-sched@0.8.0 +cuda')
