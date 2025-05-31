import re
import sys

import zstandard


def main(filepath: str):
    print('Processing', filepath)
    with zstandard.open(filepath, 'r') as fin, \
        open(filepath.rsplit('.', 1)[0]+'_items.txt', 'w') as fout:
        for line in fin:
            line = line.strip()
            if len(line) == 0:
                continue
            if re.search('^https?://.', line):
                url = line
            elif '<loc>' in line:
                url = re.search('<loc>(https?://.+?)</loc>', line).group(1)
            elif line.startswith('"'):
                url = 'http://'+'/'.join([part.strip('",') for part in line.split('","')])
            elif 'http' in line:
                raise ValueError('Could not extract URL from line {}.'.format(line))
            else:
                continue
            if re.search(r'^https?://[^/]*fc2\.com', url):
                fout.write('url:{}\n'.format(url))
            else:
                print('Skipping unrelated URL {}.'.format(url))

if __name__ == '__main__':
    for filepath in sys.argv[1:]:
        main(filepath)

