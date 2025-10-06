import rospy
import datetime

def time_publisher():
    rospy.init_node('time_publisher_node', anonymous=True)
   
    rate = rospy.Rate(0.2)
    
    rospy.loginfo("Time publisher node started. Publishing time every 5 seconds...")
    
    while not rospy.is_shutdown():
       
        current_time = datetime.datetime.now()
        
       
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
     
        rospy.loginfo(f"Current time: {formatted_time}")
        
        rate.sleep()

if __name__ == '__main__':
    try:
        time_publisher()
    except rospy.ROSInterruptException:
        pass
