# You must have selenium install in
# your system with firefox webdriver

from selenium import webdriver
import sys, os, re
from time import sleep

def banner():
    print("""
    ||     || ||    ||   ||===|
    ||     || ||    ||   ||   /
    ||     || ||==  ||== ||  / 
    ||=====|| ||    ||   ||=/
    ||     || ||    ||   ||
    ||     || ||    ||   ||
    ||     || |===  |=== ||  SELFIE


""")

if __name__ == "__main__":
    banner()
    try:
        driver = webdriver.Firefox()
    except:
        print("[!] It seems like *Firefox webdriver* is missing")
        sys.exit()
    try:
        filename = sys.argv[1]
        protocol = sys.argv[2]
        port = sys.argv[3]
    except:
        print("Usage: python3 httpselfie.py <path_to_subdomain_list> <protocol(http/https)> <port_no>")
        driver.quit()
        sys.exit()
    with open(filename, 'r') as file:
        for line in file:
            line = line.replace("\n", "")
            url = protocol + "://" + line + ":" + port
            try:
                driver.get(url)
                sleep(4)
                driver.get_screenshot_as_file((line + ".png"))
            except:
                pass

driver.quit()
print("[*] Task accomplished!")
