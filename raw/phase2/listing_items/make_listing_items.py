import re

import requests

LISTING_PARAMS = '?searchstring=&categoryid=all&action=searchengine&subaction=search&startindex=0'


def listing_urls(url: str):
    try:
        response = requests.get(url+LISTING_PARAMS, headers={'Referer': 'not Googlebot'}, timeout=10)
    except Exception:
        print('Skipping', url)
        return None
    assert response.status_code == 200
    assert response.text.count('<TD NOWRAP align=center><B>') == 1
    num_results = re.search('<TD NOWRAP align=center><B>[^0-9<]+([0-9]+)', response.text).group(1)
    print(url, num_results)
    with open(url.split('/')[2]+'_listing_items.txt', 'w') as f:
        for i in range(0, int(num_results), 10):
            f.write('url:{}{}\n'.format(url, LISTING_PARAMS.replace('startindex=0', 'startindex='+str(i))))

def main():
    for url in (
        'http://cgiserv01.fc2web.com/cgi-bin/se.cgi',
        'http://cgiserv01.gooside.com/cgi-bin/se.cgi',
        'http://cgiserv01.k-free.net/cgi-bin/se.cgi',
        'http://cgiserv01.easter.ne.jp/cgi-bin/se.cgi',
        'http://cgiserv01.muvc.net/cgi-bin/se.cgi',
        'http://cgiserv01.55street.net/cgi-bin/se.cgi',
        'http://cgiserv01.zero-city.com/cgi-bin/se.cgi',
        'http://cgiserv01.ojiji.net/cgi-bin/se.cgi',
        'http://cgiserv01.k-server.org/cgi-bin/se.cgi',
        'http://cgiserv01.zero-yen.com/cgi-bin/se.cgi',
        'http://cgiserv01.h.fc2.com/cgi-bin/se.cgi',
        'http://cgiserv01.iui.fc2.com/cgi-bin/se.cgi',
        'http://cgiserv01.happy-web.fc2.com/cgi-bin/se.cgi',
        'http://cgiserv01.kt.fc2.com/cgi-bin/se.cgi',
        'http://cgiserv01.finito.fc2.com/cgi-bin/se.cgi',
        'http://cgiserv01.ktplan.fc2.com/cgi-bin/se.cgi',
        'http://cgiserv01.pimp.fc2.com/cgi-bin/se.cgi'
    ):
        listing_urls(url.replace('cgiserv01', 'www'))

if __name__ == '__main__':
    main()

