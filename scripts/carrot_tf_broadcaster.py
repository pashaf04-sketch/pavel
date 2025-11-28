#!/usr/bin/env python3

import rospy
import tf
from turtlesim.msg import Pose
import math
from visualization_msgs.msg import Marker

def pose_callback(pose):
    global br, current_time, marker_pub
    current_time = rospy.Time.now()

    # Публикуем трансформацию turtle1 -> world
    br.sendTransform(
        (pose.x, pose.y, 0.0),
        tf.transformations.quaternion_from_euler(0, 0, pose.theta),
        current_time,
        "turtle1",
        "world"
    )

    # Параметры вращения морковки
    radius = 1.0
    frequency = 0.1
    angle = frequency * 2 * math.pi * current_time.to_sec()

    x_carrot = radius * math.cos(angle)
    y_carrot = radius * math.sin(angle)

    # Публикуем трансформацию carrot -> turtle1
    br.sendTransform(
        (x_carrot, y_carrot, 0.0),
        tf.transformations.quaternion_from_euler(0, 0, 0),
        current_time,
        "carrot",
        "turtle1"
    )

    # Создаем маркер — оранжевый конус (морковка)
    marker = Marker()
    marker.header.frame_id = "carrot"
    marker.header.stamp = current_time
    marker.ns = "carrot_marker"
    marker.id = 0
    marker.type = 0
    marker.action = Marker.ADD
    marker.pose.position.x = 0.0
    marker.pose.position.y = 0.0
    marker.pose.position.z = 0.0
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0
    marker.scale.x = 0.3  # ширина основания
    marker.scale.y = 0.3  # глубина основания
    marker.scale.z = 0.5  # высота
    marker.color.a = 1.0
    marker.color.r = 1.0  # красный
    marker.color.g = 0.6  # зелёный (оранжевый)
    marker.color.b = 0.0  # синий

    marker_pub.publish(marker)

if __name__ == '__main__':
    rospy.init_node('carrot_tf_broadcaster')
    br = tf.TransformBroadcaster()
    current_time = rospy.Time.now()

    # Публикатор маркеров
    marker_pub = rospy.Publisher('/visualization_marker', Marker, queue_size=10)

    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)

    rospy.spin()
