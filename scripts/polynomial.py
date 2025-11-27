#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray

def callback(data):
    nums = data.data
    if len(nums) != 3:
        rospy.logwarn("Expected 3 numbers, got %d", len(nums))
        return
    a, b, c = nums
    # Возводим в степени: a^1, b^2, c^3
    result = [a**3, b**2, c**1]
    pub.publish(Float32MultiArray(data=result))

rospy.init_node('polynomial_node')
sub = rospy.Subscriber('/lab3/input_numbers', Float32MultiArray, callback)
pub = rospy.Publisher('/lab3/polynomial_result', Float32MultiArray, queue_size=10)

def callback(data):
    print(f"📥 Polynomial received: {data.data}")  # <-- Добавьте эту строку
    nums = data.data
    if len(nums) != 3:
        rospy.logwarn("Expected 3 numbers, got %d", len(nums))
        return
    a, b, c = nums
    result = [a**1, b**2, c**3]
    pub.publish(Float32MultiArray(data=result))
    print(f"📤 Polynomial sent: {result}")  # <-- И эту
   
def callback(data):
    print(f"[Polynomial] 📥 Получил: {data.data}")
    if len(data.data) != 3:
        rospy.logwarn("Ожидал 3 числа, получил %d", len(data.data))
        return
    a, b, c = data.data
    result = [a**1, b**2, c**3]
    pub.publish(Float32MultiArray(data=result))
    print(f"[Polynomial] 📤 Отправил: {result}")
rospy.spin()
