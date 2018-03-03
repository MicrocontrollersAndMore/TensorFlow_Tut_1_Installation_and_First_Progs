# add_two_numbers_via_TensorFlow.py

import tensorflow as tf

# get the two numbers to add from the command prompt
intNum1 = int(input("enter num 1: "))
intNum2 = int(input("enter num 2: "))

# establish two tensors, one for each input number
num1 = tf.Variable(intNum1)
num2 = tf.Variable(intNum2)

# establish graph
sum = tf.add(num1, num2)

# note that this shows information about sum, but does NOT evaluate anything yet
print("sum = " + str(sum))

# instantiate a global variables initializer
globalVarsInitializer = tf.global_variables_initializer()

# finally we can run the graph (in a session)
with tf.Session() as sess:
    globalVarsInitializer.run()
    result = sum.eval()
# end with

# show the result
print("result = " + str(result))
