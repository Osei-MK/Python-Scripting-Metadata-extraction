'''
wk-7 solution solved
'''
import os
import zipfile 
from PIL import Image 
from prettytable import PrettyTable 

print("\nOsei-Mensah-WK7 Script\n")

#extract 
zip_path = 'photos.zip'
extract_folder  = 'extracted_photos'

if not os.path.exists(extract_folder):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"[+] Extracted '{zip_path}' to '{extract_folder}'")
else:
    print(f"[!] Folder.'{extract_folder}' already exists. Skipping extraction.")
    
#prettytable
table = PrettyTable()
table.field_names = ["Path", "Extension", "Format", "Width", "Height", "Mode"] 

for root, dirs, files in os.walk(extract_folder):
    for file in files:
        full_path = os.path.join(root, file)
        ext = os.path.splitext(file)[1]
        try: 
            with Image.open(full_path) as im:
                table.add_row([
                    full_path, 
                    ext, 
                    im.format, 
                    im.width, 
                    im.mode, 
                    im.height,
                    
                ])
        except Exception as e: 
            print(f"[x] Skipping non-image file: {file}")
            
#display results 
print("\nImage File Report:\n")
print(table) 

print("\nScript Done")
    