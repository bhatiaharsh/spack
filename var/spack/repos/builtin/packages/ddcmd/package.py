# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from os import chdir, listdir, getcwd, rename
from shutil import copy
from glob import glob


class Ddcmd(MakefilePackage):
    """DDCMD."""

    homepage = "https://lc.llnl.gov/bitbucket/projects/DDCMDY"
    git      = "ssh://git@cz-bitbucket.llnl.gov:7999/ddcmdy/ddcmd.git"

    #version('temp', commit='4c9c4cfc740', submodules=True)
    version('develop', branch='develop', submodules=True)
    version('hycop', branch='hycop-tomaso', submodules=True)
    version('gbell', tag='Gorden-Bell', submodules=True)
    version('jun8', tag='jun-8', submodules=True)

    depends_on('mpi')

    depends_on('ddcmdconverter@master', when='@develop')
    depends_on('ddcmdconverter@1.0.1', when='@jun8')
    depends_on('ddcmdconverter@1.0.0', when='@gbell')

    build_directory = 'src'
    
    def install(self, spec, prefix):

        print 'doing custom install'
        print '\t prefix =', prefix
        print '\t cwd =', getcwd()
        print '\t ls =', listdir('.')

        mkdir(prefix.bin)

        # the install target was added on Sep 07
        # so, gbell and jun8 versions do not have that
        if spec.satisfies('@gbell') or spec.satisfies('@jun8'):
            print '-> doing explicit copy for older versions without install target'
           
            chdir('bin')
            files = listdir('.')
            print 'found', len(files), 'file(s) in', getcwd()
            print files
            
            for f in files:
                print 'copying', f
                copy(f, prefix.bin)

        else:
            # go back to the build directory
            chdir('src')
            make('install', 'INSTALL_DIR={}'.format(prefix.bin))

        # the above will create the executable named as ddcMD-[arch]
        # for simplicity, we will move to 'ddcmd' or 'ddcmd-hycop'
        target_name = 'ddcmd-hycop' if spec.satisfies('@hycop') else 'ddcmd'

        chdir(prefix.bin)
        files = listdir('.')
        if len(files) == 1:
            print '-> renaming {} to {}'.format(files[0], target_name)
            rename(files[0], target_name)

        else:
            print '-> found', len(files), 'file(s) in', getcwd()
            print '  ', files
            print '-> cannot rename files. exiting'
            exit(1)
