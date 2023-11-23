import os

main_directory = "./plane_dataset"

for i in range(31, 41):
    j = f'0{i}' if i < 10 else i
    train_dir_path = os.path.join(main_directory, f'plane{j}', 'train')
    
    if os.path.exists(train_dir_path) and os.path.isdir(train_dir_path):
        os.rename(train_dir_path, os.path.join(main_directory, f'plane{j}', 'images'))