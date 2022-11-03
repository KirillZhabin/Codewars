def warn_the_sheep(queue):
    queue.reverse()
    
    for i in range(len(queue)):
        if queue[i] == 'wolf' and i != 0:
            return 'Oi! Sheep number '+ str(i) +'! You are about to be eaten by a wolf!'
            break
        elif i == 0 and queue[i] == 'wolf':
            return 'Pls go away and stop eating my sheep'