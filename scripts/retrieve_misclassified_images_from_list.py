import shutil
import os
from pathlib import Path

def move_misclassified_images(file_list, source_dir, target_dir):
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    
    # Validation: Ensure source exists
    if not source_path.exists():
        print(f"[!] Error: Source directory '{source_dir}' does not exist.")
        return

    # Ensure target directory exists
    target_path.mkdir(parents=True, exist_ok=True)
    
    found_count = 0
    
    # Process the list
    for filename in file_list:
        filename = filename.strip()
        if not filename:
            continue
            
        # Recursive search only within the specified source folder
        # rglob is case-sensitive on some systems; use glob if needed
        matches = list(source_path.rglob(filename))
        
        if not matches:
            print(f"[-] Not found: {filename}")
            continue
            
        for match in matches:
            # Prevent moving if already in target
            if match.parent.resolve() == target_path.resolve():
                print(f"[.] Already in target: {match.name}")
                continue
                
            try:
                # Use shutil.copy2 to preserve metadata (timestamps, etc.)
                # Change to shutil.move if you want to remove from source
                shutil.copy2(str(match), str(target_path / match.name))
                print(f"[+] Successfully copied: {match.name} from {match.parent.name}")
                found_count += 1
            except Exception as e:
                print(f"[!] Error processing {match.name}: {e}")

    print(f"\nOperation complete. Total unique files processed: {found_count}")

if __name__ == "__main__":
    # CONFIGURATION
    LIST_FILE = "misclassified_images_list.txt"      # Your line-separated text file
    IMAGE_SOURCE = "/Users/admin/Developer/ensf_617/garbage_data"   # THE FOLDER TO SEARCH IN
    DESTINATION = "../assets/misclassified_images"
    
    try:
        with open(LIST_FILE, "r") as f:
            images_to_move = [line.strip() for line in f if line.strip()]
            
        move_misclassified_images(images_to_move, IMAGE_SOURCE, DESTINATION)
    except FileNotFoundError:
        print(f"Error: The list file '{LIST_FILE}' was not found.")