# command_line_params.py

import tensorflow as tf
import sys
import argparse

# module level variables ##############################################################################################
FLAGS = None

#######################################################################################################################
def main(_):
    print(FLAGS.param_1)
    print(FLAGS.param_2)
    print(FLAGS.param_3)
# end main

#######################################################################################################################
if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--param_1',
                        type=str,
                        default = 'param 1 default value',
                        help='help info for param 1 here')

    parser.add_argument('--param_2',
                        type=str,
                        default = 'param 2 default value',
                        help='help info for param 2 here')

    parser.add_argument('--param_3',
                        type=str,
                        default = 'param 3 default value',
                        help='help info for param 3 here')

    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
