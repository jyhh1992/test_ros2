import time

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from action_random_interfaces.action import Randomnumber

import random as ra
class RandomServer(Node):
    def __init__(self):
        super().__init__('random_5_server')
        self.action_server = ActionServer(
            self,
            Randomnumber,
            'randomnumber',
            self.execute_callback)
    
    def execute_callback(self, goal_handle):
        self.get_logger().info('골 실행중')      

        # feedback_msg = Randomnumber.Feedback()

        sequence = None



        goal_handle.succeed()

        result = RandomServer.Result()
        return result



def main(args=None):
    rclpy.init(args=args)
    random_server = RandomServer()
    rclpy.spin(random_server)


if __name__ == '__main__':
    main()