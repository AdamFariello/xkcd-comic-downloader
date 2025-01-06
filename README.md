# xkcd-comic-downloader
Script to download all the comics from xkcd.    
This script was made as a challenge by the book, 
"How to automate the boring things with Python", ch.12.   

The practice project can be found here:   
https://automatetheboringstuff.com/2e/chapter12/


## Dependencies
* Python 3.0+
* BeautifulSoup4 library
* Requests Library

## Installing Dependencies 
#### Running the code in vscode
Install the python library in the "extention" tab on the side bar. 

#### Locally
##### Arch (My system)
```bash
sudo pacman -S python python-requests python-beautifulsoup4  
```

##### Apt
```bash
sudo aptget update && sudo aptget install python python-requests python-beautifulsoup4  
```


## Running the script
```bash
python xkcd.py {dir} 
```
Directory is optional   
If Directory isn't given, it'll download the comics in the same location the script is.



## Development Process of the File
The file, "<code>ObsidianNote.md</code>", is where the script was originally worked on, 
along side where the script's structure and planning was done.   
