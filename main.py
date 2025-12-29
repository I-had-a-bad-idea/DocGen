from code_structure_extractor import code_structure_of_file
import sys
import os
from markdown_generator import generate_markdown
from tqdm import tqdm
import asyncio

async def generate_docs_for_file(file_path):
    if not os.path.isfile(file_path):
        print("Not a file")
        return
    
    symbols = code_structure_of_file(file_path)
    if symbols:
        await generate_markdown(file_path, code_structure_of_file(file_path))


async def generate_docs_for_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Not a folder")
        return
    
    elements = os.listdir(folder_path)
    
    for element in tqdm(elements, desc=f"Processing {folder_path}", unit="item"):
        element_path = os.path.join(folder_path, element)

        if os.path.isfile(element_path):
            await generate_docs_for_file(element_path)
        elif os.path.isdir(element_path):
            await generate_docs_for_folder(element_path)


async def generate_docs_for_path(path):
    if os.path.isdir(path):
        await generate_docs_for_folder(path)
    elif os.path.isfile(path):
        await generate_docs_for_file(path)

def main():
    if len(sys.argv) >= 2:
        path = sys.argv[1]
        asyncio.run(generate_docs_for_path(path))
    else:
        print("Usage: python main.py path_to_folder")


if __name__ == "__main__":
    main()