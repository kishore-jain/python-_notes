Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Qrcode
# emoji

import qrcode
url='https://www.cricbuzz.com'
rk = qrcode.make(url)
rk.save('cb_qrcode.png')

url='https://www.cricbuzz.com'

# png = portable network graphics
url='8248820464'
rk = qrcode.make(url)
rk.save('number_qrcode.png')


# Emoji module
# ------------

import emoji
dir(emoji)
['EMOJI_DATA', 'EmojiMatch', 'EmojiMatchZWJ', 'EmojiMatchZWJNonRGI', 'LANGUAGES', 'STATUS', 'Token', '__all__', '__author__', '__builtins__', '__cached__', '__doc__', '__email__', '__file__', '__license__', '__loader__', '__name__', '__package__', '__path__', '__source__', '__spec__', '__version__', 'analyze', 'config', 'core', 'demojize', 'distinct_emoji_list', 'emoji_count', 'emoji_list', 'emojize', 'get_aliases_unicode_dict', 'get_emoji_unicode_dict', 'is_emoji', 'purely_emoji', 'replace_emoji', 'tokenizer', 'unicode_codes', 'version']
>>> 
>>> print(emoji.emojize(':smiling_face:'))
☺️
>>> print('\uooo1f603')
SyntaxError: incomplete input
>>> print('\UOOO1f603')
SyntaxError: incomplete input
>>> print('\U0001f603')
😃
>>> print(emoji.demojize('😃'))
:grinning_face_with_big_eyes:
>>> print('\U0001f605')
😅
>>> print(emoji.demojize('😅'))
KeyboardInterrupt
>>> print(emoji.demojize('😅'))
:grinning_face_with_sweat:
>>> print(emoji.demojize('U0001f605'))
U0001f605
>>> print(emoji.demojize('\U0001f605'))
:grinning_face_with_sweat:
>>> print('\U0001f601',emoji.demojize('\U0001f601'))
😁 :beaming_face_with_smiling_eyes:
>>> # task
>>> emoji 601 to 630
SyntaxError: invalid syntax
>>> # ---------------------------------emoji 601 to 630
