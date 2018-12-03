import re
def fun(s):
    output = False
    # return True if s is a valid email, else return False
    email = s
    if ('@' not in email or '.' not in email ):
        return output
    if (email.index('@') > email.index('.')):
        return output   
    if (email.count('@') > 1 or email.count('.') > 1):
        return output
    uname = email.split('@')[0]
    if (len(uname) == 0):
        return output
    wname = email.split('@')[1].split('.')[0]
    if (len(wname) == 0):
        return output
    ext = True if len(email.split('@')[1].split('.')[1]) <= 3 else False
    if (re.match("^[A-Za-z0-9_-]*$",uname) and re.match("^[A-Za-z0-9]*$",wname) and ext):
        output = True
    return output


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)