import requests
from ezhashlib import hashlib
import sys


def req_api_data(query_char):

    '''Returns response for pwned website after passing the tail'''


    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code!=200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    else:
        return res


def get_pw_lead_count(hashes,hashes_to_check):


    hashes=(line.split(':') for line in hashes.text.splitlines())
    # Splits the response
    for h,count in hashes:


        if hashes_to_check == h:

               return count
    return 0



def pwned_api_check(password):


    sha1password=hashlib.sha1(password.encode('utf-8 ')).hexdigest().upper()
    # Generatng the sha1 for your password

    head,tail=sha1password[:5],sha1password[5:]
    res=req_api_data(head)
    #sending the head to website
    return get_pw_lead_count(res,tail)
    #Sending website response and tail for checking whether tail exists in the list of responses got from website.

def main():


    args=list(input().split())

    for passwords in args:
        count=pwned_api_check(passwords)

        if count:

            print(f"Change your \"{passwords}\" password idiot as it's pwned {count} times")

        else:
            print("You've used a good password!!")



main()
