import argparse

from model import SimpleCNN
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader

from pytorch_lightning import Trainer
from pytorch_lightning.callbacks import ModelCheckpoint, LearningRateMonitor
from pytorch_lightning.loggers import TensorBoardLogger

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--version', '-v')

    args = parser.parse_args()

    train_dataset = MNIST(root='.', train=True, download=True, transform=ToTensor())
    train_dataloader = DataLoader(train_dataset,
                                  batch_size=120,
                                  num_workers=6,
                                  shuffle=True)

    val_dataset = MNIST(root='.', train=False, download=True, transform=ToTensor())
    val_dataloader = DataLoader(val_dataset,
                                batch_size=120,
                                num_workers=6,
                                shuffle=False)

    model = SimpleCNN()

    logger = TensorBoardLogger('.', version=args.version)
    model_ckpt = ModelCheckpoint(dirpath=f'lightning_logs/{args.version}/checkpoints',
                                 save_top_k=2,
                                 monitor='accuracy_val',
                                 mode='max')
    lr_monitor = LearningRateMonitor()

    trainer = Trainer(accelerator='gpu',
                      devices=1,
                      max_epochs=150,
                      val_check_interval=500,
                      callbacks=[model_ckpt, lr_monitor],
                      logger=logger)
    trainer.fit(model, train_dataloader, val_dataloader)
