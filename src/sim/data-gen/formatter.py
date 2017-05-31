with open("chr22_small.fa", "r") as f:
    xx = "_._"
    data = f.readlines()
    isBegin = True
    for line in data:
        if line[0] == '>':
            if isBegin:
                pass
            else:
                print ("\n", end="")
            isBegin = False
            words = line.split('|')
            headerAndId = "gi" + xx + words[1] + xx + words[2] + xx + words[3] + xx
            output = ">" + headerAndId + "|" + headerAndId
            print (output)
        else:
            print (line[:-1], end="")