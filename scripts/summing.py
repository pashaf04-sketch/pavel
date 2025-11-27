#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray

def callback(data):
    try:
        print(f"[Summing] 📥 Получил: {data.data}")  # Отладка
        total = sum(data.data)
        pub.publish(Float32MultiArray(data=[total]))
        print(f"[Summing] 📤 Отправил результат: {total}")  # Отладка
    except Exception as e:
        print(f"[Summing] ❌ Ошибка: {e}")

rospy.init_node('summing_node')
sub = rospy.Subscriber('/lab3/polynomial_result', Float32MultiArray, callback)
pub = rospy.Publisher('/lab3/final_result', Float32MultiArray, queue_size=10,latch=True)

print("[Summing] 🟢 Запущен и ждёт данные...")
rospy.spin()
