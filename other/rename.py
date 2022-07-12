#!/usr/bin/env python3

import os


def recursivly_walk_through_folder(path: str) -> None:
    if path is None:
        return
    path = path.strip()
    if path.startswith("."):
        return
    for cur_folder_name, sub_folders, file_names in os.walk(path):
        print(f"Current folder path: {cur_folder_name}")

        for folder in sub_folders:
            recursivly_walk_through_folder(folder)

        for file in file_names:
            if file.endswith(".py"):
                src_file_name = os.sep.join([cur_folder_name, file])
                dest_file_name = os.sep.join([cur_folder_name, lower_file_name(file)])
                try:
                    print(f"{src_file_name} -> {dest_file_name}")
                    os.rename(src_file_name, dest_file_name)
                except Exception as e:
                    print(e)


def lower_file_name(file_name: str) -> str:
    if file_name is None:
        return
    return file_name.lower()


if __name__ == "__main__":
    recursivly_walk_through_folder(os.getcwd())

    input("Please press any key to stop!")
