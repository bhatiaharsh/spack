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
#     spack install faiss
#
# You can edit this file again by typing:
#
#     spack edit faiss
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Faiss(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/facebookresearch/faiss"
    url      = "https://github.com/facebookresearch/faiss/archive/v1.5.3.tar.gz"

    version('1.5.3', '0bc12737b23def156f6a1eb782050135')

    variant('python', default=True, description='Build Python bindings')

    depends_on('blas')
    depends_on('cuda')

    depends_on('swig', when='+python', type='build')
    depends_on('python', when='+python', type=('build', 'run'))
    depends_on('py-numpy', when='+python', type=('build', 'run'))

    def build(self, spec, prefix):

        if True: #'x86' not in spec.architecture.target:
            makefile = FileFilter('makefile.inc')
            makefile.filter('CPUFLAGS     = -mavx2 -mf16c', '#CPUFLAGS     = -mavx2 -mf16c')
            #makefile.filter('CPUFLAGS     = -msse4 -mpopcnt',  '#CPUFLAGS     = -msse4 -mpopcnt')

        make()
        if '+python' in self.spec:
            make('-C', 'python')

    def install(self, spec, prefix):

        make('install')
        if '+python' in self.spec:
            make('-C', 'python', 'install') 
