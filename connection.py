from pydrive.auth import GoogleAuth


def gDriveConnection():
    """
        Function to connect with Google Drive
    """
    
    # Connecting and authorizing on Google Drive
    gauth = GoogleAuth()

    # Loading saved credentials to automate permission process
    gauth.LoadCredentialsFile("mycredentials.txt")

    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()

    # saving credentials for each session
    gauth.SaveCredentialsFile("mycredentials.txt")

    return gauth
