animals = ['dog', 'cat', 'elephant']
tests = [
    (0, 'nothing'),
    (123, 'nothing'),
    (-1, 'nothing'),
    (42, 'everything'),
    (42 * 42, 'everything squared'),
]


def convertToCelsius(temperature):
    celsius = (temperature - 32.0) * (5.0/9.0) 
    return celsius


def weather_info(temp):
    c = convertToCelsius(temp)
    if (c < 0):
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")


def build_string(*args):
    return "I like {0}!".format(", ".join(args))


def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list


def what_is(x):
    print x
    if x == 42:
        return 'everything'
    elif x == 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'


def get_status(is_busy):
    return {"status": "busy" if is_busy else "available"}


def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];
    respond = dogs[0] if n <= 10 else (dogs[1] if n <= 50 else (dogs[3] if n == 101 else dogs[2]))
    return respond


def my_first_kata(a, b):
    print type(a)
    return (a % b + b % a) if isinstance(a, (int, long, float)) and isinstance(b, (int, long, float)) else False


def find_longest(string):
    spl = string.split(" ")
    longest = 0
    i = 0
    while (i < len(spl)):
        if (len(spl[i]) > longest):
            longest = len(spl[i])
        i += 1
    return longest


def correct_tail(body, tail):
    sub = body[-len(tail):]
    print sub
    if sub == tail:
        return True
    else:
        return False


def rain_amount(mm):
    if (mm < 40):
        return "You need to give your plant {}mm of water".format(40-mm)
    else:
        return "Your plant has had more than enough water for today!"


def quicksort(arr):
    if len(arr) < 1:
        return arr
    p = arr[0]
    # return quicksort(map(lambda x: x < p, arr[::-1])) + quicksort(map(lambda x: x > p, arr[2:]))
    return quicksort(map(lambda x: x < p, arr[:-1]))

# print list_animals(animals)
# for x, answer in tests:
#     print what_is(x)
# print get_status(True)["status"]
# print how_many_dalmatians(26)
# print my_first_kata("hello",3)
# print find_longest("The quick white fox jumped around the massive dog")
# print correct_tail("Fox", "x")
# print rain_amount(100)

print quicksort([17, -5, 3])
