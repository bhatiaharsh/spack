# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import stat
from spack import *


class Callflow(PythonPackage):
    """CallFlow is an interactive visual analysis tool that provides a
       high-level overview of CCTs together with semantic refinement
       operations to progressively explore the CCTs."""

    homepage = "https://github.com/LLNL/CallFlow"
    url      = "https://github.com/LLNL/CallFlow/archive/v1.1.0.tar.gz"
    git      = 'https://github.com/LLNL/CallFlow.git'

    maintainers = ["bhatiaharsh", "jarusified"]

    version('1.1.0', sha256='f8b875eb62fbac04b117e3c23fccff99d768158226a9b7fa222a2b2a6acafa44')
    version('1.1.1', tag='v1.1.1')

    depends_on('python@3.6:',       type=('build', 'run'))
    depends_on('py-setuptools',     type=('build', 'run'))

    depends_on('py-ipython',        type=('build', 'run'))
    depends_on('py-numpy',          type=('build', 'run'))
    depends_on('py-scipy',          type=('build', 'run'))
    depends_on('py-pandas',         type=('build', 'run'))
    depends_on('py-hatchet',        type=('build', 'run'))
    depends_on('py-statsmodels',    type=('build', 'run'))
    depends_on('py-scikit-learn',   type=('build', 'run'))

    depends_on('py-colorlog',       type=('build', 'run'))
    depends_on('py-jsonschema',     type=('build', 'run'))

    depends_on('py-matplotlib',     type=('build', 'run'))
    depends_on('py-networkx',       type=('build', 'run'))

    depends_on('py-flask-socketio', type=('build', 'run'))
    depends_on('node-js@13.8: ~without-npm', type=('build', 'run'))

    # Compile the npm modules included in the project
    @run_after('build')
    def build_client(self):

        with working_dir('app'):
            npm = which('npm')
            npm('install')
            npm('run', 'build')

    @run_after('install')
    def install_client(self):

        src = os.path.join(os.getcwd(), 'app')
        dst = os.path.join(self.spec.prefix, 'app')

        os.makedirs(dst, exist_ok=True)
        install(os.path.join(src, 'app.py'), dst)
        copy_tree(os.path.join(src, 'dist'), os.path.join(dst, 'dist'))

        # create the executable
        fname = os.path.join(self.spec.prefix.bin, 'callflow_app')
        with open(fname, 'w') as f:
            f.write('#!/bin/sh\n')
            f.write('cd {0}\n'.format(dst))
            f.write('flask run\n')

        st = os.stat(fname)
        os.chmod(fname, st.st_mode | stat.S_IEXEC)
