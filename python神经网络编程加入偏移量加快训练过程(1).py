import random
import tensorflow as tf

tf.compat.v1.disable_eager_execution()# for v2

random.seed()

x = tf.compat.v1.placeholder(dtype=tf.float32)
yTrain=tf.compat.v1.placeholder(dtype=tf.float32)
#x = tf.placeholder(dtype=tf.float32)
#yTrain=tf.placeholder(dtype=tf.float32)

w=tf.Variable(tf.zeros([3]),dtype=tf.float32)
b=tf.Variable(80,dtype=tf.float32) #给b赋予初值80

wn=tf.nn.softmax(w)  #以便使得w向量中所有数值相加和为1
n1=wn*x
n2=tf.reduce_sum(n1)-b #增加偏移量b

y=tf.nn.sigmoid(n2)

loss=tf.abs(yTrain-y)

optimizer=tf.compat.v1.train.RMSPropOptimizer(0.1)
#optimizer=tf.train.RMSPropOptimizer(0.1)

train=optimizer.minimize(loss)

sess=tf.compat.v1.Session()
sess.run(tf.compat.v1.global_variables_initializer())
#sess=tf.Session()
#sess.run(tf.global_variables_initializer())

#for i in range(5):
for i in range(500):
    xData = [int(random.random()*11+90), int(random.random()*11+90), int(random.random()*11+90)]
    xAll = xData[0]*0.6+xData[1]*.3+xData[2]*.1

    if xAll>=95:
        yTrainData = 1
    else:
        yTrainData = 0

    #result = sess.run([train,x,yTrain,w,b,n2,y,loss], feed_dict={x:xData,yTrain:yTrainData})
    result = sess.run([train,x,yTrain,wn,b,n2,y,loss], feed_dict={x:xData,yTrain:yTrainData})
    print(result)

    xData = [int(random.random()*41+60), int(random.random()*41+60), int(random.random()*41+60)]
    xAll = xData[0]*0.6+xData[1]*.3+xData[2]*.1

    if xAll>=95:
        yTrainData = 1
    else:
        yTrainData = 0

    #result = sess.run([train,x,yTrain,w,b,n2,y,loss], feed_dict={x:xData,yTrain:yTrainData})
    result = sess.run([train,x,yTrain,wn,b,n2,y,loss], feed_dict={x:xData,yTrain:yTrainData})
    print(result)
