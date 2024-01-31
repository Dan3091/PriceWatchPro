import requests
import time
from bs4 import BeautifulSoup


amazon_headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                  "accept-language": "en-RO,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6",
                  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                  "accept-encoding": "gzip, deflate, br",
                  "cache-control": "max-age=0",
                  "cookie": "aws-target-data=%7B%22support%22%3A%221%22%7D; regStatus=pre-register; aws-target-visitor-id=1702313721971-605603.47_0; session-id=139-9845569-9769362; i18n-prefs=USD; sp-cdn='L5Z9:RO'; ubid-main=135-8466086-5731228; lc-main=en_US; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19748%7CMCMID%7C52204828929361673681470566352073586422%7CMCAAMLH-1706806407%7C6%7CMCAAMB-1706806407%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1706208807s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; session-id-time=2082787201l; skin=noskin; session-token=78KWo2Ivaq16bTNR5PJrvvGd7dOk0oSKK1TDTMgXOi7twfnKog+ZPih1XDSwPyvd2ZjoJUcF+VxYiv5gOT7A4MXa7rX3IHivxyPhLGaXM1A1USSdrVizjVDxb5qQfbmqLOxjhkrs7XDzVTL7BO8iXBwhRzhxg/KC5kC6LpFQuy6ZzzOl9mICde6IR2sK4doyKphUKq+LHUUrPGKW5KeWbiasrkCicyaKyKGKUJuUVgGFGidDKB9VWFNkkUVDFeGaDJ8w/Mqh0E0EaLqXhXyLwXVrpjRCqVM8NueRGCyujAj32nl7onWEUkrBpDYyaLYVXFe83CZ11ZCEFJCcCe4X2WRZHfxRjJKe; csm-hit=tb:BDN96FG71DBW1AD8KHCF+s-BDN96FG71DBW1AD8KHCF|1706367635643&t:1706367635643&adb:adblk_no",
                  "device-memory": "8",
                  "downlink": "10",
                  "dpr": "1.25",
                  "ect": "4g",
                  "referer": "https://www.amazon.com/",
                  "rtt": "100",
                  "sec-ch-device-memory": "8",
                  "sec-ch-dpr": "1.25",
                  "sec-ch-ua": "'Not_A Brand';v='8', 'Chromium';v='120', 'Google Chrome';v='120'",
                  "sec-ch-ua-mobile": "?0",
                  "sec-ch-ua-platform": "'Windows'",
                  "sec-ch-ua-platform-version": "'15.0.0'",
                  "sec-ch-viewport-width": "1071",
                  "sec-fetch-dest": "document",
                  "sec-fetch-mode": "navigate",
                  "sec-fetch-site": "same-origin",
                  "sec-fetch-user": "?1",
                  "upgrade-insecure-requests": "1",
                  "viewport-width": "1071"}
url = ""


def html_file():
    """
    This function takes two arguments the url and headers,
    and by using the get method from requests module,
    it receives a response and assign it to html_data,
    after that it use BeautifulSoup class from bs4 module,
    and creates a soup object and return it.
    """

    html_data = requests.get(url, headers=amazon_headers)
    soup = BeautifulSoup(html_data.text, "html.parser")
    return soup

def check_server_availability(search_product_name):
    """
    Here this function check the availability of the server,
    by using the status_code method if status code is diverse from code 200
    it returns False and True otherwise.
    """

    response = requests.get(f"https://www.amazon.com/s?k={search_product_name}", headers=amazon_headers)
    if response.status_code != 200:
        return False
    return True

def next_page(soup):
    """
    By using the find method from soup object,
    this function check if the tag for next page button
    with href is preset then assign it to url and return it,
    otherwise it return None.
    """

    global url
    try:
        page = soup.find("span", class_="s-pagination-strip")
        if page.find("span", class_="s-pagination-item s-pagination-next s-pagination-disabled") == None:
            url = f"http://www.amazon.com/{str(page.find('a', class_='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator').get('href'))}"
            return url
    except:
        pass
    return

def search_item(price, search_product_name):
    """
    This is the main function that takes two arguments,
    the price and the search_product_name and if present,
    returns a dictionary data in format:
    {product_name: [product_title, product_price, product_url]}
    otherwise return False.
     """

    data = {}
    global url
    try:
        search_product_name = search_product_name.replace(" ", "+")
    except:
        pass
    url = f"https://www.amazon.com/s?k={search_product_name}"
    soup = html_file()
    if "No results for " in soup.get_text():
        return False

    while True:
        soup = html_file()
        url = next_page(soup)
        if not url:
            break
        else:
            item = soup.find_all("div", class_="puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v2rh3j15wdcp4q29xeaptoa72x6 s-latency-cf-section puis-card-border")
            for i in item:
                if i != None:
                    try:
                        product_title = i.find("span", class_="a-size-medium a-color-base").get_text()
                        product_name = i.find("span", class_="a-size-medium a-color-base a-text-normal").get_text()
                        product_price = i.select_one("span.a-price").select_one("span.a-offscreen").get_text()
                        product_url = i.find("a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal", href=True).get("href")
                        if float(product_price[1:]) <= price:
                            data[product_name] = [product_title, product_price, f"https://www.amazon.com{product_url}"]
                    except:
                        pass
    return data