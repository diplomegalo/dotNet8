from os import path
from read import create_knowledge_base_file, get_case_path_files, print_row_in_file, print_title_in_file
import frontmatter

# Create the knowledge base file and get the path;
knowledge_base_path_file = create_knowledge_base_file()

# Get the list of files in the case directory;
cases_path_file = get_case_path_files()

# Init the tags dictionary;
tagsDict = {}

# For each file in the case directory;
for case_path_file in cases_path_file:
    
    # Get markdown page;
    page = frontmatter.load(case_path_file)

    # Build the url;
    url = "[" + page['title'] + "](" + case_path_file + ")"
    description = page['description']
    
    # Get the tags;
    tags = page['tags']

    for tag in tags:
        if tag in tagsDict:
            tagsDict[tag].append({"url": url, "description": description})
        else:
            tagsDict[tag] = [{"url": url, "description": description}]

# Sort the tagsDict based on key value;
tagsDict = dict(sorted(tagsDict.items()))

for tag in tagsDict:
    print_title_in_file(knowledge_base_path_file, tag + "\n")
    for item in tagsDict[tag]:
        print_row_in_file(knowledge_base_path_file, item)

