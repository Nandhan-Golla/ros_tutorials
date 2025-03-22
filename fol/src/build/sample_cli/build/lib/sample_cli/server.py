import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class Server(Node):

    def __init__(self):
        super().__init__('server')
        self.srv = self.create_service(AddTwoInts, 'topic', self.callback)
        self.get_logger().info('Node started: !')



    def callback(self, request, response):

        response.sum = request.a + request.b
        self.get_logger().info("Returning the Nodes")

        return response
    
def main(args=None):
    with rclpy.init(args=args):
        try:
            node = Server()
            rclpy.spin(node)

        except KeyboardInterrupt:
            pass

        finally:
            node.destroy_node()
            rclpy.shutdown()

    

