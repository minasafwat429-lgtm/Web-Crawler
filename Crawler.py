import options
import requests
import re
import urllib.parse
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="target_url", hrlp="Specify URL, -h for help")
    parser, arguments = parser.parse_args()

    if not options.target_url:
        parser.error("[-] Please specify url, -h for help")

    return options.target_url

target_url = "https://exmpile.com"
target_link= []

def get_links(url):
    response = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"',response.connect.decode())

def crawl(url):
    herf_links = get_links(url)
    for link in herf_links:
        link = urllib.parse.urljson(url, link)

        if "#" in link:
            link =link.split("#")[0]

        if url in  link not in target_link:
            target_link.append(link)
            print(link)
            crawl(link)

crawl(target_url)
