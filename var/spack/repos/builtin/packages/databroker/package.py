# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from os import system, chdir 

class Databroker(CMakePackage):
    """The Data Broker (DBR) is a distributed, in-memory container of key-value 
    stores enabling applications in a workflow to exchange data through one or 
    more shared namespaces. Thanks to a small set of primitives, applications 
    in a workflow deployed in a (possibly) shared nothing distributed cluster, 
    can easily share and exchange data and messages with applications."""

    homepage = "https://github.com/IBM/data-broker"
    #git      = "git@github.com:IBM/data-broker.git"

    version('0.6.1', url='https://github.com/IBM/data-broker/archive/0.6.1.tar.gz', 
                     sha256='2c7d6c6a269d4ae97aad4d770533e742f367da84758130c283733f25df83e535')
    version('0.6.0', url='https://github.com/IBM/data-broker/archive/0.6.0.tar.gz',
                     sha256='5856209d965c923548ebb69119344f1fc596d4c0631121b230448cc91bac4290')


    #version('0.6.1', version='0.6.1')
    #version('master', branch='master')
    variant('python', default=False, description='Build Python bindings')

    depends_on('cmake@2.8:',      type='build')
    depends_on('redis@5.0.2:',    type='run')
    #depends_on('redis@4.0.8:',    type=('build', 'run'))
    #depends_on('ruby@2.2.9:',    type=('build', 'run'))
    depends_on('libevent@2.1.8', type=('build', 'run'))

    extends('python@3.7:',        when='+python')
    #depends_on('py-pip',          when='+python', type='build')
    depends_on('py-setuptools',   when='+python', type=('build', 'run'))
    #depends_on('libffi@3.2.1',    when='+python', type=('build', 'run'))
    #depends_on('py-cffi@1.11.5',  when='+python', type=('build', 'run'))
    #depends_on('py-enum34@1.1.6', when='+python', type=('build', 'run'))

    #parallel = False
    def cmake_args(self):
        args = []
        args.append('-DDEFAULT_BE=redis')
        #args.append('-DCMAKE_BUILD_TYPE=Release')   # v0.6.1 fails for RelWithDebInfo (spack's default)
        #args.append('-DCMAKE_COLOR_MAKEFILE=ON')
        #args.append('-DCMAKE_VERBOSE_MAKEFILE=ON')

        if '+python' in self.spec:
            args.append('-DPYDBR=1')
        return args

    #def install(self, spec, prefix):
    #
    #    '''
    #    print ' which ruby: ', 
    #    system('which ruby')
    #    print 'which gem : ',
    #    system('which gem')
    #    system('`which gem` env')
    #    system('`which gem` install -V redis')
    #    
    #    exit()
    #    '''
    #    #system('pip install rdbtools python-lzf')

    #    #chdir(self.build_directory)
    #    #make('install')
