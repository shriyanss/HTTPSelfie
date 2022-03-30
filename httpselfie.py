# You must have selenium installed in
# your system with firefox webdriver
# by default. You can change the 
# webdriver in line 26

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
        if protocol != "url":
            port = sys.argv[3]
    except:
        print("Usage: python3 httpselfie.py <path_to_subdomain_list> <protocol(http/https)> <port_no>\n     OR\npython3 httpselfie.py <path_to_url_list> url")
        driver.quit()
        sys.exit()
    with open(filename, 'r') as file:
        for line in file:
            if sys.argv[2] == "url":
                try:
                    driver.get(line)
                    sleep(4)
                    driver.get_screenshot_as_file((line.replace("/", ">") + ".png"))
                    print(line.replace("\n", ''))
                except:
                    pass
            else:
                line = line.replace("\n", "")
                url = protocol + "://" + line + ":" + port
                try:
                    driver.get(url)
                    sleep(4)
                    driver.get_screenshot_as_file((line.replace("/", ">") + ".png"))
                    print(url)
                except:
                    pass

driver.quit()
print("[*] Task accomplished!")
