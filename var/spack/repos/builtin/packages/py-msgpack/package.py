# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMsgpack(PythonPackage):
    """MessagePack (de)serializer."""

    homepage = "https://msgpack.org/"
    url      = "https://pypi.io/packages/source/m/msgpack/msgpack-0.6.2.tar.gz"

    version('0.6.2', sha256='ea3c2f859346fcd55fc46e96885301d9c2f7a36d453f5d8f2967840efa1e1830')

    version('1.0.0',    sha256='420458874288b4ac0956f38c90b7d1043fcfd99deacd99563f166463ba0c514c')
    #version('0.6.2',    sha256='71d5cfc97b91a04c85b4193cbb8b50b29b66393626cb00c52b30275981ddb7f8')
    version('0.6.1',    sha256='734e1abc6f14671f28acd5266de336ae6d8de522fe1c8d0b7146365ad1fe6b0f')
    version('0.6.0',    sha256='4478a5f68142414084cd43af8f21cef9619ad08bb3c242ea505330dade6ca9ea')
    depends_on('py-setuptools', type='build')
