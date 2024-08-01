from sys import argv
import requests
import random

def gen_chars_list(string:str,level:int) -> list:
    """
    this function take as argument the username string and the 'level' of generation. It returns a list of chars to use in a wordlist generator
    """

    # a number and a letter can be similar and used instead of each other
    letters_and_numbers = {"a":"4","e":"3","b":"8","i":"1","o":"0"}
    numbers_and_letters = {"4":"a","3":"e","8":"b","1":"i","0":"o"}
    
    chars_lists = [] # final list
    
    for char in string: # for each char
        possible_chars = [char]

        if char in "azertyuiopqsdfghjklmwxcvbn" or char in "AZERTYUIOPQSDFGHJKLMWXCVBN":
            if level == 3:
                if char == char.upper():
                    possible_chars.append(char.lower())
                else:
                    possible_chars.append(char.upper())
            try:
                possible_chars.append(letters_and_numbers[char])
            except:
                pass
        else:
            try:
                possible_chars.append(numbers_and_letters[char])
            except:
                pass
        
        chars_lists.append(possible_chars)
    
    return chars_lists # return 

def gen_wordlist(string:str,level:int) -> list:

    """
    This function take as argument the username string that will be the base for the wordlist and the 'generation level'. It returns
    the wordlist.
    """
    chars_list = gen_chars_list(string,level) # generate a list of characters to use
    wordlist = [] # wordlist
    nb_words = 1

    print(chars_list)

    for elt in chars_list:
        nb_words *= len(elt) # evaluating the final lenght of the wordlist
    
    while len(wordlist) < nb_words -1 : # while there is new words to find
        # we create a new word randomly
        new_word = ""
        for elt in chars_list:
            new_word += elt[random.randint(0,len(elt)-1)]
        
        if not new_word in wordlist and new_word != string: # if this is a new word, we add it
            wordlist.append(new_word)
    
    wordlist.sort() # sort of the list
    
    return [string] + wordlist # return

def check_username(website:str, username:str) -> bool:
    """
    This function takes as argument the website's url to verify and the username to try.
    It try to access to the potential user profile.
    If it is a success, the function returns True, else it returns False.
    """
    url = website + username # url to try
    
    try:
        response = requests.get(url,timeout=1)  # Make the HTTP request
        if response.status_code == 200:  # Check if the request was successful.
            return True # if everything is ok, returns True
        else:
            return False # False
    except:
        return False # False


def store(data:str,filename:str) -> None:
    """
    This function take as argument the data the add at the end of the file and the name of the file.
    Then it find and store the content into a list, add the data to write into this list, and write the entire list
    into the file.
    """

    """
    storing of the content of the file
    """

    lines = []
    try:
        with open(filename,"r") as file:
            reader = file.readlines()
            file.close()
            for line in reader:
                lines.append(line.strip())
    except:
        pass
        
    lines.append(data) # the data is added
    
    """
    all content is re-writed into the file
    """

    with open(filename,"w") as file:
        for line in lines:
            file.write(f"{line}\n")
    
    return
            

def main() -> None:
    
    """
    This is the main function.
    It generate a wordlist of potential usernames similar to the username provided by the user.
    Then for each username, it try to find a user in every website in the list.
    It print the positives results and if the user provided a file, it store the data into the file to.
    """

    print("#### User finder ####")

    try:
        username = argv[1] # user to search
    except:
        print("error : username not provided")
        return

    try:
        sites_list = [line.strip() for line in open(argv[2],"r").readlines()] # wordlist of sites 
    except:
        print("error : sites list not provided")
        return
    
    try:
        level = argv[3] #"level of username wordlist generator : 1 = only username provided by script user, 2 = letters and numbers, 3 = upcase and lowcase."
        try:
            level = int(level)
        except:
            print("error : level is not int")
            return
        if level >= 1 and level <= 3:
            pass
        else:
            print('error : level must be in [1;3]')
            return
    except:
        print("error : level not provided")
        return
    
    try:
        store_file = argv[4] # in case the script user provide of file name to store results
        open(store_file,"w").close()
        to_store = True
    except:
        to_store = False
    
    if level == 1:
        wordlist = [username]
    else:
        wordlist = gen_wordlist(username,level) # similar usernames wordlist generation
    
    print(wordlist)

    for username in wordlist: # for each word into the wordlist
        print()
        print(username,end=" :\n")
        for site in sites_list:
            result = check_username(site, username)
            if result:
                string = f"[+] user {username} found on {site}"
                print(string) # if the user was found on the website, we print it
                if to_store:
                    store(string,store_file)
        if to_store:
            store("",store_file)
        
    return 
    
    
if __name__ == "__main__":
    main()