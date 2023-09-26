# Calculate the difference between location and quaternion
import os
import json
import numpy as np

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def quaternion_angle_difference(quat1, quat2):
    quat1 = quat1 / np.linalg.norm(quat1)
    quat2 = quat2 / np.linalg.norm(quat2)
    dot_product = np.dot(quat1, quat2)
    # Ensure values are within valid domain for arccos (-1 to 1)
    # dot_product = np.clip(dot_product, -1.0, 1.0)
    angle_rad = 2 * np.arccos(np.abs(dot_product))
    return np.degrees(angle_rad), quat1, quat2  # Convert to degrees

def compute_difference(dir1, dir2):
    files = [f for f in os.listdir(dir1) if f.endswith('.json')]

    for file in files:
        file_path1 = os.path.join(dir1, file)
        file_path2 = os.path.join(dir2, file)

        if os.path.exists(file_path1) and os.path.exists(file_path2):
            data1 = load_json(file_path1)
            data2 = load_json(file_path2)

            for obj1, obj2 in zip(data1['objects'], data2['objects']):
                loc1 = np.array(obj1['location_worldframe'])
                ltw = np.array(obj1['local_to_world_matrix'])
                loc2 = np.array(obj2['location'])
                dloc = np.dot(ltw.reshape(4,4).T, np.append(loc2, 1)[:, np.newaxis])[:3].ravel()
                loc_difference = np.linalg.norm(loc1 - dloc)
                # print(dloc,loc1,loc2)
                print(f"'location' difference for {file} ({obj1['class']}): {loc_difference}")

                quat1 = np.array(obj1['quaternion_xyzw'])
                quat2 = np.array(obj2['quaternion_xyzw'])
                quat_angle_difference, q1, q2 = quaternion_angle_difference(quat1, quat2)
                # print(q1, q2)
                print(f"'quaternion_xyzw' angle difference for {file} ({obj1['class']}): {quat_angle_difference} degrees")
        else:
            print(f"{file} does not exist in one of the directories.")

if __name__ == "__main__":
    # dir1 = input("Enter the path to the first directory: ")
    # dir2 = input("Enter the path to the second directory: ")
    dir1 = "D:\\Desktop\\1\\individual_project\\Deep_Object_Pose_Windows\\output\\dataset\\000\\"
    dir2 = "D:\\Desktop\\1\\individual_project\\Deep_Object_Pose_Windows\\out_experiment\\"

    compute_difference(dir1, dir2)

