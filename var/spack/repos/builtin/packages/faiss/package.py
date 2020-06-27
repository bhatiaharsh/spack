# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Faiss(AutotoolsPackage):
    """Faiss is a library for efficient similarity search and clustering of
       dense vectors.

      Faiss contains algorithms that search in sets of vectors of any size, up
      to ones that possibly do not fit in RAM. It also contains supporting code
      for evaluation and parameter tuning. Faiss is written in C++ with complete
      wrappers for Python/numpy. Some of the most useful algorithms are
      implemented on the GPU. It is developed by Facebook AI Research.
    """

    homepage = "https://github.com/facebookresearch/faiss"
    url      = "https://github.com/facebookresearch/faiss/archive/v1.6.3.tar.gz"

    # putting the creator's name for now
    #  but hopefully, FAISS developers will take over
    maintainers = ['bhatiaharsh']

    version('1.6.3', sha256='e1a41c159f0b896975fbb133e0240a233af5c9286c09a28fde6aefff5336e542')
    version('1.6.2', sha256='8be8fcb943e94a93fb0796cad02a991432c0d912d8ae946f4beb5a8a9c5d4932')
    version('1.6.1', sha256='827437c9a684fcb88ee21a8fd8f0ecd94f36e2db213f74357d0465c5a7e72ac6')
    version('1.6.0', sha256='71a47cbb00aa0ae09b77a70d3fa1617bf7861cc7d41936458b88c7a161b03660')
    version('1.5.3', sha256='b24d347b0285d01c2ed663ccc7596cd0ea95071f3dd5ebb573ccfc28f15f043b')


    variant('cuda',   default=False, description='Build with CUDA')
    variant('python', default=False, description='Build Python bindings')


    depends_on('blas')
    depends_on('cuda',     when='+cuda')

    depends_on('swig',     when='+python', type='build')
    depends_on('python',   when='+python', type=('build', 'run'))
    depends_on('py-numpy', when='+python', type=('build', 'run'))
    #depends_on('py-setuptools', when='+python') #, type='build')


    def configure_args(self):
        args = []

        if '+cuda' in self.spec:
            args.append('--with-cuda={}'.format(self.spec['cuda'].prefix))
        else:
            args.append('--without-cuda')

        return args


    def build(self, spec, prefix):

        # ----------------------------------------------------------------------
        # for v1.5.3, the makefile contains x86-specific flags
        # so, we need to remove them for powerpc
        # for v1.6.0, this seems to have been fixed

        # TODO: didn't check < 1.5.3 (but, do we care about the older versions)
        # TODO: should this be removed for other architectures as well?
        #       i.e., change the condition to target != 'x86' ?

        if self.version <= Version('1.5.3') and spec.architecture.target == 'power9le':

            makefile = FileFilter('makefile.inc')
            makefile.filter( 'CPUFLAGS     = -mavx2 -mf16c',
                            '#CPUFLAGS     = -mavx2 -mf16c')

        # ----------------------------------------------------------------------
        # for v1.6.3, GPU build has a bug (two files need to be deleted)
        # https://github.com/facebookresearch/faiss/issues/1159

        if self.version == Version('1.6.3') and '+cuda' in self.spec:
            import os
            os.remove('gpu/impl/PQCodeDistances.cu')
            os.remove('gpu/impl/PQScanMultiPassNoPrecomputed.cu')

        # ----------------------------------------------------------------------
        make()
        if '+python' in self.spec:
            make('-C', 'python')


    def install(self, spec, prefix):

        make('install')
        if '+python' in self.spec:
            make('-C', 'python', 'install')

            # ------------------------------------------------------------------
            # temp fix
            pversion = '3.7'
            fversion = '1.5.3'

            if self.version == Version('1.5.3'):
                fversion = '1.5.3'
            elif self.version == Version('1.6.3'):
                fversion = '1.6.3'

            lpath = 'lib/python{}/site-packages'.format(pversion)
            fname = 'faiss-{}-py{}.egg'.format(fversion, pversion)
            bname = '{}.zipped'.format(fname)

            import os
            os.chdir(os.path.join(self.spec['python'].prefix, lpath))
            os.system('mv {} {}'.format(fname, bname))
            os.system('unzip {} -d {}'.format(bname, fname))
