import albumentations as A
import random
from tqdm import tqdm
from .utils import get_filters
import os
import shutil
from .utils import read_video, write_video
import warnings
warnings.filterwarnings("ignore")


class Augment:
    def __init__(self, data_dir, dst_path):
        self.data_dir = data_dir
        self.dst_path = dst_path


    def augment(self, quantity, resize=True, width=0, height=0):

        filters = get_filters()

        if resize:
            filters.insert(0, A.Resize(width=width, height=height, p=1))

        classes = os.listdir(self.data_dir)

        try:
            os.makedirs(self.dst_path)
        except:
            shutil.rmtree(self.dst_path)
            os.makedirs(self.dst_path)


        for clas in tqdm(classes):

            try:
                os.makedirs(os.path.join(self.dst_path, clas))
            except:
                shutil.rmtree(os.path.join(self.dst_path, clas))
                os.makedirs(os.path.join(self.dst_path, clas))

            class_path = os.path.join(self.data_dir, clas)
            videos = os.listdir(class_path)
            videos_path = [os.path.join(class_path, vid) for vid in videos]


            for vid_path in tqdm(videos_path, desc='Augmenting Video'):
                file_count = 0
                for _ in range(quantity):
                    frames, fps = read_video(vid_path)
                    random.seed(random.randint(0, 999999))
                    video_frames_length = len(frames)
                    additional_targets = {}

                    for num in range(video_frames_length-1):
                        additional_targets[f'image{num}'] = 'image'

                    aug = A.Compose(filters, additional_targets=additional_targets)

                    frames_dict = {f'image{num}': frame for num, frame in enumerate(frames[1:])}
                    frames_dict['image'] = frames[0]
                    augmented = aug(**frames_dict)
                    augmented_frames = []
                    augmented_frames.append(augmented['image'])
                    for num in range(video_frames_length-1):
                        augmented_frames.append(augmented[f'image{num}'])

                    vid_name = os.path.basename(vid_path)
                    vid_name = vid_name.split('.')[0]
                    vid_name = f'{vid_name}_{file_count}.mp4'
                    write_video(os.path.join(self.dst_path, clas, vid_name), augmented_frames, fps)
                    file_count += 1

if __name__ == '__main__':
    augment = Augment('/home/seyed/Downloads/All Dataset each class', '/home/seyed/Downloads/augment')
    augment.augment(10, resize=True, width=224, height=224)