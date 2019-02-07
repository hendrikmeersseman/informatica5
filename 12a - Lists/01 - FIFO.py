invoer = input('Invoer: ')
queue = []
while invoer != 'STOP':

    if invoer != '?':
        queue.append(invoer)

    elif len(queue) > 0:
        print(queue.pop(0))
    invoer = input('Invoer: ')
