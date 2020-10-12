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

    depends_on('mpi')
    depends_on('fftw')

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install('gridsim2dras', prefix.bin)

        with working_dir('c3-test'):
            mfiles = ['pmfcode.m', 'make_pmf.m', 'interpolate.m', 'pmfsmooth2.m']
            for m in mfiles:
                install(m, prefix.bin)

