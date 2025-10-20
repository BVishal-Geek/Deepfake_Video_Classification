'''
Generates a csv file to point out the train, test and validation video files
'''
import os
import yaml
import random
import logging
import pandas as pd
from Deep_Fake_Video_Classification.utils.functions import load_params

params = load_params()

logging.basicConfig(
    level=logging.INFO,
    filename='Train_test_val_generator.log',
    format='%(asctime)s %(message)s',
    handlers=[
        logging.FileHandler('Train_test_val_generator.log'),
        logging.StreamHandler()
    ])

def train_test_val_generator(csv_name, **directory):
    '''
    Generates a  CSV with 2 columns consisting of video name and train, test, and val categorization.
    :return: CSV
    '''
    all_data = []

    try:
        for label, folder_path in directory.items():
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)


            total_video_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('mp4', '.avi', '.mov'))]
            random.shuffle(total_video_files)
            total_videos = len(total_video_files)
            train_end = int(params['split']['train']* total_videos)
            val_end = train_end + (int(params['split']['validation'] * total_videos))

            train_sample = total_video_files[:train_end]
            val_sample = total_video_files[train_end:val_end]
            test_sample = total_video_files[val_end:]

            for f in train_sample:
                all_data.append({"filename": f, "label": label, "split": "train"})
            for f in val_sample:
                all_data.append({"filename": f, "label": label, "split": "val"})
            for f in test_sample:
                all_data.append({"filename": f, "label": label, "split": "test"})

        df = pd.DataFrame.from_dict(all_data)
        df.to_csv(os.path.join(params['location']['home'], 'Train_test_val_split.csv'),index=False)
        logging.info(f"CSV created at {params['location']['home']}")

    except Exception as e:
        print(e)


train_test_val_generator('Train_test_val_split.csv',
real = params['location']['real'],
fake = params['location']['fake']
)