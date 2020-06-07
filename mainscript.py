import os
import time
import datetime
from connection import gDriveConnection
from upload import uploadFile
from update import updateFile
from pydrive.drive import GoogleDrive


# Google Drive destination directory ID
drive_dir_id = "1SazGz1SPWhEl40OtiOmu-G7ibsFnkiKY"

# Files to upload/update
files = {'path1': r"/home/mcwilk/Pulpit/excel_file.xlsx",
         'path2': r"/home/mcwilk/Pulpit/word_file.docx",
         'path3': r"/home/mcwilk/pdf_file.pdf"}

# Variables to verify modification time of files to upload/update
now = time.time()
delta = datetime.timedelta(hours=12)

# Variable for file names in destination directory
titles = []


if __name__ == '__main__':

    gauth = gDriveConnection()

    # Google Drive object
    drive = GoogleDrive(gauth)
    
    # List of files in destination directory
    drive_dir_files = drive.ListFile(
        {'q': f"'{drive_dir_id}' in parents and trashed=false"}).GetList()

    for d_file in drive_dir_files:
        titles.append(d_file['title'])

    # main logic for file upload/update
    if len(drive_dir_files) >= 1:

        for path in files.values():
            filename = os.path.basename(path)
            modif_time = os.path.getmtime(path)
            diff = modif_time + delta.seconds

            for d_file in drive_dir_files:

                if filename in titles:

                    if filename == d_file['title']:

                        if diff >= now:
                            updateFile(path, filename, d_file)
                            break
                        else:
                            print(f"File '{filename}' exists but NOT updated.")
                            break

                else:
                    uploadFile(path, filename, drive_dir_id, drive)
                    break
                
    else:
        
        for path in files.values():
            filename = os.path.basename(path)
            uploadFile(path, filename, drive_dir_id, drive)

