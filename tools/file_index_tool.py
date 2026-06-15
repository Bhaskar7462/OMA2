from tools.file_scanner_tool import scan_home_directory

print("Building file index...")
FILE_INDEX = scan_home_directory()
print(f"Indexed {len(FILE_INDEX)} files and folders")

def get_file_index():
    return FILE_INDEX