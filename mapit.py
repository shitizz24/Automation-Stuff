import webbrowser,sys

sys.argv # Address

if len(sys.argv>1) :
    # Address List
    address=' '.join(sys.argv[1:])
else:
    #Copy address from ClipBoard
    
