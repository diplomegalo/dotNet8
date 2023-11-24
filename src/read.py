import os

def list_case_files():
    files = []
    directory = os.getcwd() + "/knowledge-base/case/"
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            files.append(filename)
    if len(files) == 0:
        print("No files found in " + directory)
        exit(1)
    return files

def create_knowledge_base_file():
    file_path = os.getcwd() + "/knowledge-base/knowledge-base.md"
    
    # Check if the file already exists
    if os.path.exists(file_path):
        # If it exists, delete the file
        os.remove(file_path)
        
    # Create an empty file
    with open(file_path, 'w') as file:
        file.write("# Knowledge Base\n")
    file.close()
    return file_path;

def print_title_in_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write("\n## " + text + "\n")

def print_link_in_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text + "\n")