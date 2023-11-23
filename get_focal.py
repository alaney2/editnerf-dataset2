import math
import json


for i in range(31, 41):
    if i < 10:
        j = f'0{i}'
    else:
      j = i
    path = f'./plane_dataset/plane{j}'

    with open(f'{path}/transforms_train.json', 'r') as file:
        parsed_data = json.load(file)

    camera_angle_x_radians = parsed_data["camera_angle_x"]
    camera_angle_y_radians = parsed_data["camera_angle_y"]
    image_width_pixels = parsed_data["w"]
    image_height_pixels = parsed_data["h"]

    f_x_pixels = image_width_pixels / (2 * math.tan(camera_angle_x_radians / 2))
    f_y_pixels = image_height_pixels / (2 * math.tan(camera_angle_y_radians / 2))

    focal_length = (f_x_pixels / image_width_pixels + f_y_pixels / image_height_pixels) / 2

    # print(f"Computed focal length: {focal_length}")

    frames_data = parsed_data['frames']

    new_data = {'focal': focal_length, 'frames': frames_data}

    with open(f'{path}/transforms_train.json', 'w') as file:
        json.dump(new_data, file, indent=4)