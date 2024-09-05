import os
import requests
from kaggle.api.kaggle_api_extended import KaggleApi
from datasets import load_dataset

def download_kaggle_dataset(dataset, download_path):
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset, path=download_path, unzip=True)

def download_huggingface_dataset(dataset_name, split, download_path):
    dataset = load_dataset(dataset_name, split=split)
    dataset.to_csv(os.path.join(download_path, f"{dataset_name}_{split}.csv"))

def main():
    # Download Kaggle datasets
    kaggle_datasets = {
        "mathematics": "mathurinache/math-dataset",
        "science": "thedevastator/sciq-a-dataset-for-science-question-answering",
        "history": "saketk511/world-important-events-ancient-to-modern"
    }
    for name, dataset in kaggle_datasets.items():
        download_kaggle_dataset(dataset, f"data/raw/{name}")
    
    # Download SQuAD dataset from Hugging Face
    download_huggingface_dataset("squad", "train", "data/raw/squad")
    download_huggingface_dataset("squad", "validation", "data/raw/squad")

if __name__ == "__main__":
    main()
