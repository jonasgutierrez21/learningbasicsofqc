#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import *
import matplotlib.pyplot as plt
import numpy as np


# In[7]:


#define the oracle circuit,oracle operator
oracle = QuantumCircuit(2,name='oracle')
oracle.cz(0,1) # convenient gate, flips sign of winning gate with controlled z gate  
oracle.to_gate()
oracle.draw()


# In[4]:


backend=Aer.get_backend('statevector_simulator')# check if simulator(oracle) is correct  
grover_circ = QuantumCircuit(2,2) #define the grover circuit
grover_circ.h([0,1]) # add hadamer gates, prepares for superposition state s
grover_circ.append(oracle,[0,1]) #add oracle, querry all states at the same time
grover_circ.draw()


# In[5]:


job=execute(grover_circ,backend)
result=job.result()


# In[6]:


sv=result.get_statevector()
np.around(sv,2)


# In[8]:


# reflection operator 
reflection=QuantumCircuit(2,name='reflection')
reflection.h([0,1]) # add hadamer on qubits, original 00 state
reflection.z([0,1]) # apply z on all qubits
reflection.cz(0,1) #apply a controlled z
reflection.h([0,1]) #transform to hadamer 
reflection.to_gate() #turn into a gate 


# In[9]:


reflection.draw()


# In[10]:


backend = Aer.get_backend('qasm_simulator')
grover_circ = QuantumCircuit(2,2) #2 qubits, 2 classical registers
grover_circ.h([0,1]) 
grover_circ.append(oracle,[0,1]) # add oracle 
grover_circ.append(reflection,[0,1])
grover_circ.measure([0,1],[0,1])


# In[11]:


grover_circ.draw()


# In[15]:


job=execute(grover_circ,backend,shots=1) # why when you put shot=1 you get 1024 ?
result=job.result()
result.get_counts()


# In[1]:


balanced_oracle=QuantumCircuit(n+1)

#we apply the x gates
for qubit in range(len(bstr)):
    if b_str=[qubit] =='1'
    balanced_oracle.x(qubit)
balanced.oracle.draw()


# In[ ]:





# In[ ]:




