import re
import typing
import urllib.parse

import requests


def top_urls(url: str) -> typing.Set[str]:
    print(url)
    response = requests.get(url, timeout=10)
    items = set()
    for s in re.findall(r'HREF="(top[^"]+\.html)"', response.text, re.I):
        items.add('url:'+urllib.parse.urljoin(url, s))
    print('Found', len(items))
    return items


def main():
    items = set()
    for url in (
        "http://fc2web.com/g-i-m-g-s/top/002/",
        "http://fc2web.com/g-i-m-g-s/top/003/",
        "http://gooside.com/g-i-m-g-s/top/004/",
        "http://k-free.net/g-i-m-g-s/top/005/",
        "http://easter.ne.jp/g-i-m-g-s/top/006/",
        "http://muvc.net/g-i-m-g-s/top/007/",
        "http://55street.net/g-i-m-g-s/top/008/",
        "http://zero-city.com/g-i-m-g-s/top/009/",
        "http://ojiji.net/g-i-m-g-s/top/010/",
        "http://k-server.org/g-i-m-g-s/top/011/",
        "http://zero-yen.com/g-i-m-g-s/top/012/",
        "http://fc2web.com/g-i-m-g-s/top/013/",
        "http://fc2web.com/g-i-m-g-s/top/014/",
        "http://fc2web.com/g-i-m-g-s/top/015/",
        "http://fc2web.com/g-i-m-g-s/top/016/",
        "http://fc2web.com/g-i-m-g-s/top/018/",
        "http://ktplan.fc2.com/g-i-m-g-s/top/019/",
        "http://pimp.fc2.com/g-i-m-g-s/top/020/"
    ):
        items |= top_urls(url)
    with open('top_urls.txt', 'w') as f:
        f.write('\n'.join(items)+'\n')

if __name__ == '__main__':
    main()

