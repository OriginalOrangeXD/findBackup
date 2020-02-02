import requests
import argparse

def parseArgs():
    parse = argparse.ArgumentParser()
    parse.add_argument("-w", "--wordlist", dest="wordlist", help="The wordlist you would liek to use")
    parse.add_argument("-t", "--target", dest="target", help="The list of targets you would like to attack")
    parse.add_argument("-u", "--url", dest="url", help="The url you would like to attack")
    options = parse.parse_args()
    if not options.target:
        print("You forgot to enter a target file")
    if not options.wordlist:
        print("You forgot to enter a wordlist file")
    if not options.url:
        print("You have forgotten to enter a url")
    return options

def sendReq(url):
    response = requests.get(str(url))
    return response.status_code


parseInfo = parseArgs()
print(parseInfo.target, parseInfo.wordlist)
statusList = [200, 204, 301, 307, 401, 403]
with open(parseInfo.target, "r") as targetFiles, open(parseInfo.wordlist, "r") as potentialDirectories:
    allBruteFiles = []
    for line in targetFiles:
        bruteFile = line.strip()
        allBruteFiles.append(line)
    for line2 in potentialDirectories:
        indicator = line2.strip()
        for lin in allBruteFiles:
            fullURL = parseInfo.url + lin.strip()+ indicator
            #print(fullURL)
            statusCode = sendReq(fullURL)
            #print(statusCode)
            if statusCode in statusList:
                print("we in")
                print(fullURL, " Status Code: ", statusCode)


