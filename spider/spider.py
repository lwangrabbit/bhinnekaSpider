import urllib2
from bs4 import BeautifulSoup
import cookielib

hostUrl = 'http://www.bhinneka.com/aspx/faq/faqindex.aspx'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Upgrade-Insecure-Requests": "1",
    }
myCookie = cookielib.CookieJar()
pageOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(myCookie))
loginPageRequest = urllib2.Request(url=hostUrl, headers=headers)
loginPageHTML = pageOpener.open(loginPageRequest).read()

soup = BeautifulSoup(loginPageHTML)

__VIEWSTATE = soup.find(id="__VIEWSTATE")['value']
print("__VIEWSTATE=" + __VIEWSTATE)

login_data = {
    ''
}

