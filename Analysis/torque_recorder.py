from __future__ import division
import numpy as np
import rospy
import pylab
from collections import deque
from geometry_msgs.msg import Wrench, WrenchStamped
from std_msgs.msg import String, Header, Time
from scipy import stats
import math

hand="l"

class torque_recorder ():
    def __init__(self):
        self.num=input("Enter Trial Number: ")
        rospy.init_node('Torque_listener', anonymous=False)
        self.tmag=deque([])
        self.torque_x=deque([])
        self.torque_y=deque([])
        self.torque_z=deque([])
        self.torque_t=deque([])
        self.torque_tn=deque([])
        self.xfname="Trial%s_tx_part"%self.num
        self.yfname="Trial%s_ty_part"%self.num
        self.zfname="Trial%s_tz_part"%self.num
        self.tfname="Trial%s_tt_part"%self.num
        self.magname="Trial%s_tmag_part"%self.num
        self.part="0"
        self.file0x=open(self.xfname + "0", "w")
        self.file0y=open(self.yfname + "0", "w")
        self.file0z=open(self.zfname + "0", "w")
        self.file0t=open(self.tfname + "0", "w")
        self.file0m=open(self.magname + "0", "w") 
        self.file1x=open(self.xfname + "1", "w")
        self.file1y=open(self.yfname + "1", "w")
        self.file1z=open(self.zfname + "1", "w")
        self.file1t=open(self.tfname + "1", "w")
        self.file1m=open(self.magname + "1", "w") 
        self.file2x=open(self.xfname + "2", "w")
        self.file2y=open(self.yfname + "2", "w")
        self.file2z=open(self.zfname + "2", "w")
        self.file2t=open(self.tfname + "2", "w")
        self.file2m=open(self.magname + "2", "w")
        self.file3x=open(self.xfname + "3", "w")
        self.file3y=open(self.yfname + "3", "w")
        self.file3z=open(self.zfname + "3", "w")
        self.file3t=open(self.tfname + "3", "w")
        self.file3m=open(self.magname + "3", "w")
        self.file4x=open(self.xfname + "4", "w")
        self.file4y=open(self.yfname + "4", "w")
        self.file4z=open(self.zfname + "4", "w")
        self.file4t=open(self.tfname + "4", "w")
        self.file4m=open(self.magname + "4", "w")
        self.file5x=open(self.xfname + "5", "w")
        self.file5y=open(self.yfname + "5", "w")
        self.file5z=open(self.zfname + "5", "w")
        self.file5t=open(self.tfname + "5", "w")
        self.file5m=open(self.magname + "5", "w")
        self.file6x=open(self.xfname + "6", "w")
        self.file6y=open(self.yfname + "6", "w")
        self.file6z=open(self.zfname + "6", "w")
        self.file6t=open(self.tfname + "6", "w")
        self.file6m=open(self.magname + "6", "w")
        self.file7x=open(self.xfname + "7", "w")
        self.file7y=open(self.yfname + "7", "w")
        self.file7z=open(self.zfname + "7", "w")
        self.file7t=open(self.tfname + "7", "w")
        self.file7m=open(self.magname + "7", "w")
        self.file8x=open(self.xfname + "8", "w")
        self.file8y=open(self.yfname + "8", "w")
        self.file8z=open(self.zfname + "8", "w")
        self.file8t=open(self.tfname + "8", "w")
        self.file8m=open(self.magname + "8", "w")
        self.file9x=open(self.xfname + "9", "w")
        self.file9y=open(self.yfname + "9", "w")
        self.file9z=open(self.zfname + "9", "w")
        self.file9t=open(self.tfname + "9", "w")
        self.file9m=open(self.magname + "9", "w")
        self.file10x=open(self.xfname + "10", "w")
        self.file10y=open(self.yfname + "10", "w")
        self.file10z=open(self.zfname + "10", "w")
        self.file10t=open(self.tfname + "10", "w")
        self.file10m=open(self.magname + "10", "w")
        self.file11x=open(self.xfname + "11", "w")
        self.file11y=open(self.yfname + "11", "w")
        self.file11z=open(self.zfname + "11", "w")
        self.file11t=open(self.tfname + "11", "w")
        self.file11m=open(self.magname + "11", "w")
        self.message='b'

        rospy.Subscriber("ft/%s_gripper_motor"%hand, WrenchStamped, self.callback)
        rospy.Subscriber('Main_Control', String, self.listen)
            
 
    def callback(self, msg):
        self.torque_t.append(msg.header.stamp.secs)
        self.torque_tn.append(msg.header.stamp.nsecs)
        self.torque_x.append(msg.wrench.torque.x)  #average the samples from the message 
        self.torque_y.append(msg.wrench.torque.y)
        self.torque_z.append(msg.wrench.torque.z)
        if self.message is 'b':
            self.t0=self.torque_t[0]
            self.message='e'  
        self.worknstuff()
    
    def listen(self, msg):
        self.message=msg.data
        if self.message is "Part0":
            self.part="0"                   #when the PR2 is switching between controllers, node will  
        elif self.message is "Part1":
            self.part="1"
        elif self.message is "Part2":
            self.part="2"
        elif self.message is "Part3":
            self.part="3"
        elif self.message is "Part4":
            self.part="4"
        elif self.message is "Part5":
            self.part="5"
        elif self.message is "Part6":
            self.part="6"
        elif self.message is "Part7":
            self.part="7"
        elif self.message is "Part8":
            self.part="8"
        elif self.message is "Part9":
            self.part="9"
        elif self.message is "Part10":
            self.part="10"
        elif self.message is "Part11":
            self.part="11"
        self.worknstuff()           
            
    def worknstuff (self):
        #Calculate magnitude of the newest point and add to magnitude deque 
        self.tmag.append(math.sqrt(self.torque_x[-1]**2+self.torque_y[-1]**2+self.torque_z[-1]**2))
        
        index=range(0, len(self.torque_x))  
        if self.part is "0": 
            for i in index:
                a=self.torque_x.popleft()
                self.file0x.write(str(a)+'\n')
                b=self.torque_y.popleft()
                self.file0y.write(str(b)+'\n')
                c=self.torque_z.popleft()
                self.file0z.write(str(c)+'\n')
                d=self.torque_t.popleft()+(10**-9)*(self.torque_tn.popleft()) -self.t0
                self.file0t.write(str(d)+'\n')
                e=self.tmag.popleft()
                self.file0m.write(str(e)+'\n')
        if self.part is "1": 
            for i in index:
                a=self.torque_x.popleft()
                self.file1x.write(str(a)+'\n')
                b=self.torque_y.popleft()
                self.file1y.write(str(b)+'\n')
                c=self.torque_z.popleft()
                self.file1z.write(str(c)+'\n')
                d=self.torque_t.popleft()+(10**-9)*(self.torque_tn.popleft()) -self.t0
                self.file1t.write(str(d)+'\n')
                e=self.tmag.popleft()
                self.file1m.write(str(e)+'\n')
        if self.part is "2": 
            for i in index:
                a=self.torque_x.popleft()
                self.file2x.write(str(a)+'\n')
                b=self.torque_y.popleft()
                self.file2y.write(str(b)+'\n')
                c=self.torque_z.popleft()
                self.file2z.write(str(c)+'\n')
                d=self.torque_t.popleft()+(10**-9)*(self.torque_tn.popleft()) -self.t0
                self.file2t.write(str(d)+'\n')
                e=self.tmag.popleft()
                self.file2m.write(str(e)+'\n')
        if self.part is "3":
             for i in index:
                a=self.torque_x.popleft()
                self.file3x.write(str(a)+'\n')
                b=self.torque_y.popleft()
                self.file3y.write(str(b)+'\n')
                c=self.torque_z.popleft()
                self.file3z.write(str(c)+'\n')
                d=self.torque_t.popleft()+(10**-9)*(self.torque_tn.popleft()) -self.t0
                self.file3t.write(str(d)+'\n')
                e=self.tmag.popleft()
                self.file3m.write(str(e)+'\n')
        if self.part is "4":        
             for i in index:
                a=self.torque_x.popleft()
                self.file4x.write(str(a)+'\n')
                b=self.torque_y.popleft()
                self.file4y.write(str(b)+'\n')
                c=self.torque_z.popleft()
                self.file4z.write(str(c)+'\n')
                d=self.torque_t.popleft()+(10**-9)*(self.torque_tn.popleft()) -self.t0
                self.file4t.write(str(d)+'\n')
                e=self.tmag.popleft()
                self.file4m.write(str(e)+'\n')
        if self.part is "5":        
            for i in index:
                a=self.torque_x.popleft()
                self.file5x.write(str(a)+'\n')
                b=self.torque_y.popleft()
                self.file5y.write(str(b)+'\n')
                c=self.torque_z.popleft()
                self.file5z.write(str(c)+'\n')
                d=self.torque_t.popleft()+(10**-9)*(self.torque_tn.popleft()) -self.t0
                self.file5t.write(str(d)+'\n')
                e=self.tmag.popleft()
                self.file5m.write(str(e)+'\n')    
   
        if self.part is "6":
            for i in index:
                a=self.torque_x.popleft()
                self.file6x.write(str(a)+'\n')
                b=self.torque_y.popleft()
                self.file6y.write(str(b)+'\n')
                c=self.torque_z.popleft()
                self.file6z.write(str(c)+'\n')
                d=self.torque_t.popleft()+(10**-9)*(self.torque_tn.popleft()) -self.t0
                self.file6t.write(str(d)+'\n')
                e=self.tmag.popleft()
                self.file6m.write(str(e)+'\n')
        if self.part is "7":        
            for i in index:
                a=self.torque_x.popleft()
                self.file7x.write(str(a)+'\n')
                b=self.torque_y.popleft()
                self.file7y.write(str(b)+'\n')
                c=self.torque_z.popleft()
                self.file7z.write(str(c)+'\n')
                d=self.torque_t.popleft()+(10**-9)*(self.torque_tn.popleft()) -self.t0
                self.file7t.write(str(d)+'\n')
                e=self.tmag.popleft()
                self.file7m.write(str(e)+'\n')
        if self.part is "8":        
            for i in index:
                a=self.torque_x.popleft()
                self.file8x.write(str(a)+'\n')
                b=self.torque_y.popleft()
                self.file8y.write(str(b)+'\n')
                c=self.torque_z.popleft()
                self.file8z.write(str(c)+'\n')
                d=self.torque_t.popleft()+(10**-9)*(self.torque_tn.popleft()) -self.t0
                self.file8t.write(str(d)+'\n')
                e=self.tmag.popleft()
                self.file8m.write(str(e)+'\n')
        if self.part is "9":        
            for i in index:
                a=self.torque_x.popleft()
                self.file9x.write(str(a)+'\n')
                b=self.torque_y.popleft()
                self.file9y.write(str(b)+'\n')
                c=self.torque_z.popleft()
                self.file9z.write(str(c)+'\n')
                d=self.torque_t.popleft()+(10**-9)*(self.torque_tn.popleft()) -self.t0
                self.file9t.write(str(d)+'\n')
                e=self.tmag.popleft()
                self.file9m.write(str(e)+'\n')
        if self.part is "10":        
            for i in index:
                a=self.torque_x.popleft()
                self.file10x.write(str(a)+'\n')
                b=self.torque_y.popleft()
                self.file10y.write(str(b)+'\n')
                c=self.torque_z.popleft()
                self.file10z.write(str(c)+'\n')
                d=self.torque_t.popleft()+(10**-9)*(self.torque_tn.popleft()) -self.t0
                self.file10t.write(str(d)+'\n')
                e=self.tmag.popleft()
                self.file10m.write(str(e)+'\n')
        if self.part is "11":        
            for i in index:
                a=self.torque_x.popleft()
                self.file11x.write(str(a)+'\n')
                b=self.torque_y.popleft()
                self.file11y.write(str(b)+'\n')
                c=self.torque_z.popleft()
                self.file11z.write(str(c)+'\n')
                d=self.torque_t.popleft()+(10**-9)*(self.torque_tn.popleft()) -self.t0
                self.file11t.write(str(d)+'\n')
                e=self.tmag.popleft()
                self.file11m.write(str(e)+'\n')
        if self.message is 'stop':
            self.closefiles()

    def closefiles(self):
        self.file0x.close
        self.file0y.close
        self.file0z.close
        self.file0t.close
        self.file0m.close 
        self.file1x.close
        self.file1y.close
        self.file1z.close
        self.file1t.close
        self.file1m.close 
        self.file2x.close
        self.file2y.close
        self.file2z.close
        self.file2t.close
        self.file2m.close
        self.file3x.close
        self.file3y.close
        self.file3z.close
        self.file3t.close
        self.file3m.close
        self.file4x.close
        self.file4y.close
        self.file4z.close
        self.file4t.close
        self.file4m.close
        self.file5x.close
        self.file5y.close
        self.file5z.close
        self.file5t.close
        self.file5m.close
        self.file6x.close
        self.file6y.close
        self.file6z.close
        self.file6t.close
        self.file6m.close
        self.file7x.close
        self.file7y.close
        self.file7z.close
        self.file7t.close
        self.file7m.close
        self.file8x.close
        self.file8y.close
        self.file8z.close
        self.file8t.close
        self.file8m.close
        self.file9x.close
        self.file9y.close
        self.file9z.close
        self.file9t.close
        self.file9m.close
        self.file10x.close
        self.file10y.close
        self.file10z.close
        self.file10t.close
        self.file10m.close
        self.file11x.close
        self.file11y.close
        self.file11z.close
        self.file11t.close
        self.file11m.close
if __name__=='__main__':
    callthis=torque_recorder()
    while not rospy.is_shutdown():
        rospy.spin()
