# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import stat
import shutil
from spack import *


class Callflow(PythonPackage):
    """CallFlow is an interactive visual analysis tool that provides a
       high-level overview of CCTs together with semantic refinement
       operations to progressively explore the CCTs."""

    homepage = "https://github.com/LLNL/CallFlow"
    url      = "https://github.com/LLNL/CallFlow/archive/v1.1.0.tar.gz"

    maintainers = ["bhatiaharsh", "jarusified"]

    version('1.1.0', sha256='f8b875eb62fbac04b117e3c23fccff99d768158226a9b7fa222a2b2a6acafa44')
    version('test', git='git@github.com:jarusified/CallFlow.git', branch='fix/installation')

    depends_on('python@3.6:',       type=('build', 'run'))
    depends_on('py-setuptools',     type='build')

    depends_on('py-numpy',          type=('build', 'run'))
    depends_on('py-pandas',         type=('build', 'run'))
    depends_on('py-hatchet',        type=('build', 'run'))

    depends_on('py-pydot',          type=('build', 'run'))
    depends_on('py-pyyaml',         type=('build', 'run'))
    depends_on('py-colorlog',       type=('build', 'run'))
    depends_on('py-jsonschema',     type=('build', 'run'))

    depends_on('py-matplotlib',     type=('build', 'run'))
    depends_on('py-networkx',       type=('build', 'run'))
    depends_on('py-statsmodels',    type=('build', 'run'))
    depends_on('py-scikit-learn',   type=('build', 'run'))

    depends_on('py-flask',          type=('build', 'run'))
    depends_on('py-flask-socketio', type=('build', 'run'))
    depends_on('node-js@13.8: ~without-npm', type=('build', 'run'))

    # Compile the npm modules included in the project
    @run_after('install')
    def build_app(self):

        src = os.path.join(os.getcwd(), 'app')
        dst = os.path.join(self.spec.prefix, 'app')
        shutil.copytree(src, dst)

        with working_dir(dst):
            os.system('npm install .')

        fname = os.path.join(self.spec.prefix.bin, 'callflow_client')
        with open(fname, 'w') as f:
            f.write('#!/bin/sh\n')
            f.write('cd {}\n'.format(dst))
            f.write('npm run dev\n')

        st = os.stat(fname)
        os.chmod(fname, st.st_mode | stat.S_IEXEC)
