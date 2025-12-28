from code_structure_extractor import code_structure_of_file
import sys
import os
from markdown_generator import generate_markdown
from tqdm import tqdm
import asyncio

async def generate_docs_for_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Not a folder")
        return
    
    elements = os.listdir(folder_path)
    
    for element in tqdm(elements, desc=f"Processing {folder_path}", unit="item"):
        element_path = os.path.join(folder_path, element)


        if os.path.isfile(element_path):
            symbols = code_structure_of_file(element_path)
            if symbols:
                await generate_markdown(element_path, code_structure_of_file(element_path))

        elif os.path.isdir(element_path):
            await generate_docs_for_folder(element_path)

def main():
    if len(sys.argv) >= 2:
        folder_path = sys.argv[1]
        asyncio.run(generate_docs_for_folder(folder_path))
    else:
        print("Usage: python main.py path_to_folder")


if __name__ == "__main__":
    main()