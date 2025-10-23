#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32, String

def uc_publisher():
    rospy.init_node('uc_pub', anonymous=True)
    
    # Получаем namespace из параметров (если нужно) или используем текущий
    ns = rospy.get_namespace()
    rospy.loginfo(f"Node started in namespace: {ns}")

    pub_time = rospy.Publisher('time_topic', Int32, queue_size=10)
    pub_overflow = rospy.Publisher('overflow_topic', String, queue_size=10)
    
    rate = rospy.Rate(10)  # 10 Hz

    count = 0
    while not rospy.is_shutdown():
        msg_num = Int32()
        msg_num.data = count
        pub_time.publish(msg_num)
        rospy.loginfo(f"[{ns.strip('/')}] Published: {count}")

        if count >= 100:
            alert_msg = String()
            alert_msg.data = f"Overflow in {ns.strip('/')}! Count reached {count}. Resetting..."
            pub_overflow.publish(alert_msg)
            rospy.logwarn(alert_msg.data)
            count = 0
        else:
            count += 2

        rate.sleep()

if __name__ == '__main__':
    try:
        uc_publisher()
    except rospy.ROSInterruptException:
        pass
