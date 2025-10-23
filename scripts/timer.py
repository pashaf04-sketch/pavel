#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def time_callback(msg):
    ns = rospy.get_namespace()
    rospy.loginfo(f"[{ns.strip('/')}] Timer received: {msg.data}")

def timer_node():
    rospy.init_node('timer', anonymous=True)
    rospy.Subscriber('time_topic', Int32, time_callback)
    rospy.loginfo("Timer node started.")
    rospy.spin()

if __name__ == '__main__':
    try:
        timer_node()
    except rospy.ROSInterruptException:
        pass
