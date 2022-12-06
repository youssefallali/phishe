<h1 align="center">Phishe</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.1-green?style=for-the-badge">
  <img src="https://camo.githubusercontent.com/5601a2b93c2e30f778dc2e4178da964cf682de8da7b2f22a5d27ec50bf95cbf3/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f77617463686572732f4b6173526f756472612f4d6178506869736865723f636f6c6f723d6379616e267374796c653d666f722d7468652d626164676526636f6c6f723d707572706c65">
  <img src="https://camo.githubusercontent.com/5def6d15dc01da804f574c1da1b99d93199a76fb07f9a48407c3b747d9bba84a/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f4b6173526f756472612f4d6178506869736865723f7374796c653d666f722d7468652d626164676526636f6c6f723d6f72616e6765">
  <img src="https://camo.githubusercontent.com/6e8c61de9d25be0310a2ad9fdf852dcc8b25a4bc4335d8a62c89aada39e317ac/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f4b6173526f756472612f4d6178506869736865723f7374796c653d666f722d7468652d626164676526636f6c6f723d626c7565">
 
<br>
<br>
  <img src="https://img.shields.io/badge/Author-Youssefallali-purple?style=flat-square">
  <img src="https://img.shields.io/badge/Open%20Source-Yes-cyan?style=flat-square">
  <img src="https://img.shields.io/badge/Made%20in-morocco-green?colorA=%23ff0000&colorB=%23017e40&style=flat-square">
  <img src="https://img.shields.io/badge/Written%20In-Python-blue?style=flat-square">
</p>


### [√] Description :

***A python phishing script for login phishing, image phishing, video phishing and many more***

### [+] Installation

##### Install primary dependencies (git, python)

 - For Debian (Ubuntu, Kali-Linux, Parrot)
    - ```sudo apt install git python3 php openssh-client -y```
 - For Arch (Manjaro)
    - ```sudo pacman -S git python3 php openssh --noconfirm```
 - For Redhat(Fedora)
    - ```sudo dnf install git python3 php openssh -y```
 - For Termux
    - ```pkg install git python3 php openssh -y```

##### Clone this repository

 - ```git clone https://github.com/youssefallali/phishe```

##### Enter the directory
 - ```cd Phishe```

##### Install all modules
 - ```pip3 install -r files/requirements.txt```

##### Run the tool
 - ```python3 phishe.py```

```

### Pip
 - `pip3 install maxphisher` [For Termux]
 - `sudo pip3 install phishe` [For Linux]
 - `phishe`

### Docker

 - `sudo docker pull youssefallali/phishe`
 - `sudo docker run --rm -it youssefallali/phishe`


### Support

OS         | Support Level
-----------|--------------
Linux      | Excellent
Android    | Excellent
iPhone     | Alpha (Recommended docker)
MacOS      | Alpha (Recommended docker)
Windows    | Unsupported (Use docker/virtual-box/vmware)
BSD        | Never tested

#### Options

```
usage: Phishe.py [-h] [-p PORT] [-t TYPE] [-o OPTION]
                     [-T TUNNELER] [-r REGION] [-S SUBDOMAIN]
                     [-d DIRECTORY] [-f FEST] [-i YTID] [-u URL]
                     [-s DURATION] [-m MODE] [-e TROUBLESHOOT]
                     [--nokey] [--noupdate]

options:
  usage: phishe.py [-h] [-p PORT] [-t TYPE] [-o OPTION]
                     [-T TUNNELER] [-r REGION] [-S SUBDOMAIN]
                     [-d DIRECTORY] [-f FEST] [-i YTID] [-u URL]
                     [-s DURATION] [-m MODE] [-e TROUBLESHOOT]
                     [--nokey] [--noupdate]

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Phishe's server port [Default : 8080]
  -t TYPE, --type TYPE  Phishe's phishing type index [Default :
                        null]
  -o OPTION, --option OPTION
                        Phishe's template index [ Default : null ]
  -T TUNNELER, --tunneler TUNNELER
                        Tunneler to be chosen while url shortening
                        [Default : Cloudflared]
  -r REGION, --region REGION
                        Region for ngrok and loclx [Default: auto]
  -S SUBDOMAIN, --subdomain SUBDOMAIN
                        Subdomain for ngrok and loclx [Pro Account]
                        (Default: null)
  -d DIRECTORY, --directory DIRECTORY
                        Directory where media files will be saved
                        [Default : /sdcard/Media]
  -f FEST, --fest FEST  Festival name for fest template [Default:
                        Birthday]
  -i YTID, --ytid YTID  Youtube video ID for yttv template [Default :
                        6hHmkInZkMQ (NASA Video)]
  -u URL, --url URL     Redirection url for ip-tracking or login
                        phishing [Default : null]
  -s DURATION, --duration DURATION
                        Media duration while capturing [Default :
                        5000(ms)]
  -m MODE, --mode MODE  Mode of MaxPhisher [Default: normal]
  -e TROUBLESHOOT, --troubleshoot TROUBLESHOOT
                        Troubleshoot a tunneler [Default: null]
  --nokey               Use localtunnel without ssh key [Default:
                        False]
  --noupdate            Skip update checking [Default : False]

### Features:

 - Multi platform (Supports most linux)
 - 100+ templates
 - Concurrent 4 tunneling (Ngrok, Cloudflared and LocalXpose, LocalHostRun)
 - OTP Support
 - Credentials mailing
 - Easy to use
 - Possible error diagnoser
 - Built-in masking of URL
 - Custom masking of URL
 - URL Shadowing
 - Portable file (Can be run from any directory)
 - Get IP Address and many other details along with login credentials


### Requirements

 - `Python(3)`
   - `requests`
   - `bs4`
   - `rich`
 - `PHP`
 - `SSH`
 - 900MB storage
 
If not found, php, ssh and python modoules will be installed on first run

#### Tested on

 - `Termux`
 - `Ubuntu`
 - `Kali-Linux`
 - `Arch`
 - `Fedora`
 - `Manjaro`

## Usage

1. Run the script
2. Choose a Website
3. Wait sometimes for setting up all
4. Send the generated link to victim
5. Wait for victim login. As soon as he/she logs in, credentials will be captured

<h1 align="center">Desclaimer</h1>



 
## [!] Disclaimer
***This tool is developed for educational purposes. Here it demonstrates how phishing works. If anybody wants to gain unauthorized access to someones social media, he/she may try out this at his/her own risk. You have your own responsibilities and you are liable to any damage or violation of laws by this tool. The author is not responsible for any misuse of MaxPhisher!***




