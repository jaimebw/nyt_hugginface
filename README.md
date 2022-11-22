# Repo for uploading NYT articles Kaggle dataset to the hugginface repo

The code in this repo is for automatically uploading the latest code base to the [HugginFace repository](https://huggingface.co/datasets/jaimebw/nyt_dataset).
Hopefully, this won't be touched anymore

## What has been doen to the dataset?
The [original data](https://www.kaggle.com/datasets/brendanmiles/nyt-news-dataset-20082021) had not been cleaned from abstracts/title that were incomplete nor repeated abstracts/titles. 
Also, the original dataset has the "keyword" column not well formatted into a list.

I have formated everything for making it almost ready to use in NLP. You may need to filter the dataset a bit more, or maybe tokenize, etc... But that's on you ;) 

And I changed the format from .csv to .json .


