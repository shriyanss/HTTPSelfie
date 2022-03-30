# HTTPSelfie
This is a simple, yet effective website screenshotting tool written in python3

**Found it useful, how about *starring* this *repository* :)**
# Usage
- First of all, make a new folder
- Now, make a list of subdomains in that folder
- Paste the python script in the same folder
- Now just run the command `python3 httpselfie.py <path_to_subdomain_list> <protocol(http/https)> <port_no>`
- This would create image file with name as `<host>.png`

# Features
- Screenshot for a subdomains list with certain protocol (http/https) and particular port
    - `python3 httpselfie.py <path_to_subdomain_list> <protocol(http/https)> <port_no>`
    ![](https://raw.githubusercontent.com/shriyanss/HTTPSelfie/main/media/gif/domains.gif)
- Screenshot for a list of URLs
    - `python3 httpselfie.py <path_to_url_list> url`
    ![](https://raw.githubusercontent.com/shriyanss/HTTPSelfie/main/media/gif/urls.gif)

# OS Support
Any OS with Python 3 and Selenium with webdriver installed can use the tool

## Error handling
If you think that the tool is stuck somewhere, please reload the page once (in new firefox window created) and it will move on.
