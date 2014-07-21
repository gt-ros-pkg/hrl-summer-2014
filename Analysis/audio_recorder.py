from __future__ import division
import numpy as np
import rospy
from collections import deque
from std_msgs.msg import String
import math

import pyaudio
import wave


class audio_core():
    def __init__(self):
        self.num=input("Enter Trial Number: ")
        self.stop=True
        self.fname="trial%s"%self.num
        self.chunk=1024 #frame size
        self.form=pyaudio.paFloat32
        self.channel=1 #number of channels
        self.rate1=44100 #sampling rate
        rospy.init_node('state_listener', anonymous=False)
        self.p=pyaudio.PyAudio() #open stream to record data
        self.stream=self.p.open(format=self.form, channels=self.channel, rate=self.rate1, input=True, frames_per_buffer=self.chunk)
        rospy.Subscriber('Main_Control', String, self.listen)     #listen for changes between subtasks
        self.part='0'
        self.part0=[]
        self.part1=[]
        self.part2=[]
        self.part3=[]
        self.part4=[]
        self.part5=[]
        self.part6=[]
        self.part7=[]
        self.part8=[]
        self.part9=[]
        self.part10=[]
        self.part11=[]

        self.record()    #start recording
 
    def listen(self, msg):
        self.message=msg.data          #grab message from 'Master_Control" topic
        print ('made it')
        if self.message is "Part10":   #set part variable to part of the tast being performed
            self.part="10"
        elif self.message is "Part11":
            self.part="11"
        elif self.message is 'stop':   #if task is over set part to 'na'
            self.part='na'
        else:
            self.part=self.message[-1]
    
    def record(self):
        print("*recording")
            while self.stop:                       #record audio data
			    data=self.stream.read(self.chunk)
			    if self.part is'0':                #divide into parts based on sub-task being performed    
			        self.part0.append(data)
			    elif self.part is '1':
			        self.part1.append(data)
			    elif self.part is '2':
			        self.part2.append(data)
			    elif self.part is '3':
			        self.part3.append(data)
			    elif self.part is'4':
			        self.part4.append(data)
			    elif self.part is'5':
			        self.part5.append(data)
			    elif self.part is '6':
			        self.part6.append(data)
			    elif self.part is '7':
			        self.part7.append(data)
			    elif self.part is '8':
			        self.part8.append(data)
			    elif self.part is '9':
			        self.part9.append(data)
			    elif self.part is '10':
			        self.part10.append(data)
			    elif self.part is '11':
			        self.part11.append(data)
                if self.message is 'STOP'or self.part is 'na': #if end of task, stop recording
                    print("stop heard")
                    break
                    
        
        print("*stopped recording")   #stop recording at end of task
        self.makefiles()              #write data to files
        self.stream.stop_stream()     #close audio stream
        self.stream.close()
        self.p.terminate()
            

    def makefiles(self):	          #writes each part of the task to its own audio file
		print("*writing data to files")	
		output_file='trial%s_p0.wav'%self.num
		wf=wave.open(output_file, 'wb')
		wf.setnchannels(self.channel)
		wf.setsampwidth(self.p.get_sample_size(self.form))
		wf.setframerate(self.rate1)
		wf.writeframes(b''.join(self.part0))
		wf.close()

		output_file='trial%s_p1.wav'%self.num
		wf=wave.open(output_file, 'wb')
		wf.setnchannels(self.channel)
		wf.setsampwidth(self.p.get_sample_size(self.form))
		wf.setframerate(self.rate1)
		wf.writeframes(b''.join(self.part1))
		wf.close()

		output_file='trial%s_p2.wav'%self.num
		wf=wave.open(output_file, 'wb')
		wf.setnchannels(self.channel)
		wf.setsampwidth(self.p.get_sample_size(self.form))
		wf.setframerate(self.rate1)
		wf.writeframes(b''.join(self.part2))
		wf.close()

		output_file='trial%s_p3.wav'%self.num
		wf=wave.open(output_file, 'wb')
		wf.setnchannels(self.channel)
		wf.setsampwidth(self.p.get_sample_size(self.form))
		wf.setframerate(self.rate1)
		wf.writeframes(b''.join(self.part3))
		wf.close()	
		 
		output_file='trial%s_p4.wav'%self.num
		wf=wave.open(output_file, 'wb')
		wf.setnchannels(self.channel)
		wf.setsampwidth(self.p.get_sample_size(self.form))
		wf.setframerate(self.rate1)
		wf.writeframes(b''.join(self.part4))
		wf.close()        
		 
		output_file='trial%s_p5.wav'%self.num
		wf=wave.open(output_file, 'wb')
		wf.setnchannels(self.channel)
		wf.setsampwidth(self.p.get_sample_size(self.form))
		wf.setframerate(self.rate1)
		wf.writeframes(b''.join(self.part5))
		wf.close()        

		output_file='trial%s_p6.wav'%self.num
		wf=wave.open(output_file, 'wb')
		wf.setnchannels(self.channel)
		wf.setsampwidth(self.p.get_sample_size(self.form))
		wf.setframerate(self.rate1)
		wf.writeframes(b''.join(self.part6))
		wf.close()

		output_file='trial%s_p7.wav'%self.num
		wf=wave.open(output_file, 'wb')
		wf.setnchannels(self.channel)
		wf.setsampwidth(self.p.get_sample_size(self.form))
		wf.setframerate(self.rate1)
		wf.writeframes(b''.join(self.part7))
		wf.close()

		output_file='trial%s_p8.wav'%self.num
		wf=wave.open(output_file, 'wb')
		wf.setnchannels(self.channel)
		wf.setsampwidth(self.p.get_sample_size(self.form))
		wf.setframerate(self.rate1)
		wf.writeframes(b''.join(self.part8))
		wf.close()

		output_file='trial%s_p9.wav'%self.num
		wf=wave.open(output_file, 'wb')
		wf.setnchannels(self.channel)
		wf.setsampwidth(self.p.get_sample_size(self.form))
		wf.setframerate(self.rate1)
		wf.writeframes(b''.join(self.part9))
		wf.close()

		output_file='trial%s_p10.wav'%self.num
		wf=wave.open(output_file, 'wb')
		wf.setnchannels(self.channel)
		wf.setsampwidth(self.p.get_sample_size(self.form))
		wf.setframerate(self.rate1)
		wf.writeframes(b''.join(self.part10))
		wf.close()

		output_file='trial%s_p11.wav'%self.num
		wf=wave.open(output_file, 'wb')
		wf.setnchannels(self.channel)
		wf.setsampwidth(self.p.get_sample_size(self.form))
		wf.setframerate(self.rate1)
		wf.writeframes(b''.join(self.part11))
		wf.close()
		
    
def main():
    core = audio_core()
    rospy.spin()

if __name__=='__main__':
    main()
