'''
Defines a class, Neuron472427533, of neurons from Allen Brain Institute's model 472427533

A demo is available by running:

    python -i mosinit.py
'''
class Neuron472427533:
    def __init__(self, name="Neuron472427533", x=0, y=0, z=0):
        '''Instantiate Neuron472427533.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron472427533_instance is used instead
        '''
               
        self._name = name
        # load the morphology
        from load_swc import load_swc
        load_swc('Scnn1a-Tg2-Cre_Ai14_IVSCC_-176958.05.02.01_471750463_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
 
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron472427533_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im', u'K_P', u'K_T', u'Kv3_1', u'NaTs', u'Nap', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 26.95
            sec.e_pas = -92.7820739746
        for sec in self.apic:
            sec.cm = 2.22
            sec.g_pas = 3.18482838725e-05
        for sec in self.axon:
            sec.cm = 1.0
            sec.g_pas = 0.000264805794444
        for sec in self.dend:
            sec.cm = 2.22
            sec.g_pas = 9.78263312302e-06
        for sec in self.soma:
            sec.cm = 1.0
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Im = 1.56341e-05
            sec.gbar_Ih = 3.45384e-05
            sec.gbar_NaTs = 0.71282
            sec.gbar_Nap = 0.000247043
            sec.gbar_K_P = 0.0248444
            sec.gbar_K_T = 0.00296613
            sec.gbar_SK = 0.000151241
            sec.gbar_Kv3_1 = 0.118104
            sec.gbar_Ca_HVA = 0.000197121
            sec.gbar_Ca_LVA = 0.00784187
            sec.gamma_CaDynamics = 0.00178784
            sec.decay_CaDynamics = 971.922
            sec.g_pas = 1.66466e-05
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

