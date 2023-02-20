import re

def l_extract(line):
    # 'l_extract is an acronym for line extraction
    items =  line.split()
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    email_list = []
    
    for item in items:
        if re.search(pattern, item):
            for email in re.findall(pattern, item):
                email_list.append(email)
    
    if email_list:
        return email_list


def read_file(file):

    with open(file) as email_raw:
        email_addresses = []
        
        for line in email_raw.readlines():
            email_list = l_extract(line)

            if email_list != None:
                # Lines without valid email addresses return an enpty list which eventually returns None and 'NoneType' cannot be iterated.
                for email in email_list:
                    email_addresses.append(email)
    
    return email_addresses
