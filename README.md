# simplecnn-mnist

Simple repository implementing the model $M_5$ of "An Ensemble of
Simple Convolutional Neural Network Models for MNIST
Digit Recognition", with PyTorch Lightning.

All credit to the authors of the paper,
Sanghyeon An, Minjun Lee, Sanglee Park, Heerin Yang, Jungmin So.

Link to paper: https://arxiv.org/abs/2008.10400.

To create the environment, run ``conda env create -f environment.yml``.

To track training, ``tensorboard --logdir lightning_logs``.

To launch training, ``python run_training.py -v version_name``.
