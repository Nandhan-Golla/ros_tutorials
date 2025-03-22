import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/nandhan-golla/Desktop/ros_tutorials/fol/src/install/sample_cli'
