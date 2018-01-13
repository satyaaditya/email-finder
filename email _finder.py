import pyperclip,re,ctypes

emailRegex = re.compile(r'''([a-zA-Z0-9._%+-]+@ [a-zA-Z0-9.-]+        
       (\.[a-zA-Z]{2,4})  
       )''', re.VERBOSE)
input_from_clipboard = (pyperclip.paste())
matches= []
for i in emailRegex.findall(input_from_clipboard):
    matches.append(i[0])
if len(matches) > 0:
    text_to_paste = '\n'.join(matches)
    ctypes.windll.user32.MessageBoxW(0,text_to_paste,"",1)
else:
    print "no emails found on this page"






