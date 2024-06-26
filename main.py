import datetime

import torch
import os

from pathlib import Path

from utils.dataset import IMDBBertDataset
from utils.model_architecture import BERT
from utils.model_trainer import BertTrainer

BASE_DIR = Path(__file__).resolve().parent

EMB_SIZE = 64
HIDDEN_SIZE = 36
EPOCHS = 4
BATCH_SIZE = 12
NUM_HEADS = 4

CHECKPOINT_DIR = BASE_DIR.joinpath('data/bert_checkpoints')
if not os.path.exists(CHECKPOINT_DIR):
    os.makedirs(CHECKPOINT_DIR)

timestamp = datetime.datetime.utcnow().timestamp()
LOG_DIR = BASE_DIR.joinpath(f'data/logs/bert_experiment_{timestamp}')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

if torch.cuda.is_available():
    torch.cuda.empty_cache()

if __name__ == '__main__':
    print("Prepare dataset")
    ds = IMDBBertDataset(BASE_DIR.joinpath('data/imdb.csv'), ds_from=0, ds_to=1000)
    print("Dataset Prepared")

    bert = BERT(len(ds.vocab), EMB_SIZE, HIDDEN_SIZE, NUM_HEADS).to(device)
    trainer = BertTrainer(
        model=bert,
        dataset=ds,
        log_dir=LOG_DIR,
        checkpoint_dir=CHECKPOINT_DIR,
        print_progress_every=20,
        print_accuracy_every=200,
        batch_size=BATCH_SIZE,
        learning_rate=0.00007,
        epochs=35000
    )

    trainer.print_summary()
    trainer()