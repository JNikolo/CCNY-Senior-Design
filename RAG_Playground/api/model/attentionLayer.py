import tensorflow as tf
from tensorflow.keras.layers import Layer

class ScaledDotProductAttention(Layer):
    def __init__(self, **kwargs):
        super(ScaledDotProductAttention, self).__init__(**kwargs)

    def call(self, inputs):
        encoder_out_seq, decoder_out_seq = inputs

        #Calculate the dot products
        scores = tf.matmul(decoder_out_seq, encoder_out_seq, transpose_b=True)

        #Scale the scores
        d_k = tf.cast(tf.shape(encoder_out_seq)[-1], tf.float32)
        scaled_scores = scores / tf.sqrt(d_k)
        #Calculate attention weights
        attention_weights = tf.nn.softmax(scaled_scores, axis=-1)

        #Compute the context vector
        context_vector = tf.matmul(attention_weights, encoder_out_seq)

        return context_vector, attention_weights

    def compute_output_shape(self, input_shape):
        return [
            tf.TensorShape((input_shape[1][0], input_shape[1][1], input_shape[0][2])),
            tf.TensorShape((input_shape[1][0], input_shape[1][1], input_shape[0][1]))
        ]
