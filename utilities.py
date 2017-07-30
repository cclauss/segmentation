def PReLU(x):
    """
    - DOES:

    - INPUT:

    - OUTPUT:
    """

    # (based on the implementation by kwotsin)

    # (PReLU(x) = x if x > 0, alpha*x otherwise)

    alpha = tf.get_variable("alpha", shape=[1],
                initializer=tf.constant_initializer(0), dtype=tf.float32)

    output = tf.nn.relu(x) + alpha*(x - abs(x))*0.5

    return output

def spatial_dropout(x, drop_prob, training=True):
    """
    - DOES:

    - INPUT:

    - OUTPUT:
    """

    # (based on the implementation by kwotsin)

    # x is a tensor of shape [batch_size, fb_height, fb_width, fb_depth]
    # where fb stands for "feature block"

    if training:
        keep_prob = 1.0 - drop_prob
        input_shape = x.get_shape().as_list()

        batch_size = input_shape[0]
        fb_depth = input_shape[3]

        # drop each feature block layer with probability drop_prob:
        noise_shape = tf.constant(value=[batch_size, 1, 1, fb_depth])
        x_drop = tf.nn.dropout(x, keep_prob, noise_shape=noise_shape)

        output = x_drop
    else:
        output = x

    return output

def unpool(x, mask, kernel_shape=[1, 2, 2, 1]):
    """
    - DOES:

    - INPUT:

    - OUTPUT:
    """

    # (based on the implementation by kwotsin)

    input_shape = x.get_shape().as_list()
    batch_size, fb_height, fb_width, fb_depth = (input_shape[0], input_shape[1],
                input_shape[2], input_shape[3])

    output_shape = (batch_size, fb_height*kernel_shape[1],
                fb_width*kernel_shape[2], fb_depth)

    # TODO!

    return 0