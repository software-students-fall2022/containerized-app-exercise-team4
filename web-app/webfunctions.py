def countsScores(scoresList):
    failed,average,good,veryGood,excellent,perfect=0,0,0,0,0,0
    for score in scoresList:
        if score=="Very Good":
            veryGood+=1
        elif score=="Average":
            average+=1
        elif score=="Excellent":
            excellent+=1
        elif score=="Perfect":
            perfect+=1
        elif score=="Failed":
            failed+=1
        elif score=="Good":
            good+=1
    return failed,average,good,veryGood,excellent,perfect