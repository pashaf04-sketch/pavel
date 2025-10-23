#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def overflow_callback(msg):
    ns = rospy.get_namespace()
    rospy.logerr(f"[{ns.strip('/')}] OVERFLOW: {msg.data}")

def overflow_timer_node():
    rospy.init_node('overflow_timer', anonymous=True)
    rospy.Subscriber('overflow_topic', String, overflow_callback)
    rospy.loginfo("Overflow timer node started.")
    rospy.spin()

if __name__ == '__main__':
    try:
        overflow_timer_node()
    except rospy.ROSInterruptException:
        pass
