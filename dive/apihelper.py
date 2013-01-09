def info(object, spacing=10, collapse=1):
    """Print all methods and their docstrings.
    """

    methodList = [method for method in dir(object) if callable(getattr(object, method)) and not str(method).startswith("__")]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n\n\n".join(["%s %s" %
                    (method.ljust(spacing),
                        processFunc(str(getattr(object, method).__doc__)))
                    for method in methodList])


if __name__ == "__main__":

    #methodList = [method for method in dir(object) if callable(getattr(object, method))]
    #for each_m in methodList:
    #    print each_m

    #print "---"
    #for each_d in dir(object):
    #    print each_d

    #l = []

    print getattr(l,"pop")


    #info(re)


