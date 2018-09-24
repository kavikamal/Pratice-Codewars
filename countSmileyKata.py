import re
def count_smileys(arr):
    r = re.compile(r'(?::|;)(?:-|~)?(?:\)|D)')
    return len(list(filter(r.match, arr)))

print count_smileys([':)',':(',':D',':O',':;'])    