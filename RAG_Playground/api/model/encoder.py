from tensorflow.keras.models import Model
from tensorflow.keras.layers import Concatenate

class Encoder:
    def __init__(self, my_model):
        # Define the encoder model
        encoder_inputs = my_model.input[0]  # Input for encoder
        encoder_bidirectional_layer = my_model.get_layer('bidirectional_2')  # The last bidirectional LSTM layer
        encoder_outputs, forward_h3, forward_c3, backward_h3, backward_c3 = encoder_bidirectional_layer.output

        # Concatenate the forward and backward states
        encoder_state_h = Concatenate()([forward_h3, backward_h3])
        encoder_state_c = Concatenate()([forward_c3, backward_c3])

        # Encoder model outputs the encoder outputs for attention, and the final hidden/cell states
        self.encoder_model = Model(inputs=encoder_inputs, outputs=[encoder_outputs, encoder_state_h, encoder_state_c])
    
    def predict(self, input_seq):
        return self.encoder_model.predict(input_seq, verbose=0)
