
#! /usr/bin/env python
#
#   This node will record background noise and continue recording while detecting
#   amplitude anomalies based on a statistical model of previous trials. If an 
#   amplitude anomaly is detected, it will publish a ROS message to the 'emergency' topic.
#   Otherwise, it will take a DFT spectrogram of the audio data, find the average
#   power for each frequency and publish a 1D numpy array ([Average Power, frequency]) 
#   of this data to the 'audio_analysis' topic. 
#
#
from __future__ import division
import numpy as np
import rospy
import pylab
from collections import deque
from std_msgs.msg import String
from matplotlib import pyplot as plt
from matplotlib import mlab
from scipy import stats
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
import math

import pyaudio
import wave

chunk=1024      		#frame size
form=pyaudio.paFloat32
channel=1      			#number of channels
rate1=44100     		#sampling rate


secs=5          		#number of seconds to establish background noise baseline
stop=True 
mu=0			        #mean as calculated from previous trials
				#variance
sigma=140
				#standard deviation	
stddevs=1	          	#number of standard deviations above mean to allow as a threshhold
print(str(sigma*stddevs))
rospy.init_node('audio_talker', anonymous=False)
pub1=rospy.Publisher('emergency', String)
pub2=rospy.Publisher('audio_analysis', numpy_msg(Floats))


p=pyaudio.PyAudio()

stream=p.open(format=form, channels=channel, rate=rate1, input=True, frames_per_buffer=chunk)


#print ("*recording background noise")

#frames_back=deque([])
#amp_back=deque([])
#for i in range(0, int(rate1/chunk*secs)):     #Record a couple (5) seconds of background noise
#    data=stream.read(chunk)
#    decoded=np.fromstring(data, 'Float32')
#    decoded2=np.fromstring(data, 'Int16')
#    frames_back.append(decoded)
#    amp_back=deque([])

#print("*done recording background noise")


#Model of Background Noise

#mu_back=np.mean(amp_back)




frames=deque([], 3000)
amp_frames=deque([], 3000)
try:
    while stop:
        data=stream.read(chunk)
        decoded=np.fromstring(data, 'Float32')
        decoded2=np.fromstring(data, 'Int16')
        amp_frames.append(decoded2)
        frames.append(decoded)
        l=len(frames)
        if l*chunk>=3000:
            index=range(0, l-2)
            frames_arr=np.array(frames.popleft())   
            amp_frames_arr=np.array(amp_frames.popleft())
            for i in index:
                e=frames.popleft()
                frames_arr=np.concatenate((frames_arr, e), axis=0)
            for i in index:
                s=amp_frames.popleft()
                amp_frames_arr=np.concatenate((amp_frames_arr, s), axis=0)
            frames_arr.reshape(-1)    


            #DFT Spectrogram
            Pxx, freqs, t=mlab.specgram(frames_arr, NFFT=256, Fs=rate1)
            
            #Find average power       
            Pxx_ave=np.mean(Pxx, axis=1)
            ind=freqs<=3000
            #Look at frequencies that are in expected range
            c=Pxx_ave[ind]
            d=freqs[ind]
            #Amalgamate into one 1D array, so it can be sent as a ROS message
            data=np.concatenate((c, d)) 
            #Make histogram of frequency vs power spectral density
            #H, xedges, yedges=np.histogram2d(Pxx_ave, freqs, bins=16, normed=True)
                   
            #Find Z score with which to check amplitude
            z=((amp_frames_arr-mu)/sigma)
            print(z)
            a=abs(z)>=stddevs*sigma
            print(a.any())           
            #Publish ROS messages
    	    
            def audio_analyzer(z, data): 
                global pub1
                global pub2
                
                r=rospy.Rate(10) #in hz
                #Check if amplitude is above threshold
                a=abs(z)>=stddevs*sigma
                b=a.any()
                
                if b:
                    #Continue checking amplitude and publish stop message if anomaly occurs
                    pub1.publish('STOP')
                    pub1.publish('STOP')
                    pub1.publish('STOP')
                    pub1.publish('STOP')
                    pub1.publish('STOP')
                    pub1.publish('STOP')
                    pub1.publish('STOP')
                    pub1.publish('STOP')
                    pub1.publish('STOP')
                    pub1.publish('STOP')
                    rospy.sleep(0.1)
                    print('help')
                    rospy.sleep(0.1)                
                else:
                    
                    #If no anomaly continue publishing power and frequency data
                    pub2.publish(data.astype(float))
                
                while not rospy.is_shutdown():
                    a=abs(z)>=stddevs*sigma
                    b=a.any()
                    
                    if b:
                        #Continue checking amplitude and publish stop message if anomaly occurs
                        str1='STOP'
                        pub1.publish(str1)
                        pub1.publish('STOP')
                        pub1.publish('STOP')
                        pub1.publish('STOP')
                        pub1.publish('STOP')
                        pub1.publish('STOP')
                        pub1.publish('STOP')
                        pub1.publish('STOP')
                        pub1.publish('STOP')
                        pub1.publish('STOP')
                        pub1.publish('STOP')
                        rospy.sleep(0.1)
                        print('work')
                        rospy.sleep(0.1)  
                    else:
                        
                        #If no anomaly continue publishing power and frequency data
                        pub2.publish(data.astype(float))
                    
              

            if __name__=='__main__':
                audio_analyzer(z, data)
                
                 

except KeyboardInterrupt: 
    stream.stop_stream()
    stream.close()
    p.terminate()
    rospy.shutdown()
