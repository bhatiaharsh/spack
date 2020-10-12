# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyGreenlet(PythonPackage):
    """Lightweight in-process concurrent programming"""

    homepage = "https://github.com/python-greenlet/greenlet"
    url      = "https://github.com/python-greenlet/greenlet/archive/0.4.17.tar.gz"

    version('0.4.17', sha256='c63c8258eef589a86c266a05385b1ed105cf2a7fc48f47c89bb0c1de48d90c00')
    version('0.4.13', sha256='0fef83d43bf87a5196c91e73cb9772f945a4caaff91242766c5916d1dd1381e4')
