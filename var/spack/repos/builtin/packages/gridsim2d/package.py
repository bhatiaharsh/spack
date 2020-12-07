# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

import os

class Gridsim2d(MakefilePackage):

    git        = "ssh://git@cz-bitbucket.llnl.gov:7999/~tomaso/gridcorr2d.git"
    homepage   = "https://lc.llnl.gov/bitbucket/users/tomaso/repos/gridcorr2d/browse"

    version('master', branch='master')
    version('campaign-3', branch='Campaign-3')
    version('v2020-09-16', tag='v2020-09-16')
    version('v2020-10-01', tag='v2020-10-01')
    version('v2020-10-09', tag='v2020-10-09')
    version('v2020-10-09.2', tag='v2020-10-09.2')
    version('v2020-10-16-summit', tag='v2020-10-16-summit')
    version('v2020-10-23-scaling', tag='v2020-10-23-scaling')   ## Added by tomaso, 2020-10-23
    version('v2020-11-13', tag='v2020-11-13')                   ## Added by tomaso, 2020-11-13
    version('v2020-12-04', tag='v2020-12-04')
    version('v2020-12-21-c3-final', tag='v2020-12-21-c3-final') ## Added by tomaso, 2020-12-21

    depends_on('mpi')
    depends_on('fftw')

    
    def build(self, spec, prefix):
        make('clean')
        make()

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install('gridsim2dras', prefix.bin)

        '''
        with working_dir('c3-final'):
            ## mfiles desginate files needed for running and for starting a simulation from scratch
            mfiles = [ 'run-1um.cfg', \ ## Main input file
                       'make_pmf.m','pmfcode.m','interpolate.m','pmfsmooth2.m', \ ## m-files for feedback
                       'cofk_ij_hack-g2.txt','cofr_ij_hack_smooth-g2.dat', \ ## Correlation functions
                       'atoms.init','bonds.init', \ ## Initial conditions for proteins
                       'pmf_mRAFb-g2.txt','pmf_zero.txt'    , \ ## Remaining files are potentials
                       'pmf_RASa-g2.txt' ,'pmf_mRASa-g2.txt', \
                       'pmf_RASb-g2.txt' ,'pmf_mRASb-g2.txt', \
                       'pmf_RASc-g2.txt' ,'pmf_zRAFa-g2.txt', \
                       'pmf_mRAFa-g2.txt','pmf_zRASa-g2.txt', \
                       'rep12_pot.dat' \ ## Protein-protein repulsive potential
            ]


            mfiles = [] # Set this if no files need copying, e.g. continuing existin simulation
            for m in mfiles:
                install(m, prefix.bin)
        '''
