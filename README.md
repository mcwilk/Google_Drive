# Google Drive upload

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Libraries](#libraries)
* [Status](#status)
* [Contact](#contact)

## General info
I prepared this Python script to automate boring task of uploading bunch of files on Google Drive after each modification. It connects to Google Drive using Google Drive API and PyDrive library, authorize an user and upload or update specified files from local drive. 


Step-by-step:
1. Connect to Google Drive using 'gDriveConnection' function;
2. Create an instance of Drive;
3. Create two lists: first for all files metadata from destination directory and second for their names (titles) only;
4. Main Logic:
Check whether destination directory contains any files (len >= 1):
- if yes: Update existing files (if modified within last 12 hours) with 'updateFile' function or upload for the first time (if do not exist on Drive) with 'uploadFile' function;
- if not: Upload files for the first time with 'uploadFile' function.


## Technologies
* Python 3.7.5
* Google Drive API

## Libraries
* Python: os, time, datetime, PyDrive

## Status
Project is: _finished_

## Contact
maciej.wilk04@gmail.com
