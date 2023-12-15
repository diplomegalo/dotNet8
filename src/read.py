import os

def get_case_path_files(path="/knowledge-base/case/"):
    files = []
    path = os.getcwd() + path
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        if os.path.isfile(filepath):
            files.append(path + filename)
    if len(files) == 0:
        print("No files found in " + path)
        exit(1)
    return files

def create_knowledge_base_file(path="/knowledge-base/knowledge-base.md"):
    file_path = os.getcwd() + path
    
    # Check if the file already exists
    if os.path.exists(file_path):
        # If it exists, delete the file
        os.remove(file_path)
        
    # Create an empty file
    with open(file_path, 'w') as file:
        file.write("# Knowledge Base\n\n")
    file.close()
    return file_path

import urllib.parse

def print_line_in_file(file_path, tag):
    encoded_tag = urllib.parse.quote(tag)
    with open(file_path, 'a') as file:
        file.write(f"- [{tag}](#{encoded_tag})\n")

def print_title_in_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write("\n## " + text + "\n")
        file.write("| Titre | Description |\n")
        file.write("|--|--|\n")

def print_row_in_file(file_path, row):
    with open(file_path, 'a') as file:
        file.write("| " + row['url'] + " | " + row['description'] + " |\n")
