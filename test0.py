import numpy as np
#import benchmark_class
import ARS_benchmark
import matplotlib.pyplot as plt
N = 20
T = 0.5+1/30

noise = 0.00 # remember noise is optional

#two_level = benchmark_class.TwoLevel(N, T, noise)

#alist = 2*(np.random.rand(N)-0.5)

# this is how you evaluate it, with step-per-step updates

#for step in range(0, N):
    
#    _, r = two_level.update(alist[step])
#    print("r:", r)

# this is how you use roll_out

#G = two_level.roll_out(alist)
#print("G:", G)
Tlist = []
# Note, if the noise is different from zero, you get a different result each time. 
pulse = np.random.rand(N)#np.array([ 1.        ,  0.75186758,  0.18700439, -0.90246136, -1.        ,
       #-1.        , -1.        , -1.        ,  0.37882948,  0.21337853,
       # 0.21337512,  0.37883106, -1.        , -1.        , -1.        ,
       #-1.        , -0.90246192,  0.18700451,  0.75186756,  1.        ]) #np.random.rand
alpha = 0.1
v = 0.4
maxite = 80
maxepochs = 10
f_story = np.zeros((maxepochs,maxite))
times = np.zeros((maxepochs,maxite))
M_list = np.zeros((N,maxite))
ARS = ARS_benchmark.ARSTrainer()

for i in range(maxite):
    T += 0.05
    M_list[:,i],f_story[:,i],times[:,i] = ARS.train(pulse,N,T,alpha,v,L=5, Noise = noise,maxepochs=maxepochs)
    pulse = np.random.rand(N)
    Tlist.append(T)


time_average_A = np.average(times,axis = 0)
f_story_avg_A = np.average(f_story,axis = 0)
f_story_std_A = np.std(f_story,axis = 0)
f_story_max_A = np.max(f_story,axis = 0)
fig = plt.figure()
ax1 = fig.add_subplot(111)
#ax1.plot(time_average_A,f_story_avg_A,'*',label = "Fidelity max Waveless")
#ax1.plot(times,f_story,'*',label = "Fidelity max Waveless")
ax1.plot(Tlist,1-f_story_max_A,'*',label = "Fidelity max Waveless")
ax1.set_xlabel('T ')
ax1.set_yscale('log')
ax1.set_ylabel('Fidelity')
ax1.set_title('QSL ARS graph-Max')
#ax1.legend()
ax1.set_title('QSL ARS graph - with noise')
fig.show()
'''
T = 3.2+1/30
for i in range(maxite):
    M_list[:,i],f_story[:,i],times[:,i] = ARS.train(pulse,N,T,alpha,v,L=5, Noise = noise,maxepochs=maxepochs)

time_average_A = np.average(times,axis = 1)
f_story_avg_A = np.average(f_story,axis = 1)
f_story_std_A = np.std(f_story,axis = 1)
f_story_max_A = np.max(f_story,axis = 1)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(time_average_A,f_story_avg_A,'*',label = "Fidelity mean Waveless")
ax1.plot(time_average_A,f_story_max_A,'+',label = "Fidelity max Waveless")
ax1.plot(time_average_A,f_story_avg_A+f_story_std_A,'g--',label = "Fidelity std Waveless")
ax1.plot(time_average_A,f_story_avg_A-f_story_std_A,'r--',label = "Fidelity std Waveless")
#ax1.plot(times,f_story,'*',label = "Fidelity max Waveless")
#ax1.plot(Tlist,f_story[-1,:],'*',label = "Fidelity max Waveless")
ax1.set_xlabel('Wall time ')
ax1.set_ylabel('Fidelity')
ax1.set_title('QSL ARS graph-Max')
ax1.legend()
ax1.set_title('QSL ARS graph')
fig.show()
'''