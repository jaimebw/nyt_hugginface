import os
from huggingface_hub import HfApi


if __name__ == "__main__":
    token = os.environ["HUGGINGFACE_TOKEN"]
    api = HfApi(
        token=token
    )
    api.upload_file(
        path_or_fileobj="NYT_Dataset.csv",
        path_in_repo="NYT_Dataset.csv",
        repo_id="jaimebw/nyt_dataset",
        repo_type="dataset",
    )
