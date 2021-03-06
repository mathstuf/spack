##############################################################################
# Copyright (c) 2014, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Written by Matthew LeGendre, legendre1@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://scalability-llnl.github.io/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License (as published by
# the Free Software Foundation) version 2.1 dated February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *

class Spindle(Package):
    """Spindle improves the library-loading performance of dynamically
       linked HPC applications.  Without Spindle large MPI jobs can
       overload on a shared file system when loading dynamically
       linked libraries, causing site-wide performance problems.
    """
    homepage = "https://computation.llnl.gov/project/spindle/"
    url      = "https://github.com/hpc/Spindle/archive/v0.8.1.tar.gz"
    list_url = "https://github.com/hpc/Spindle/releases"

    version('0.8.1', 'f11793a6b9d8df2cd231fccb2857d912')

    depends_on("launchmon")

    def install(self, spec, prefix):
        configure("--prefix=" + prefix)
        make()
        make("install")
