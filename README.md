# Python Twitter Tweet Deleter Script
This project contains a Python script for deleting tweets from a Twitter account using the Tweepy library.

## Requirements
To use this script, you must have the following installed:
* Python 3
* Tweepy library
* Twitter API authentication details (consumer key, consumer secret, access token key, and access token secret)

## Installation
If you don't have the Tweepy library installed, you can install it using pip:
```
pip install tweepy
```

## Usage
To use the script, follow these steps:
1. Clone this repository or download the script file.
2. Replace the Twitter API authentication details in the script with your own details.
3. Save the tweet IDs you want to delete in separate JSON files with the format as follows:
```
[    {        "tweet": {            "id": "<tweet_id>"        }    },    ...]

```

4. Update the files list in the script with the names of the JSON files containing the tweet IDs.
5. Run the script using the command:
```
python tweet_deleter.py
```
The script will loop through each tweet ID in the JSON files and attempt to delete the corresponding tweet. The script will display the deletion status for each tweet.

## Functions
The script includes the following functions:
* `show_authorization_status()`: Displays the current status of Twitter API authorization.
* `install_missing_libraries()`: Checks if the required libraries are installed and installs them if they are missing.

## Author
This script was written by Isrg Rajan.
