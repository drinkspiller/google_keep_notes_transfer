from colorama import Fore, Style
from PyInquirer import style_from_dict
from prompt_toolkit.token import Token

CUSTOM_PROMPT_STYLE = style_from_dict({
    Token.Separator: '#6C6C6C',
    Token.QuestionMark: '#FF9D00 bold',
    Token.Selected: '#2196f3',
    Token.Pointer: '#FF9D00 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '#FFD591',
})
Messages = {
  'ATTACHMENT_NOTICE': (Fore.YELLOW + 'NOTE: attachments are unsupported by ' +
    'gkeepapi. Notes with attachments will be logged to stdout so you can ' +
    'manually reattach using the attachment files (in the Takeout/Keep ' +
    'folder).' + Style.RESET_ALL),
  'ATTACHMENT_TEMPLATE': (Fore.YELLOW + '* note with title `{0}` has the following ' +
    'attachments: \n {1}' + Style.RESET_ALL),
  'COMPLETE': (Fore.LIGHTGREEN_EX + 'Script execution complete' +
    Style.RESET_ALL),
  'DOWNLOAD_NOTES_VIA_TAKEOUT': (Fore.LIGHTGREEN_EX + 'To run this script, ' +
    'your Google Keep Notes must first be download via Google Takeout. To ' +
    'download your keep notes: \n1. Visit ' +
    'https://takeout.google.com/settings/takeout.\n' + Style.BRIGHT + Fore.RED +
    '   Be sure you have the right account selected (click avatar \n   in ' +
    'the upper right of the page to change accounts)' + Style.NORMAL +
    Fore.LIGHTGREEN_EX + '\n2. Select the checkbox for Google Keep. \n3. ' +
    'Scroll to the bottom of the page and click "Next step". Choose ".zip" ' +
    'for file type, then click "Create export". When your export is ' +
    'complete, download the zip and extract its contents to a directory. ' +
    'When this is done, please rerun this script.' + Style.RESET_ALL
    ),
  'LOGIN_SUCCESS': (Fore.LIGHTGREEN_EX + 'Account login was successfull.'
    + Style.RESET_ALL),
  'LOGIN_FAILURE_TEMPLATE': (Fore.RED + 'An exception occurred while ' +
    'logging in: {exception}' + Style.RESET_ALL),
  'START': Fore.LIGHTGREEN_EX + 'Processing notes...' + Style.RESET_ALL,
  'SYNC': Fore.LIGHTGREEN_EX + 'Syncing notes to {0}' + Style.RESET_ALL,
  'SYNC_FAILURE_TEMPLATE': (Fore.RED + 'sAn exception occurred while ' +
    'syncing: {exception}' + Style.RESET_ALL),
}
