from croc.train.train import train
import wandb
wandb.init(mode="offline")

if __name__ == "__main__":
    train()