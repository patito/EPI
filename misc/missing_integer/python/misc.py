

def solution(array, size):
    minor = 1
    for i in range(size):
        if minor not in array:
            break
        minor += 1
    return minor
