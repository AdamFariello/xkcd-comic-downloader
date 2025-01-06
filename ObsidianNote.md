---
Name: Chapter 12 -- Downloading All XKCD Comics (Github)
date: 2025-01-05
tags:
  - Python
  - How_to_automate_the_boring_stuff_with_python
  - Book
book: How to automate the boring stuff with python
---
# Project
## Challenge (poised by the book)
 Here’s what your program does:
 1. Loads the XKCD home page
 2. Saves the comic image on that page
 3. Follows the Previous Comic link
 4. Repeats until it reaches the first comic
So the code should do:
1. Download pages with the requests module.
2. Find the URL of the comic image for a page using Beautiful Soup.
3. Download and save the comic image to the hard drive with <code>iter_content()</code>
4. Find the URL of the Previous Comic link, and repeat.

## Check list
### Just for the book
1. [x] Imports
2. [x] Download webpage
3. [x] Get image link, and download it
4. [x] Get link to previous button
5. [x] Use previous button link to get previous comic
6. [x] Cycle 2 - 6 with loop
7. [x] Create (function) check where last comic is reached
8. [x] Add main function and [[Python -- Declaring functions#If statement (and function) to make file NOT a script|if statement]].
### Additional (for me)
1. [x] Add (singular argument option for) directories
2. [x] Add comic number to filename, prefacing comic's title
3. [x] Add exit for last comic
### For Others to use the file
1. [ ] Add regex library, and use it for checking, (instead of over using [[Python -- Partition String|partition()]])
2. [ ] Add function (using [[Python -- Regex|regex]]) to validate directory given by user.

## Solution
### Import 
* [[Python -- sys.argv]]
* [[Python -- Beautiful Soup 4|Python -- bs4]]
* [[Python -- Requests Library]]

### Code
```python
import requests, bs4, sys

website = "https://xkcd.com/"

def downloadComic(soup, directory):
    def getCurrentComicNumber(soup):
        comicUrl = soup.select_one("meta[property='og:url']")
        comicNumber = comicUrl.get("content")
        comicNumber = comicNumber.partition(".com/")[-1]
        return comicNumber[0:-1]
    def getComicLink(soup):
        image = soup.select_one("div[id = 'comic'] > img")
        image = image.get("src")[2:]
        image = "https://" + image
        return image


    try:
        # Get Image Link
        imageLink = getComicLink(soup)
        res = requests.get(imageLink)
        res.raise_for_status()

        # Naming File
        comicNumber = getCurrentComicNumber(soup)
        comicName = imageLink.partition("comics/")[-1]
        fileName = comicNumber + "." + comicName

        # Writing the File
        comic = open(directory + fileName, 'wb')
        for chunk in res.iter_content(100000):
            comic.write(chunk)
            comic.close()
    except Exception as e:
        print("ERROR: Couldn't download the comic")
        print(e)


def getBackButton(soup):
    backButton = soup.select_one("a[rel = 'prev']")
    backButton = backButton.get("href")
    if backButton != "#":
        webpage = requests.get(website + backButton)
        return webpage
    else:
        return None


def main ():
    #TODO: Validation of directory name used below
    directory = sys.argv[1] + "/" if len(sys.argv) == 2 else "./"
    try:
        webpage = requests.get(website)

        while True:
            # Setup
            webpage.raise_for_status()
            soup = bs4.BeautifulSoup(webpage.text, "html.parser")
            # Download comic (function to get it is called there) 
            downloadComic(soup, directory)

            webpage = getBackButton(soup)
            return 0
    except:
        print("That's the end of the links")
if __name__ == '__main__': main()
```