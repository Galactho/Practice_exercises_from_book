
#! python
#! Project: Multi Clipboard Automatic Messages

import sys  # import sys to use argv wich reads terminal
import pyperclip    # import pyperclip to acces the clipboard

# dictionary with values to copy on clipboard depends the keyphrase
text = {'agree':'Yes, I agree. That sounds great to me.',
        'busy':'Sorry, can we do this later this week or next week?',
        'upsell':'Would you consider making this a monthly donation?'}

# reads if a command have introduced in terminal
if len(sys.argv) < 2:
    print('Usage_: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

# variable keyphrase is readed from terminal
keyphrase = sys.argv[1] # firdt command line arg is the keyphrase

# if the phrase writed appears in dictionary, will copy to clipboard
if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print(f'Text for {keyphrase} copied to clipboard.')
else:
    print(f'There is no text for {keyphrase}')