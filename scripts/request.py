#!/usr/bin/env python3
import rospy
import sys
from std_msgs.msg import Float32MultiArray

result_received = False

def result_callback(data):
    global result_received
    print(f"[Request] 📥 Получил результат: {data.data}")  
    if not result_received and len(data.data) > 0:
        print(f"✅ Окончательный результат: {data.data[0]}")
        result_received = True
        rospy.signal_shutdown("Результат получен")

def main():
    if len(sys.argv) != 4:
        print("Использование: rosrun lab3 request.py <a> <b> <c>")
        return

    try:
        nums = [float(x) for x in sys.argv[1:4]]
    except ValueError:
        print("❌ Все аргументы должны быть числами.")
        return

    rospy.init_node('request_node')

    pub = rospy.Publisher('/lab3/input_numbers', Float32MultiArray, queue_size=10)
    rospy.sleep(2.0)  

    pub.publish(Float32MultiArray(data=nums))
    print(f"📤 Отправлен запрос: {nums}")

    rospy.Subscriber('/lab3/final_result', Float32MultiArray, result_callback)
    rospy.spin()  

if __name__ == '__main__':
    main()
