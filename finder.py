from sys import argv
import requests

def gen_chars_list(string:str) -> list:
    letters_and_numbers = {"a":"4","e":"3","b":"8","i":"1","o":"0"}
    numbers_and_letters = {"4":"a","3":"e","8":"b","1":"i","0":"o"}
    
    chars_lists = []
    
    for char in string:
        char = char.lower()
        possible_chars = [char]
        
        if char.upper() != char:
            possible_chars.append(char.upper())
            
        try:
            possible_chars.append(letters_and_numbers[char])
        except:
            try:
                possible_chars.append(numbers_and_letters[char])
            except:
                pass
        
        chars_lists.append(possible_chars)
    
    return chars_lists

def gen_wordlist(string:str) -> list:
    chars_list = gen_chars_list(string)
    wordlist = []
    nb_words = 1
    for elt in chars_list:
        nb_words *= len(elt)
    
    while len(wordlist) < nb_words -1 :
        new_word = ""
        for elt in chars_list:
            new_word += elt[random.randint(0,len(elt)-1)]
        
        if not new_word in wordlist and new_word != string:
            wordlist.append(new_word)
    
    wordlist.sort()
    
    return [string] + wordlist

def check_username(website:str, username:str) -> bool:
    url = website + username  
    
    try:
        response = requests.get(url,timeout=1)  # Make the HTTP request
        if response.status_code == 200:  # Check if the request was successful.
            return True
        else:
            return False
    except:
        return False


def store(data:str,filename:str) -> None:
    lines = []
    try:
        with open(filename,"r") as file:
            reader = file.readlines()
            file.close()
            for line in reader:
                lines.append(line.strip())
    except:
        pass
        
    lines.append(data)
    
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
        store_file = argv[2] # in case the script user provide of file name to store results
        open(store_file,"w").close()
        to_store = True
    except:
        to_store = False

    """
    list of checked websites 
    """
    sites_list = {"Instagram": "https://www.instagram.com/}",
    "Facebook": "https://www.facebook.com/",
    "YouTube": "https://www.youtube.com/user/",
    "Reddit": "https://www.reddit.com/user/",
    "GitHub": "https://github.com/",
    "Twitch": "https://www.twitch.tv/",
    "Pinterest": "https://www.pinterest.com/",
    "TikTok": "https://www.tiktok.com/@",
    "Flickr": "https://www.flickr.com/photos/"}
    
    wordlist = gen_wordlist(username) # similar usernames wordlist generation
    
    for username in wordlist: # for each word into the wordlist
        print()
        print(username,end=" :\n")
        for key,item in sites_list.items():
            result = check_username(item, username)
            if result:
                string = f"[+] user {username} found on {key}"
                print(string) # if the user was found on the website, we print it
                if to_store:
                    store(string,store_file)
    return 
    
    
if __name__ == "__main__":
    main()