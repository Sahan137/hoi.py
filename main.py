def omgekeerde_woord():
    while True:
        woord=input("vul hier het woord in wat je wilt omdraaien: ")
        omgekeerd_woord=""
        for i in reversed(woord):
            omgekeerd_woord += i
        print(omgekeerd_woord)

omgekeerde_woord()