import os
import shutil
from datetime import datetime
from collections import defaultdict


extensions = {
    'Text files': ["txt", "md", "csv", "log", "json"],
    'Document files': ["doc", "docx", "pdf", "rtf", "odt", "PDF"],
    'Spreadsheet files': ["xls", "xlsx", "ods", "csv"],
    'Presentation files': ["ppt", "pptx", "odp"],
    'Image files': ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "svg", "webp", "JPG", "PNG"],
    'Audio files': ["mp3", "wav", "ogg", "flac", "aac", "m4a"],
    'Video files': ["mp4", "mkv", "avi", "mov", "wmv", "flv", "webm", "MOV"],
    'Archive files': ["zip", "rar", "7z", "tar", "gz", "bz2", "xz", "evtx"],
    'Executable files': ["exe", "bat", "sh", "py", "pl", "jar", "app", "neek", "neex", "rel", "vbs"],
    'Web files': ["html", "htm", "css", "js", "php", "asp", "aspx", "jsp", "mhtml", "mht"],
    'Database files': ["db", "sql", "sqlite", "mdb", "accdb"],
    'System files': ["dll", "sys", "ini", "cfg", "reg"],
    'Font files': ["ttf", "otf", "woff", "woff2"],
    'Disk image files': ["iso", "img", "dmg"],
    '3D model files': ["obj", "fbx", "stl", "dae", "3ds"],
    'Code files': ["c", "cpp", "h", "hpp", "java", "js", "ts", "go", "rb", "rs", "swift", "kt", "dart"]
}

def checkOrganizer():
    organizer_folder = "C:/Users/Alphy/Desktop/Organizer/"
    if not os.path.exists(organizer_folder):
        os.mkdir(organizer_folder)

def get_files_in_desktop():
    downloads_folder = os.path.expanduser("C:/Users/Alphy/Desktop")
    files_info = []

    for file_name in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, file_name)
        if os.path.isfile(file_path):
            file_info = {
                'Name': file_name,
                'Path': file_path,
                'Size (Bytes)': os.path.getsize(file_path),
                'Creation Time': datetime.fromtimestamp(os.path.getctime(file_path)).strftime("%Y-%m-%d"),
                'Last Access Time': datetime.fromtimestamp(os.path.getatime(file_path)).strftime("%Y-%m-%d"),
                'Last Modification Time': datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y-%m-%d")
            }
            if ".lnk" not in file_info["Name"]:
                files_info.append(file_info)
    return files_info

def move_files(files):
    for file in files:
        if len(file["Name"]) > 1:
            extension = file["Name"].split(".")[-1]
            for ext in extensions:
                if extension in extensions[ext]:
                    check_folder = "C:/Users/Alphy/Desktop/Organizer/" + file["Creation Time"]
                    if not os.path.exists(check_folder):
                        os.mkdir(check_folder)
                    
                    check_type_folder =  "C:/Users/Alphy/Desktop/Organizer/" + file["Creation Time"] + "/" + ext
                    if not os.path.exists(check_type_folder):
                        os.mkdir(check_type_folder)
                    
                    check_ext_folder = "C:/Users/Alphy/Desktop/Organizer/" + file["Creation Time"] + "/" + ext + "/" + extension
                    if not os.path.exists(check_ext_folder):
                        os.mkdir(check_ext_folder)
                    
                    try:
                        #Moves the file to the correct folder
                        shutil.move(file["Path"], check_ext_folder + "/")
                    except:
                        print("Permission denied: Unable to move file")
                        print(file["Name"])
                        print()

checkOrganizer()
files = get_files_in_desktop()
move_files(files)
