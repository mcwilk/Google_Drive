def updateFile(file, name, drive_file):
    """
        Function to update existing file if it was modified within indicated
        time preriod
    """
       
    drive_file.SetContentFile(file)
    drive_file.Upload()
    print(f"File '{name}' modified within last 12 hours: updated.")
