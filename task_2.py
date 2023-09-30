'''
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
-Для дочерних объектов указывайте родительскую директорию.
-Для каждого объекта укажите файл это или директория. 
-Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
'''

import os
import json
import csv
import pickle


def get_dir_size(dir_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)

    return total_size


def save_dir_contents(dir_path, output_dir):
    results = []

    def process_dir(directory):
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            item_type = "file" if os.path.isfile(item_path) else "directory"

            if item_type == "file":
                item_size = os.path.getsize(item_path)

            else:
                item_size = get_dir_size(item_size)

            results.append({
                "name": item,
                "path": item_path,
                "type": item_type,
                "parents_directory": directory
            })

            if os.path.isdir(item_path):
                process_dir(item_path)

        process_dir(dir_path)

    # Сохраняем результаты в JSON

    json_file_path = os.path.join(output_dir, "dir_contents.json")

    with open(json_file_path, 'w') as json_file:
        json.dump(results, json_file, indent=4)

    # Сохраняем результаты в CSV

    csv_file_path = os.path.join(output_dir, "dir_contents.csv")

    with open(csv_file_path, 'w', newline='') as csv_file:
        fieldnames = ['name', 'path', 'type', 'parent_directory']

        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(results)

    # Сохраняем результаты в Pickle

    pickle_file_path = os.path.join(output_dir, "dir_content.pkl")

    with open(pickle_file_path, 'wb') as pickle_file:
        pickle.dump(results, pickle_file)


if __name__ == "__main__":
    input_dir = "/python_homework_8"
    output_dir = "/8"

    save_dir_contents(input_dir, output_dir)
