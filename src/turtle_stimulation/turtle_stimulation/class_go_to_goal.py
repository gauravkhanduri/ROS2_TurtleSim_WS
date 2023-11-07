import rclpy
from turtlesim.msg import Pose
import math
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys

class Driver_node(Node):
    def __init__(self):
        super().__init__("Go_to_goal_node")
        self.cmd_vel_pub = self.create_publisher(Twist,'/turtle1/cmd_vel',10)
        self.pose_sub = self.create_subscription(Pose,'/turtle1/pose',self.pose_callback_,10)
        self.timer = self.create_timer(0.1,self.go_to_goal)
        self.pose = None
    
    def pose_callback_(self, data):
        self.pose = data
    
    def go_to_goal(self):
        goal = Pose()
        goal.x = float(sys.argv[1])
        goal.y = float(sys.argv[2])
        # goal.theta = float(sys.argv[3])
        kp = float(sys.argv[3])

        new_vel = Twist()

        distance_to_goal = math.sqrt((goal.x-self.pose.x)**2 + (goal.y-self.pose.y)**2)

        angle_to_goal = math.atan2((goal.y-self.pose.y),(goal.x-self.pose.x))

        distance_tol = 0.3
        angle_tol = 0.3
        # kp = 1.5
        angle_error = angle_to_goal-self.pose.theta

        if abs(angle_error) > angle_tol:
            new_vel.angular.z =  kp *0.5
        else:
            if distance_to_goal > distance_tol:
                new_vel.linear.x = kp *0.5
            else:
                new_vel.linear.x = 0.0
                self.get_logger().info("Goal_reached")
        self.cmd_vel_pub.publish(new_vel)

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = Driver_node()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()





