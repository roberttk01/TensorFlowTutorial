import os
import tensorflow as tf
# Used to suppress tf warning during output // not in original tutorials
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# creates nodes in a graph
# "construction phase"
x1 = tf.constant(5)
x2 = tf.constant(6)

result = tf.multiply(x1, x2)
print(result)

# defines our session and launches graph
sess = tf.Session()
# runs result
print(sess.run(result))
sess.close()

with tf.Session() as sess:
    output = sess.run(result)
    print(output)

    matrix1 = tf.constant([[3., 3.]])
    matrix2 = tf.constant([[2.], [2.]])
    product = tf.matmul(matrix1, matrix2)
    print(product)
    product = sess.run(product)
    print(product)


