import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2,sqrt


def get_turtlesim_pose(data):
    global bot_pose
    bot_pose = data
    bot_pose.x = data.x
    bot_pose.y = data.y
    bot_pose.theta = data.theta

def send_turtlesim_cmd_vel():
    global bot_pose, pub,desired_pose

    distance_to_goal = sqrt(pow((desired_pose.x-bot_pose.x),2)+ pow((desired_pose.y - bot_pose.y),2))
    angle_to_goal  = atan2(desired_pose.y-bot_pose.y,desired_pose.x-bot_pose.x)
    node.get_logger().debug ('My log message %d' % (angle_to_goal))
    # angle_to_turn = angle_to_goal-bot_pose.theta
    new_vel = Twist()
    
    distance_tol = 0.1
    angle_tolrence = 0.01
    kp = 1.0

    angle_to_turn = angle_to_goal-bot_pose.theta

    if abs(angle_to_turn) > angle_tolrence:
        new_vel.angular.z = kp * angle_to_turn
    else:
        if(distance_to_goal)>=distance_tol:
            new_vel.linear.x = kp *distance_to_goal
        else:
            # self.get_logger().info("goal_reached")
            new_vel.linear.x = 0.0
            quit()
    pub.publish(new_vel)


def main(args=None):
    rclpy.init(args=args)

    global node, pub,desired_pose
    node=Node("go_to_position_node")
    node.create_subscription(Pose,'/turtle1/pose',get_turtlesim_pose,10)
    desired_pose = Pose()
    desired_pose.x = 2.70
    desired_pose.y = 2.6
    pub = node.create_publisher(Twist,'/turtle1/cmd_vel',10)
    node.create_timer(1.0,send_turtlesim_cmd_vel)
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=='__main__':
    main()