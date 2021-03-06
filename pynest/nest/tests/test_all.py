# -*- coding: utf-8 -*-
#
# test_all.py
#
# This file is part of NEST.
#
# Copyright (C) 2004 The NEST Initiative
#
# NEST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# NEST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NEST.  If not, see <http://www.gnu.org/licenses/>.

import unittest
import nest

from . import compatibility

from . import test_errors
from . import test_stack
from . import test_create
from . import test_status
from . import test_onetooneconnect
from . import test_convergent_divergent_connect
from . import test_connect_all_to_all
from . import test_connect_fixed_indegree
from . import test_connect_fixed_outdegree
from . import test_connect_fixed_total_number
from . import test_connect_one_to_one
from . import test_connect_pairwise_bernoulli
from . import test_findconnections
from . import test_getconnections
from . import test_dataconnect
from . import test_events
from . import test_networks
from . import test_threads
from . import test_csa
from . import test_quantal_stp_synapse


def suite():

    suite = unittest.TestSuite()

    suite.addTest(test_errors.suite())
    suite.addTest(test_stack.suite())
    suite.addTest(test_create.suite())                    
    suite.addTest(test_status.suite())
    suite.addTest(test_onetooneconnect.suite())
    suite.addTest(test_convergent_divergent_connect.suite())
    suite.addTest(test_connect_all_to_all.suite())
    suite.addTest(test_connect_fixed_indegree.suite())
    suite.addTest(test_connect_fixed_outdegree.suite())
    suite.addTest(test_connect_fixed_total_number.suite())
    suite.addTest(test_connect_one_to_one.suite())
    suite.addTest(test_connect_pairwise_bernoulli.suite())
    suite.addTest(test_findconnections.suite())    
    suite.addTest(test_getconnections.suite())
    suite.addTest(test_dataconnect.suite())
    suite.addTest(test_events.suite())
    suite.addTest(test_networks.suite())
    suite.addTest(test_threads.suite())    
    suite.addTest(test_csa.suite())    
    suite.addTest(test_quantal_stp_synapse.suite())    
    
    return suite


if __name__ == "__main__":

    debug = nest.get_debug()
    nest.set_debug(True)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())

    nest.set_debug(debug)
