import os
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import read_wave

wave = read_wave('C:/Users/Administrator.000/Desktop/第五次实验/123.wav')

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
wave.make_spectrogram(512).plot(high=5000)
plt.ylabel('频率(HZ)')
plt.xlabel('时间（s）')
wave.write(filename='output3-4.wav')
plt.show()
