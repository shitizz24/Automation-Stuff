import webbrowser,sys,pyperclip

sys.argv # Address

if len(sys.argv)>1 :
    # Address List
    address=' '.join(sys.argv[1:])
else:
    #Copy address from ClipBoard
    address=pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+ address)
    
