from tensorflow.keras.layers import Input, Concatenate
from tensorflow.keras.models import Model

class Decoder:
    def __init__(self, my_model, latent_dim=300, max_len_text=150):
       
        # Define the decoder model inputs
        decoder_inputs = Input(shape=(None,), name="decoder_inputs")  # Decoder input (word sequences)
        decoder_state_input_h = Input(shape=(latent_dim * 2,), name="decoder_state_input_h")  # Placeholder for initial hidden state
        decoder_state_input_c = Input(shape=(latent_dim * 2,), name="decoder_state_input_c")  # Placeholder for initial cell state
        encoder_output_input = Input(shape=(max_len_text, latent_dim * 2), name="encoder_output_input")  # Encoder outputs for attention

        # Embedding layer for the decoder inputs
        dec_emb_layer = my_model.get_layer("embedding_1")  # Use the decoder embedding layer from the trained model
        dec_emb = dec_emb_layer(decoder_inputs)

        # LSTM layer with attention mechanism
        decoder_lstm = my_model.get_layer("lstm_3")  # Access the decoder LSTM layer
        decoder_outputs, state_h, state_c = decoder_lstm(
            dec_emb, initial_state=[decoder_state_input_h, decoder_state_input_c]
        )

        # Attention layer
        attn_layer = my_model.get_layer('scaled_dot_product_attention')
        attn_out, attn_weights = attn_layer([encoder_output_input, decoder_outputs])

        # Concatenate attention output and LSTM output
        decoder_concat_input = Concatenate(axis=-1)([decoder_outputs, attn_out])

        # Dense layer for generating the final prediction
        decoder_dense = my_model.get_layer("time_distributed")
        decoder_outputs = decoder_dense(decoder_concat_input)

        # Define the decoder model
        self.decoder_model = Model(
            inputs=[decoder_inputs, encoder_output_input, decoder_state_input_h, decoder_state_input_c],
            outputs=[decoder_outputs, state_h, state_c]
        )

    def predict(self, target_seq, e_out, e_h, e_c):
        return self.decoder_model.predict([target_seq] + [e_out, e_h, e_c], verbose=0)
