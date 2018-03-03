# add_two_numbers_via_TensorFlow_TensorBoard.py

import os
import tensorflow as tf

# get the two numbers to add from the command prompt
intNum1 = int(input("enter num 1: "))
intNum2 = int(input("enter num 2: "))

# establish two tensors, one for each input number, note we add a name so we can see which node is which in TensorBoard
num1 = tf.Variable(intNum1, name="num1")
num2 = tf.Variable(intNum2, name="num2")

# establish graph
sum  = tf.add(num1, num2, name="sum")

# note that this shows information about tensorSum, but does NOT evaluate anything yet
print("sum = " + str(sum))

# instantiate a global variables initializer
globalVarsInitializer = tf.global_variables_initializer()

# finally we can run the graph (in a session)
with tf.Session() as sess:
    globalVarsInitializer.run()
    result = sum.eval()
# end with

print("result = " + str(result))

# write the graph to file so we can view with TensorBoard
fileWriter = tf.summary.FileWriter(os.getcwd())
fileWriter.add_graph(sess.graph)
fileWriter.close()

# to start TensorBoard, enter the following at a command prompt:
# tensorboard --logdir="(repository_location)"
# ex: tensorboard --logdir="C:\Users\cdahms\Documents\TensorFlow_Tut_1_Installation_and_First_Progs"
