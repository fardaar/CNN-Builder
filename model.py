import tensorflow as tf
import numpy as np

print("YO (☞ﾟヮﾟ)☞! Let's get your CNN up and running")

affirmative = ['true', 'TRUE', 'T', 't', 'True', '1', 'YES', 'Yes', 'yes']


def builder(instance, labels):
    print(
        "First you're gonna need to pass in your input shapes and number of classes\nif you don't know them just pass in a single instance of your training dataset and the entire labels")
    classes_num = len(set(labels))

    input_shape = instance.shape()
    # gonna use tensorflow's functional api
    layers = []
    input_layer = tf.keras.layers.Input(shape=input_shape)
    layers.append(input_layer)
    default = input("if you really know what your doing type False else just type True: ")

    if default in affirmative:
        default = True
    else:
        default = False

    layer_counter = 1
    build_layers = True
    if not default:
        while build_layers:
            layer_type = input("What kind of layer is this: (for now just type dense or convolution)")
            if layer_type in ['Conv', 'conv', 'Convolution', 'convolution']:
                print("*** Setting up layer {0} ***".format(layer_counter))
                num_units = int(input("Number of units for this layer: "))
                kernel_size = input("Kernel size for this layer:").split(',')
                kernel_size = tuple(int(x) for x in kernel_size)
                custom_padding = input("Do you need custom padding for this layer?")

                if custom_padding in affirmative:
                    padding = input("Padding is: ").split(',')
                    padding = tuple([int(x) for x in padding])
                else:
                    padding = input("same or valid padding: ")
                    if padding in ['SAME', 'same', 'Same']:
                        padding = 'SAME'
                    else:
                        padding = 'VALID'
                stride_size = int(input("What's the stride size? (Enter 0 for no stride)"))
                c = tf.keras.layers.Conv2D(filter=num_units, kernel_size=kernel_size, strides=stride_size,
                                           padding=padding)(layers[-1])
                layers.append(c)
                layer_counter += 1
