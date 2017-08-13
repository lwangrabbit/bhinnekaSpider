import urllib2
from bs4 import BeautifulSoup
import cookielib
import urllib
import time
import re
import json

login_url = 'https://www.bhinneka.com/aspx/Login.aspx'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Upgrade-Insecure-Requests": "1",
    "Content-Type": "application/x-www-form-urlencoded"
    }

myCookie = cookielib.CookieJar()
pageOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(myCookie))

def get_view():
    loginPageRequest = urllib2.Request(url=login_url, headers=headers)
    loginPageHTML = pageOpener.open(loginPageRequest, timeout=30).read()
    soup = BeautifulSoup(loginPageHTML, "html.parser")
    __VIEWSTATE = soup.find(id="__VIEWSTATE")['value']
    print("__VIEWSTATE=" + __VIEWSTATE)
    __VIEWSTATEGENERATOR = soup.find(id="__VIEWSTATEGENERATOR")['value']
    print("__VIEWSTATEGENERATOR = " + __VIEWSTATEGENERATOR)
    return (__VIEWSTATE, __VIEWSTATEGENERATOR)

def login(user, pwd):
    (__VIEWSTATE, __VIEWSTATEGENERATOR) = get_view()
    login_data = {
        "__EVENTARGUMENT": "",
        "__EVENTTARGET": "",
        "__VIEWSTATE": __VIEWSTATE,
        "__VIEWSTATEGENERATOR": __VIEWSTATEGENERATOR,
        "ctl00$Search": "",
        "ctl00$content$LoginDefault$Password": "apeng1234",
        "ctl00$content$LoginDefault$UserName": "lwangrabbit@qq.com",
        "ctl00$content$LoginDefault$btnLogin": "Submit",
        "ctl00$ddlSearchCategory": "",
        "ctl00$hdnIsTablet": "",
        "ctl00$hdnSearchCategory": "",
        "eblast": "masukkan email di sini",
        "headerDayTglBayar": time.strftime("%d",time.localtime(time.time())),
        "headerKodeTrx": "",
        "headerMonthTglBayar": time.strftime("%m",time.localtime(time.time())),
        "headerNilaiBayar": "0",
        "headerYearTglBayar": time.strftime("%Y",time.localtime(time.time()))
    }
    login_data = urllib.urlencode(login_data)
    login_request = urllib2.Request(url=login_url, data=login_data, headers=headers)
    login_response = pageOpener.open(login_request, timeout=20).read()

    print("&&&&&&&&&&&&&&&&&")
    print(login_response)
    print("&&&&&&&&&&&&&&&&&")

    soup = BeautifulSoup(login_response, "html.parser")
    script = soup.find_all('script', limit=2)
    print(script)

    pattern = re.compile(r"(?<=googleTagManagerDataLayer[ ][=]).*?(?=[;])")
    json_str = re.findall(pattern, str(script))

    print(json_str[0])

    user_id = json.loads(json_str[0].replace("\\r\\n", "", -1))["UserID"]
    if user_id.strip() == '':
        return False
    else:
        return True


def get_addr_list():
    addr_url = 'https://www.bhinneka.com/aspx/member/mbr_myacc_profile.aspx'
    addr_request = urllib2.Request(url=addr_url, headers=headers)
    addr_response = pageOpener.open(addr_request, timeout=20).read()

    print("***********")
    print(addr_response)
    print("***********")

    soup = BeautifulSoup(addr_response, "html.parser")
    addr_html_list = soup.find_all("tr", style="line-height: 15px;")
    print("++++++++++++++++++")
    print(addr_html_list)
    print("++++++++++++++++++")

    addr_list = []
    for addr_html in addr_html_list:
        soup = BeautifulSoup(str(addr_html), "html.parser")
        addr = soup.find("span", class_="shippingAddress").string
        province = soup.find("span", class_="shippingProvince").string
        city = soup.find("span", class_="shippingCity").string
        district = soup.find("span", class_="shippingDistrict").string
        zip_code = soup.find("span", class_="shippingZipCode").string
        is_primary = soup.find("span", class_="shippingPrimary MainDisplayNone").string
        addr = {
            'addr': addr,
            'province': province,
            'city': city,
            'district': district,
            'zip_code': zip_code,
            'is_primary': is_primary
        }
        addr_list.append(addr)
    return addr_list