from os import path
from read import create_knowledge_base_file, list_case_files, print_link_in_file, print_title_in_file
import frontmatter

path = "knowledge-base/"
filename = "knowledge-base.md"

files = list_case_files()
tagsDict = {}
knowledge_base_path_file = create_knowledge_base_file()
for file in files:
    page = frontmatter.load(path + file)
    url = "[" + page['title'] + "](" + path + file + ")"
    for tag in page['tags']:
        if tag in tagsDict:
            tagsDict[tag].append(url)
        else:
            tagsDict[tag] = [url]

for tag in tagsDict:
    print_title_in_file(knowledge_base_path_file, tag + "\n")
    for url in tagsDict[tag]:
        print_link_in_file(knowledge_base_path_file, "- " + url)

