# QuestionAnsweringBERT
Implementing a question answering BERT model to understand the basics of BERT architecture
Things to note: Only one encoder is used to simplify the training process

## Dependencies (assuming windows): 
`pip install pylzma numpy ipykernel jupyter torch --index-url {Find you r right version of pytorch based on cuda and cudnn installed(use nvidia-smi to get the version) here: https://pytorch.org/}`

If you don't have an NVIDIA GPU, then the `device` parameter will default to `'cpu'` since `device = 'cuda' if torch.cuda.is_available() else 'cpu'`. If device is defaulting to `'cpu'` that is fine, you will just experience slower runtimes.

Tensorboard is also enabled and keeps track of training  loss and validation loss over the epochs> Make sure you the path to the runs is defined in gpt-v1.py
`tensorboard --logdir <place where you will have the logs>`

## Dataset.
Im currently using IMDB dataset of movie reviews for training: https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
Download the data and put it in data/ folder

## Visual Studio 2022 (for lzma compression algo) - https://visualstudio.microsoft.com/downloads/