
# Google Keep Transfer

A Python script based on [gkeepapi](https://github.com/kiwiz/gkeepapi) for transferring Google Keep notes from one account to another.




## Setup

1. To run this script, your Google Keep Notes must first be download via Google Takeout. To dowload your keep notes:
    * Visit https://takeout.google.com/settings/takeout. **Be sure you have the right account selected (click avatar in the upper right of the page to change accounts)**
    * Select the checkbox for Google Keep.
    * Scroll to the bottom of the page and click "Next step". Choose ".zip" for file type, then click "Create export". When your export is complete, download the zip and extract its contents to a directory. When this is done, please rerun this script.
2. If your account uses two-factor authentication, first create an app Password and use that password here. To create an app password, follow the instructions at https://support.google.com/accounts/answer/185833?hl=en
## Installation & Running

1. Download/clone this repo
2. `cd` to repo directory in terminal
3. (optional) create virtual env
4.  Install dependencies
```bash
pip install -r requirements.txt
```
5. Run main.py from command line, follow prompts
```bash
  python main.py
```
