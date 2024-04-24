# user-finder :

**Disclaimer: This script is for educational purposes only.**
**Do not use against any network, system or application that you don't own or have authorisation to test.**

**Licence** : this project is under the [MIT licence](https://mit-license.org/).
************************************

**user-finder** is a **python** script to **automatically** search to usernames online.
It is a **solo** project that I ([prc-github-prc](https://github.com/prc-github-prc)) developed to help OSINT investigators or pentesters to find someone online. The way that the script work will be detailed later.

**********
## Installation and configuration :

##### 1. Install git :
-windows : download the exe file for windows from the [official website](https://git-scm.com/download/win)
-linux (debian, ubuntu, kali...) : ```
```
sudo apt install git
```
-linux (arch) : ```
```
sudo pacman -S git
```

##### 2. Install python(3) :
-windows : download the exe file from the [official website](https://www.python.org/downloads/) (if pip is **not directly installed** with python, please consider **searching solutions on internet**)

-linux (debian, ubuntu, kali...) : ```
```
sudo apt install python3 python3-pip
```
-linux (arch) : ```
```
sudo pacman -S python3 python3-pip
```

##### 3. Install dependencies with pip (some dependencies may be already satisfied):

-powershell or cmd for windows, bash or sh for linux : ```
```
pip install requests
```
or :
```
pip3 install requests
```

##### 4. Clone the project (commands are the same for windows and linux) :
```
git clone https://www.github.com/prc-github-prc/user-finder/
cd user-finder
```

##### 5. Utilisation (commands are the same for windows and linux) : 
from the project clone directory (./automated-pages-explorer/) :
```
python finder.py <username> <save file (optional)>
```
or :
```
python3 finder.py <username> <save file (optional)>
```

***************
## How it works ? :

This script work by generating a **wordlist of usernames that are similar** (to the username provided by the script user) and try them with a **list of sites**. It can be useful to find "hidden accounts" because some people
use differents **but** similar usernames with differents services.

If you want more details about how the **script works**, you can just **read the code and the comments**.
