import requests
import re
import urllib.parse
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="target_url", help="Specify URL, -h for help")
    options, arguments = parser.parse_args()

    if not options.target_url:
        parser.error("[-] Please specify url, -h for help")

    return options.target_url

def get_links(url):
    try:
        response = requests.get(url, timeout=10)
        return re.findall('(?:href=")(.*?)"', response.text)
    except:
        return []

def crawl(url, base_url, visited=None):
    if visited is None:
        visited = set()
    
    if url in visited:
        return visited
    
    visited.add(url)
    print(url)
    
    for link in get_links(url):
        full_link = urllib.parse.urljoin(url, link)
        full_link = full_link.split("#")[0]
        
        if base_url in full_link and full_link not in visited:
            crawl(full_link, base_url, visited)
    
    return visited

if __name__ == "__main__":
    target_url = get_arguments()
    print(f"[+] Starting crawl on: {target_url}\n")
    crawl(target_url, target_url)
