from flask import Flask
from flask import request
from flask import make_response
from spider.spider import *

app = Flask(__name__)

"""
request:
    {
        "user": "abc@xyz.com",
        "password": "abc"
    }
response:
    1: 404 user/password not correct
    {
        "error": "Login Fail: Please check user and password"
    }
    2. 200 
    {
        [
            {
                'addr': "larry road 1008",
                'province': "bai",
                'city': "bai",
                'district': "bai",
                'zip_code': "81183",
                'is_primary': True
            }
        ]
    }
"""
@app.route('/api/bhinneka/address', methods=['POST'])
def bhinneka_addr():
    user = json.loads(request.data, strict=False)['user']
    pwd = json.loads(request.data, strict=False)['password']
    is_login = login(user, pwd)
    if is_login == False:
        return make_response('{"error": "Login Fail: Please check user and password"}', 404)
    addr_list = get_addr_list()
    return make_response(json.dumps(addr_list), 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8690, debug=True)



