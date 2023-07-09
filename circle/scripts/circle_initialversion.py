#!/usr/bin/env python
import rospy
import math as m
from geometry_msgs.msg import Twist

def circle_move():
    # Creating a new node
    rospy.init_node('circle', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # Take input from the user for angular speed
    print("The turtle will move in a circle")
    ang_vel = float(input("Enter the angular speed of the turtle: "))
    radius = float(input("Enter the radius: "))

    lin_vel = ang_vel * radius

    vel_msg.angular.z = ang_vel
    vel_msg.linear.x = lin_vel

    # Set other velocities to 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    # Setting the current time for distance calculation
    t0 = rospy.Time.now().to_sec()
    current_distance = 0

    # Loop to keep the turtle moving until the circle is completed
    while current_distance < 2 * m.pi * radius and not rospy.is_shutdown():
        # Publish the velocity
        velocity_publisher.publish(vel_msg)

        # Takes actual time for velocity calculus
        t1 = rospy.Time.now().to_sec()

        # Calculates the current distance
        current_distance = lin_vel * (t1 - t0)

    # After the loop, stop the turtle
    vel_msg.angular.z = 0
    vel_msg.linear.x = 0

    # Force the turtle to stop
    velocity_publisher.publish(vel_msg)


if __name__ == '__main__':
    try:
        # Testing our function
        circle_move()
    except rospy.ROSInterruptException:
        pass
