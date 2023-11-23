import json
import os

directory_path = './plane_dataset'


for subdir in next(os.walk(directory_path))[1]:
        subdir_path = os.path.join(directory_path, subdir)
        
        for file in os.listdir(subdir_path):
            if file.endswith('.json'):
                json_file_path = os.path.join(subdir_path, file)
                
                with open(json_file_path, 'r') as json_file:
                    data = json.load(json_file)
                
                for frame in data["frames"]:
                    frame["file_path"] = frame["file_path"].replace("train/", "images/")
                
                with open(json_file_path, 'w') as json_file:
                    json.dump(data, json_file, indent=4)