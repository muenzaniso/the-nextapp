import tensorflow as tf
tf.logging.set_verbosity(tf.logging.ERROR)
import numpy as np

b = np.array([0,1,4,3,2])
print("Max : {}".format(np.max(b)))
print("Average : {}".format(np.average(b)))
print(" MAx Index : {}".format(np.argmax(b)))

print("n\You can print the type of any element")
print("Type of b {}, type of b[0] {} ".format(type(b), type(b[0])))