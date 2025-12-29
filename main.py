from code_structure_extractor import code_structure_of_file, get_language_name
import sys
import os
from markdown_generator import generate_markdown
from tqdm import tqdm
from tqdm.asyncio import tqdm_asyncio
import asyncio

queue = set()

async def generate_docs_for_file(file_path):
    if not os.path.isfile(file_path):
        print("Not a file")
        return

    symbols = code_structure_of_file(file_path)
    if symbols:
        await generate_markdown(file_path, symbols)


async def get_files_for_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Not a folder")
        return
    
    elements = os.listdir(folder_path)
    
    for element in tqdm(elements, desc=f"Getting files in {folder_path}", unit="item"):
        element_path = os.path.join(folder_path, element)

        if os.path.isfile(element_path):
            if get_language_name(element_path):
                queue.add(element_path)
        elif os.path.isdir(element_path):
            await get_files_for_folder(element_path)


async def get_files_for_path(path):
    if os.path.isdir(path):
        await get_files_for_folder(path)
    elif os.path.isfile(path):
        if get_language_name(path):
            queue.add(path)

async def generate_docs():
    tasks = [generate_docs_for_file(path) for path in queue]

    for task in tqdm_asyncio.as_completed(tasks, total=len(tasks), desc="Processing files", unit="chunk"):
        await task

def main():
    if len(sys.argv) >= 2:
        path = sys.argv[1]
        asyncio.run(get_files_for_path(path))
        asyncio.run(generate_docs())
        print("\n\nGenerated docs!")
    else:
        print("Usage: python main.py path_to_folder")


if __name__ == "__main__":
    main()