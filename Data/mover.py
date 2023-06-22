import os
import shutil


def move_jpeg_files(source_folder):
    # Get a list of all JPEG files in the source folder
    jpeg_files = [file for file in os.listdir(source_folder) if file.lower().endswith(".jpg")]

    # Create a destination folder for each file and move the file
    for index, jpeg_file in enumerate(jpeg_files, start=1):
        destination_folder = "C:\\Users\\User\\PycharmProjects\\Face_Recognition_w_DeepFace\\Data\\Person" + str(index+88)
        destination_path = os.path.join(source_folder, destination_folder)

        # Create the destination folder if it doesn't exist
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        # Move the JPEG file to the destination folder
        shutil.move(os.path.join(source_folder, jpeg_file), destination_path)

    print("Files moved successfully.")


move_jpeg_files('C:\\Users\\User\\PycharmProjects\\Face_Recognition_w_DeepFace\\Data\\people')
