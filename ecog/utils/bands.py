"""
Frequency band information for different types of data processing.
"""
import numpy as np

class DataFormat(object):
    def write_preprocessed(self):
        raise NotImplementedError
    def read_preprocessed(self):
        raise NotImplementedError

# Chang lab frequencies
fq_min = 4.0749286538265
fq_max = 200.
scale = 7.
cfs = 2 ** (np.arange(np.log2(fq_min) * scale, np.log2(fq_max) * scale) / scale)
cfs = np.array(cfs)
sds = 10 ** ( np.log10(.39) + .5 * (np.log10(cfs)))
sds = np.array(sds)
chang_lab = {'fq_min': fq_min,
             'fq_max': fq_max,
             'scale': scale,
             'cfs': cfs,
             'sds': sds,
             'block_path': '{}_Hilb.h5'}

# Standard neuro bands
bands = ['theta', 'alpha', 'beta', 'high beta', 'gamma', 'high gamma']
min_freqs = [4., 9., 15., 21., 30., 75.]
max_freqs = [8., 14., 20., 29., 59., 150.]
HG_freq = 200.
neuro = {'bands': bands,
         'min_freqs': min_freqs,
         'max_freqs': max_freqs,
         'HG_freq': HG_freq,
         'block_path': '{}_neuro_Hilb.h5'}
