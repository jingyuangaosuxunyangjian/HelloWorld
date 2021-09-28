import paddle
from paddle.nn import Linear
import paddle.nn.functional as F
import os
import numpy as np

train_dataset = paddle.vision.datasets.MNIST(mode = 'train')