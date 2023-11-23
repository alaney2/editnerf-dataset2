import json
from random import shuffle

for i in range(31, 41):
    j = f'0{i}' if i < 10 else i
    
    path = f'./plane_dataset/plane{j}'

    with open(f'{path}/transforms_train.json', 'r') as file:
        full_data = json.load(file)

    frames = full_data['frames']
    shuffle(frames)

    train_frames = frames[:60]
    val_frames = frames[60:80]
    test_frames = frames[80:]

    train_frames_sorted = sorted(train_frames, key=lambda x: x['file_path'])
    val_frames_sorted = sorted(val_frames, key=lambda x: x['file_path'])
    test_frames_sorted = sorted(test_frames, key=lambda x: x['file_path'])


    with open(f'{path}/transforms_train.json', 'w') as file:
        json.dump({'focal': full_data['focal'], 'frames': train_frames_sorted}, file, indent=4)

    with open(f'{path}/transforms_val.json', 'w') as file:
        json.dump({'focal': full_data['focal'], 'frames': val_frames_sorted}, file, indent=4)

    with open(f'{path}/transforms_test.json', 'w') as file:
        json.dump({'focal': full_data['focal'], 'frames': test_frames_sorted}, file, indent=4)