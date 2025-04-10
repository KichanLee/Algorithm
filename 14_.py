def soloution(k, dungeons):
    curr = k
    adv = 0
    for d in dungeons:
        if current >= d[0] : 
            adv += 1
            current -= d[1]
        else : 
            break
    return adv
