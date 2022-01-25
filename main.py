#!/usr/bin/python

import colorama
import gkeepapi
from gkeepapi.exception import LoginException, SyncException
from gkeepapi.node import ColorValue
import glob
import json
from constants import CUSTOM_PROMPT_STYLE, Messages
from PyInquirer import prompt

colorama.init()



# Check if Notes being transferred have been downloaded.
files_downloaded_via_takeout = prompt([
    {
        'type': 'list',
        'name': 'answer',
        'message': ('Have you already downloaded the Keep notes you wish to ' +
          'transfer via Google Takeout?'),
        'choices': [
            'No',
            'Yes',
        ]
    }
], style=CUSTOM_PROMPT_STYLE)

if files_downloaded_via_takeout['answer'] == 'No':
  print(Messages['DOWNLOAD_NOTES_VIA_TAKEOUT'])
  exit()
else:
  keep_notes_dir = prompt([
    {
        'type': 'input',
        'name': 'answer',
        'message': ('What is the path to the directory where the Keep files ' +
                    'are stored (e.g. ./Takeout/Keep/) Include the trailing ' +
                    'slash for the directory.'),
    }
], style=CUSTOM_PROMPT_STYLE)

# Log in to account notes are being transferred to.
keep = gkeepapi.Keep()
login = prompt([
    {
        'type': 'input',
        'name': 'answer',
        'message': ('Enter the email address for the account you want to ' +
                    'transfer the downloaded Keep notes to. ' +
                    '(e.g. example@gmail.com)'),
    }
], style=CUSTOM_PROMPT_STYLE)

password = prompt([
    {
        'type': 'password',
        'name': 'answer',
        'message': ('Enter the password for that account. Password is NOT ' +
                    'saved. NOTE: If your account uses\n  two-factor ' +
                    'authentication, first create an app Password and use ' +
                    'that password here. To \n  create an app password, ' +
                    'follow the instructions at ' +
                    'https://support.google.com/accounts/answer/185833?hl=en'),
    }
], style=CUSTOM_PROMPT_STYLE)
try:
    login = login['answer']
    password = password['answer']
    keep.login(login, password)
    print(Messages['LOGIN_SUCCESS'])
except LoginException as exception:
    print(Messages['LOGIN_FAILURE_TEMPLATE'].format(exception.args[0]))

note_json_files = glob.glob(keep_notes_dir['answer'] + '*.json')

print(Messages['START'])
print(Messages['ATTACHMENT_NOTICE'])

# Get a list of all notes from Takeout export.
for note_json_file in note_json_files:
    with open(note_json_file, 'r') as note_data:
        note = json.load(note_data)

        # Create a new text or checklist note.
        if note.get('listContent'):
            checklist = map(lambda item: (
                item['text'], item['isChecked']), note.get('listContent'))
            new_note = keep.createList(note.get('title'), checklist)
        else:
            new_note = keep.createNote(
                note.get('title'), note.get('textContent'))

        # Add properties from downloaded note to new note.
        if note.get('color') and note.get('color') != 'DEFAULT':
            new_note.color = ColorValue[note.get('color').title()]
        if note.get('isPinned'):
            new_note.pinned = True
        if note.get('isArchived'):
            new_note.archived = True
        if note.get('attachments'):
            print(Messages['ATTACHMENT_TEMPLATE'].format(
                new_note.title,
                '\t' + ', '.join(list(map(
                  lambda attachment: attachment['filePath'],
                  note.get('attachments'))))))
        if note.get('isTrashed'):
            new_note.trash()

# Sync all notes.
try:
  print(Messages['SYNC'].format(login))
  keep.sync()
except SyncException:
  print(Messages['SYNC_FAILURE_TEMPLATE'].format(exception.args[0]))

print(Messages['COMPLETE'])
