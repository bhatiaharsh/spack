# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libmonitor(AutotoolsPackage):
    """Libmonitor is a library providing callback functions for the
    begin and end of processes and threads.  It provides a layer on
    which to build process monitoring tools and profilers."""

    homepage = "https://github.com/HPCToolkit/libmonitor"
    git      = "https://github.com/HPCToolkit/libmonitor.git"
    maintainers = ['mwkrentel']

    version('master', branch='master')
    version('2019.05.31', commit='c9767087d52e58a719aa7f149136b101e499db44')
    version('2018.07.18', commit='d28cc1d3c08c02013a68a022a57a6ac73db88166')
    version('2013.02.18', commit='4f2311e413fd90583263d6f20453bbe552ccfef3')

    # Configure for Rice HPCToolkit.
    variant('hpctoolkit', default=False,
            description='Configure for HPCToolkit')

    # Configure for Krell and OpenSpeedshop.
    variant('krellpatch', default=False,
            description="Build with openspeedshop based patch.")

    patch('libmonitorkrell-0000.patch', when='@2013.02.18+krellpatch')
    patch('libmonitorkrell-0001.patch', when='@2013.02.18+krellpatch')
    patch('libmonitorkrell-0002.patch', when='@2013.02.18+krellpatch')

    signals = 'SIGBUS, SIGSEGV, SIGPROF, 36, 37, 38'

    # Set default cflags (-g -O2) and move to the configure line.
    def flag_handler(self, name, flags):
        if name != 'cflags':
            return (flags, None, None)

        if '-g' not in flags:
            flags.append('-g')
        for flag in flags:
            if flag.startswith('-O'):
                break
        else:
            flags.append('-O2')

        return (None, None, flags)

    def configure_args(self):
        args = []

        if '+hpctoolkit' in self.spec:
            args.append('--enable-client-signals=%s' % self.signals)

        return args
