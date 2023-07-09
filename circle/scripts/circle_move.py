#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def circle_move():
    # Create a new node
    rospy.init_node('circle_move_node', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    
    #assigning the values to linear and angular variables 
    angular_speed = 2.0
    linear_speed = 2.0
    radius = 2.0
    circumference = 2.0 * 3.14159 * radius
    num_revolutions = 1
    distance = num_revolutions * circumference

    # Calculate the time it will take to complete the circle
    time = distance / linear_speed

    # Create a Twist message and set the linear and angular velocities
    vel_msg = Twist()
    vel_msg.linear.x = linear_speed
    vel_msg.angular.z = angular_speed

    # Get the current time
    start_time = rospy.Time.now().to_sec()

    # Main loop to move the turtle in a circle
    while not rospy.is_shutdown():
        # Publish the velocity message
        velocity_publisher.publish(vel_msg)

        # Get the current time
        current_time = rospy.Time.now().to_sec()

        # Check if the turtle has completed the circle
        if current_time - start_time >= time:
            # Stop the turtle
            vel_msg.linear.x = 0.0
            vel_msg.angular.z = 0.0
            velocity_publisher.publish(vel_msg)
            break

        # Sleep to maintain the desired rate
        rate.sleep()

if __name__ == '__main__':
    try:
        # Call the circle_move function
        circle_move()
    except rospy.ROSInterruptException:
        pass
