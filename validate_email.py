import re

banned_char = [
    "!",
    "#",
    "$",
    "%",
    "&",
    "'",
    "*",
    "+",
    "-",
    "/",
    "=",
    "?",
    "^",
    "_",
    "`",
    "{",
    "|",
    "}",
    "~",
    " ",
]


def email_check(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    if len(email) > 256:
        return False
    for char in banned_char:
        if char in email:
            return False
    return True


print(email_check(""))
