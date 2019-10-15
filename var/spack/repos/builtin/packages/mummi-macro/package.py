# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class MummiMacro(MakefilePackage):
    git        = "ssh://git@cz-bitbucket.llnl.gov:7999/~tomaso/gridcorr2d.git"
    version('master', branch='master')

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install('gridsim2dras', prefix.bin)
