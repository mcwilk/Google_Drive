def uploadFile(file, name, folder_id, drive):
    """
        Function to upload file for the first time
    """

    new_file = drive.CreateFile({"title": name,
                    "parents": [{"kind": "drive#fileLink", "id": folder_id}]})
    new_file.SetContentFile(file)
    new_file.Upload()
    print(f"File '{name}' has been uploaded for the first time.")
