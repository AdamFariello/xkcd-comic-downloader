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

            # if the webpage is "None", then it'll throw an error, ending the loop
            webpage = getBackButton(soup)
    except:
        print("That's the end of the links")
if __name__ == '__main__': main()
