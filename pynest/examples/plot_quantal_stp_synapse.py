# -*- coding: utf-8 -*-
#
# plot_quantal_stp_synapse.py
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

# This script compares the two variants of the Tsodyks/Markram synapse in NEST.

import nest
import nest.voltage_trace
import numpy
import pylab

nest.ResetKernel()
n_syn=12.0 # number of synapses in a connection
n_trials=30# number of measurement trials

# parameter set for facilitation
fac_params={"U":0.03,"u": 0.03, "tau_fac":500.,"tau_rec":200.,"weight":1.}
dep_params={"U":0.5, "u": 0.5,  "tau_fac":15.,"tau_rec":670.,"weight":1.}
lin_params={"U":0.3, "u": 0.3,  "tau_fac":330.,"tau_rec":330.,"weight":1.}

# Here we assign the parameter set to the synapse models 
t1_params=fac_params       # for tsodyks2_synapse
t2_params=t1_params.copy() # for furhmann_synapse

t2_params['n']=n_syn
t2_params['weight']=1./n_syn

nest.SetDefaults("tsodyks2_synapse",t1_params)
nest.SetDefaults("quantal_stp_synapse",t2_params)
nest.SetDefaults("iaf_psc_exp",{"tau_syn_ex": 3., 'tau_m':70.})

source=nest.Create('spike_generator')
nest.SetStatus(source,{'spike_times':[30.,60.,90.,120.,150.,180.,210.,240., 270., 300., 330., 360., 390.,900.]})

neuron = nest.Create("iaf_psc_exp",2)

nest.Connect(source,[neuron[0]],syn_spec="tsodyks2_synapse")
nest.Connect(source,[neuron[1]],syn_spec="quantal_stp_synapse")

voltmeter = nest.Create("voltmeter",2)
nest.SetStatus(voltmeter, {"withgid": False, "withtime": True})
t_plot=1000.
t_tot=1500.

# the following is a dry run trial so that the synapse dynamics is
# idential in all subsequent trials.

nest.Simulate(t_tot)


# Now we connect the voltmeters
nest.Connect([voltmeter[0]], [neuron[0]])
nest.Connect([voltmeter[1]], [neuron[1]])

for t in range(n_trials):
    t_net=nest.GetKernelStatus('time')
    nest.SetStatus(source,{'origin':t_net})
    nest.Simulate(t_tot)

nest.Simulate(.1) # flush the last voltmeter events from the queue

vm= numpy.array(nest.GetStatus([voltmeter[1]],'events')[0]['V_m'])
vm_reference=numpy.array(nest.GetStatus([voltmeter[0]],'events')[0]['V_m'])

vm.shape=(n_trials,t_tot)
vm_reference.shape=(n_trials,t_tot)

vm_mean=numpy.array([numpy.mean(vm[:,i]) for i in range(int(t_tot))]) 
vm_ref_mean=numpy.array([ numpy.mean(vm_reference[:,i]) for i in range(int(t_tot))]) 

for t in range(n_trials):
    pylab.plot(vm[t][:t_plot],color='gray',lw=0.5)
#for t in range(n_trials):
#    pylab.plot(vm_reference[t,t_rest:t_plot],lw=0.5)
#    
pylab.plot(vm_mean[:t_plot], color='black',lw=2.)
pylab.plot(vm_reference[0][:t_plot], color='red',lw=2.)

pylab.show()
