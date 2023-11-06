sitename = "www.orc.org"


def hasher(site):
    site = site.split(".")[1]
    site = site.split(".")[0]
    site = site.upper()
    site = [ord(c) for c in site]
    total = 0
    for i in site:
        total += i
    return total


print(hasher(sitename))
