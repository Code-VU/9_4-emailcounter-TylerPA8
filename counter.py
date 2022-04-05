def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
        handle = open(name)
    else:
        handle = open(name)
    fr = handle.readlines()
    froms ={}
    for n in fr:
        if n.startswith("From "):
            n = n.strip()
            n = n.split(' ')
            if n[1] in froms:
                froms[n[1]] += 1
            else:
                froms[n[1]] = 1
    maxSender = max(froms, key=froms.get)
    print(maxSender + " " + str(froms[maxSender]))
## if you want to test locally before you try to sync
## uncomment countEmail() and run > python counter.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
##countEmail()
