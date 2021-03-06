from __future__ import division
import numpy as np
import rospy
from collections import deque
from geometry_msgs.msg import Wrench, WrenchStamped
from std_msgs.msg import String, Header, Time
import math

hand="l"

class force_recorder ():
    def __init__(self):
        self.num=input("Enter Trial Number: ")
        rospy.init_node('Force_listener', anonymous=False)
        self.fmag=deque([])
        self.force_x=deque([])
        self.force_y=deque([])
        self.force_z=deque([])
        self.force_t=deque([])
        self.force_tn=deque([])
        self.xfname="./Trial/Trial%s_fx_part"%self.num
        self.yfname="./Trial/Trial%s_fy_part"%self.num
        self.zfname="./Trial/Trial%s_fz_part"%self.num
        self.tfname="./Trial/Trial%s_ft_part"%self.num
        self.magname="./Trial/Trial%s_fmag_part"%self.num
        self.part="-1"
        self.file0x=open(self.xfname + "0", "w")
        self.file0y=open(self.yfname + "0", "w")
        self.file0z=open(self.zfname + "0", "w")
        self.file0t=open(self.tfname + "0", "w")
        self.file0f=open(self.magname + "0", "w") 
        self.file1x=open(self.xfname + "1", "w")
        self.file1y=open(self.yfname + "1", "w")
        self.file1z=open(self.zfname + "1", "w")
        self.file1t=open(self.tfname + "1", "w")
        self.file1f=open(self.magname + "1", "w") 
        self.file2x=open(self.xfname + "2", "w")
        self.file2y=open(self.yfname + "2", "w")
        self.file2z=open(self.zfname + "2", "w")
        self.file2t=open(self.tfname + "2", "w")
        self.file2f=open(self.magname + "2", "w")
        self.file3x=open(self.xfname + "3", "w")
        self.file3y=open(self.yfname + "3", "w")
        self.file3z=open(self.zfname + "3", "w")
        self.file3t=open(self.tfname + "3", "w")
        self.file3f=open(self.magname + "3", "w")
        self.file4x=open(self.xfname + "4", "w")
        self.file4y=open(self.yfname + "4", "w")
        self.file4z=open(self.zfname + "4", "w")
        self.file4t=open(self.tfname + "4", "w")
        self.file4f=open(self.magname + "4", "w")
        self.file5x=open(self.xfname + "5", "w")
        self.file5y=open(self.yfname + "5", "w")
        self.file5z=open(self.zfname + "5", "w")
        self.file5t=open(self.tfname + "5", "w")
        self.file5f=open(self.magname + "5", "w")
        self.file6x=open(self.xfname + "6", "w")
        self.file6y=open(self.yfname + "6", "w")
        self.file6z=open(self.zfname + "6", "w")
        self.file6t=open(self.tfname + "6", "w")
        self.file6f=open(self.magname + "6", "w")
        self.file7x=open(self.xfname + "7", "w")
        self.file7y=open(self.yfname + "7", "w")
        self.file7z=open(self.zfname + "7", "w")
        self.file7t=open(self.tfname + "7", "w")
        self.file7f=open(self.magname + "7", "w")
        self.file8x=open(self.xfname + "8", "w")
        self.file8y=open(self.yfname + "8", "w")
        self.file8z=open(self.zfname + "8", "w")
        self.file8t=open(self.tfname + "8", "w")
        self.file8f=open(self.magname + "8", "w")
        self.file9x=open(self.xfname + "9", "w")
        self.file9y=open(self.yfname + "9", "w")
        self.file9z=open(self.zfname + "9", "w")
        self.file9t=open(self.tfname + "9", "w")
        self.file9f=open(self.magname + "9", "w")
        self.file10x=open(self.xfname + "10", "w")
        self.file10y=open(self.yfname + "10", "w")
        self.file10z=open(self.zfname + "10", "w")
        self.file10t=open(self.tfname + "10", "w")
        self.file10f=open(self.magname + "10", "w")
        self.file11x=open(self.xfname + "11", "w")
        self.file11y=open(self.yfname + "11", "w")
        self.file11z=open(self.zfname + "11", "w")
        self.file11t=open(self.tfname + "11", "w")
        self.file11f=open(self.magname + "11", "w")
        self.message='b'
 
        rospy.Subscriber("ft/%s_gripper_motor"%hand, WrenchStamped, self.callback)
        rospy.Subscriber('Main_Control', String, self.listen)
            
 
    def callback(self, msg):
        self.force_t.append(msg.header.stamp.secs)
        self.force_tn.append(msg.header.stamp.nsecs)
        self.force_x.append(msg.wrench.force.x)  #average the samples from the message 
        self.force_y.append(msg.wrench.force.y)
        self.force_z.append(msg.wrench.force.z)
        if self.message is 'b':
            self.t0=self.force_t[0]
            self.message='e'  
        self.worknstuff()
    
    def listen(self, msg):
        self.message=msg.data                   #when the PR2 is switching between controllers, node will  
        if self.message[-2] is 't':
            self.part=self.message[-1]
        else:
            if self.message[-1] is '0': 
                self.part='10'
            elif self.message[-1] is '1':
                self.part='11'          
            
        
        if self.message[-1] is 'P':
            print("Stop recording")
            self.closefiles()
        self.worknstuff()           
            
    def worknstuff (self):
        #Calculate magnitude of the newest point and add to magnitude deque 
        if len(self.force_x)>=1:
            self.fmag.append(math.sqrt(self.force_x[-1]**2+self.force_y[-1]**2+self.force_z[-1]**2))
        
        index=range(0, len(self.force_x))
        magindex=range(0, len(self.fmag))
   
        if self.part is "0":
            for i in index:
                a=self.force_x.popleft()
                self.file0x.write(str(a)+'\n')
                b=self.force_y.popleft()
                self.file0y.write(str(b)+'\n')
                c=self.force_z.popleft()
                self.file0z.write(str(c)+'\n')
                d=self.force_t.popleft() + (10**-9)*(self.force_tn.popleft()) -self.t0
                self.file0t.write(str(d)+'\n')
                e=self.fmag.popleft()
                self.file0f.write(str(e)+'\n')
        if self.part is "1": 
            for i in index:
                a=self.force_x.popleft()
                self.file1x.write(str(a)+'\n')
                b=self.force_y.popleft()
                self.file1y.write(str(b)+'\n')
                c=self.force_z.popleft()
                self.file1z.write(str(c)+'\n')
                d=self.force_t.popleft() + (10**-9)*(self.force_tn.popleft()) -self.t0
                self.file1t.write(str(d)+'\n')
                e=self.fmag.popleft()
                self.file1f.write(str(e)+'\n')
        if self.part is "2": 
            for i in index:
                a=self.force_x.popleft()
                self.file2x.write(str(a)+'\n')
                b=self.force_y.popleft()
                self.file2y.write(str(b)+'\n')
                c=self.force_z.popleft()
                self.file2z.write(str(c)+'\n')
                d=self.force_t.popleft() + (10**-9)*(self.force_tn.popleft()) -self.t0
                self.file2t.write(str(d)+'\n')
                e=self.fmag.popleft()
                self.file2f.write(str(e)+'\n')
        if self.part is "3":
             for i in index:
                a=self.force_x.popleft()
                self.file3x.write(str(a)+'\n')
                b=self.force_y.popleft()
                self.file3y.write(str(b)+'\n')
                c=self.force_z.popleft()
                self.file3z.write(str(c)+'\n')
                d=self.force_t.popleft() + (10**-9)*(self.force_tn.popleft()) -self.t0
                self.file3t.write(str(d)+'\n')
                e=self.fmag.popleft()
                self.file3f.write(str(e)+'\n')
        if self.part is "4":        
             for i in index:
                a=self.force_x.popleft()
                self.file4x.write(str(a)+'\n')
                b=self.force_y.popleft()
                self.file4y.write(str(b)+'\n')
                c=self.force_z.popleft()
                self.file4z.write(str(c)+'\n')
                d=self.force_t.popleft() + (10**-9)*(self.force_tn.popleft()) -self.t0
                self.file4t.write(str(d)+'\n')
                e=self.fmag.popleft()
                self.file4f.write(str(e)+'\n')
        if self.part is "5":        
            for i in index:
                a=self.force_x.popleft()
                self.file5x.write(str(a)+'\n')
                b=self.force_y.popleft()
                self.file5y.write(str(b)+'\n')
                c=self.force_z.popleft()
                self.file5z.write(str(c)+'\n')
                d=self.force_t.popleft() + (10**-9)*(self.force_tn.popleft()) -self.t0
                self.file5t.write(str(d)+'\n')
                e=self.fmag.popleft()
                self.file5f.write(str(e)+'\n')    
   
        if self.part is "6":
            for i in index:
                a=self.force_x.popleft()
                self.file6x.write(str(a)+'\n')
                b=self.force_y.popleft()
                self.file6y.write(str(b)+'\n')
                c=self.force_z.popleft()
                self.file6z.write(str(c)+'\n')
                d=self.force_t.popleft() + (10**-9)*(self.force_tn.popleft()) -self.t0
                self.file6t.write(str(d)+'\n')
                e=self.fmag.popleft()
                self.file6f.write(str(e)+'\n')
        if self.part is "7":        
            for i in index:
                a=self.force_x.popleft()
                self.file7x.write(str(a)+'\n')
                b=self.force_y.popleft()
                self.file7y.write(str(b)+'\n')
                c=self.force_z.popleft()
                self.file7z.write(str(c)+'\n')
                d=self.force_t.popleft() + (10**-9)*(self.force_tn.popleft()) -self.t0
                self.file7t.write(str(d)+'\n')
                e=self.fmag.popleft()
                self.file7f.write(str(e)+'\n')
        if self.part is "8":        
            for i in index:
                a=self.force_x.popleft()
                self.file8x.write(str(a)+'\n')
                b=self.force_y.popleft()
                self.file8y.write(str(b)+'\n')
                c=self.force_z.popleft()
                self.file8z.write(str(c)+'\n')
                d=self.force_t.popleft() + (10**-9)*(self.force_tn.popleft()) -self.t0
                self.file8t.write(str(d)+'\n')
                e=self.fmag.popleft()
                self.file8f.write(str(e)+'\n')
        if self.part is "9":        
            for i in index:
                a=self.force_x.popleft()
                self.file9x.write(str(a)+'\n')
                b=self.force_y.popleft()
                self.file9y.write(str(b)+'\n')
                c=self.force_z.popleft()
                self.file9z.write(str(c)+'\n')
                d=self.force_t.popleft() + (10**-9)*(self.force_tn.popleft()) -self.t0
                self.file9t.write(str(d)+'\n')
                e=self.fmag.popleft()
                self.file9f.write(str(e)+'\n')
        if self.part is "10":        
            for i in index:
                a=self.force_x.popleft()
                self.file10x.write(str(a)+'\n')
                b=self.force_y.popleft()
                self.file10y.write(str(b)+'\n')
                c=self.force_z.popleft()
                self.file10z.write(str(c)+'\n')
                d=self.force_t.popleft() + (10**-9)*(self.force_tn.popleft()) -self.t0
                self.file10t.write(str(d)+'\n')
                e=self.fmag.popleft()
                self.file10f.write(str(e)+'\n')
        if self.part is "11":        
            for i in index:
                a=self.force_x.popleft()
                self.file11x.write(str(a)+'\n')
                b=self.force_y.popleft()
                self.file11y.write(str(b)+'\n')
                c=self.force_z.popleft()
                self.file11z.write(str(c)+'\n')
                d=self.force_t.popleft() + (10**-9)*(self.force_tn.popleft()) -self.t0
                self.file11t.write(str(d)+'\n')
                e=self.fmag.popleft()
                self.file11f.write(str(e)+'\n')

    def closefiles(self):
        print("*closing files")
        self.file1x.close
        self.file1y.close
        self.file1z.close
        self.file1t.close
        self.file1f.close 
        self.file2x.close
        self.file2y.close
        self.file2z.close
        self.file2t.close
        self.file2f.close
        self.file3x.close
        self.file3y.close
        self.file3z.close
        self.file3t.close
        self.file3f.close
        self.file4x.close
        self.file4y.close
        self.file4z.close
        self.file4t.close
        self.file4f.close
        self.file5x.close
        self.file5y.close
        self.file5t.close
        self.file5f.close
        self.file6x.close
        self.file6y.close
        self.file6z.close
        self.file6t.close
        self.file6f.close
        self.file7x.close
        self.file7y.close
        self.file7z.close
        self.file7t.close
        self.file7f.close
        self.file8x.close
        self.file8y.close
        self.file8z.close
        self.file8t.close
        self.file8f.close
        self.file9x.close
        self.file9y.close
        self.file9z.close
        self.file9t.close
        self.file9f.close
        self.file10x.close
        self.file10y.close
        self.file10z.close
        self.file10t.close
        self.file10f.close
        self.file11x.close
        self.file11y.close
        self.file11z.close
        self.file11t.close
        self.file11f.close
    
if __name__=='__main__':
    callthis=force_recorder()
    while not rospy.is_shutdown():
        rospy.spin()
        
