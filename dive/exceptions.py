

try:
    import termios, TERMIOS
except ImportError:
    try:
        import msvcrt
    except ImportError:
        try:
            from EasyDialogs import AskPassword
        except ImportError:
            print "None available"
        else:
           print "EasyDialogs"
    else:
       print "msvcrt"
else:
    print "termios"

