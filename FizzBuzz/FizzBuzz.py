

deviders = {'4': 'fizz', '3': 'buzz', '5': 'free', '7': 'karma'}


def fizzbuzz(length, start=0):
    for i in range(start, start+length):
        out = [i]
        for num in deviders.keys():
            if(i % int(num) == 0):
                out.append(deviders[num])
        print(f'#{out.pop(0):5}:{"".join(out)}')


fizzbuzz(100)
