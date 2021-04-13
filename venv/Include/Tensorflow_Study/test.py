import pydot
import tensorflow
if __name__ == '__main__':
    tf.keras.utils.plot_model(model, "my_first_model_with_shape_info.png", show_shapes=True)
