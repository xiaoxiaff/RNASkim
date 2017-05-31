with open("chr22_small.fa", "r") as f:
    xx = "_._"
    data = f.readlines()
    isBegin = True
    cnt = 1
    for line in data:
        if line[0] == '>':
            if isBegin:
                pass
            else:
                print ("\n", end="")
            isBegin = False
            words = line.split('|')
            # headerAndId = "gi" + xx + words[1] + xx + words[2] + xx + words[3] + xx
            # headerAndId = "gi" + xx + str(cnt) + xx + words[1] + xx + words[3]
            headerAndId = "gi" + xx + str(cnt)
            output = ">" + headerAndId + "|" + headerAndId
            print (output)
            cnt += 1
        else:
            print (line[:-1], end="")