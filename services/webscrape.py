import urllib.request

dynasties = ['ming', 'qing', 'song', 'tang']

for dynasty in dynasties:
    with open(f'links/{dynasty}.txt', 'r') as file:
        contents = file.read()

    urls = contents.split()

    for url in urls:
        with urllib.request.urlopen(url) as request:
            contents = request.read()

        html = contents.decode()

        filename = url.replace('/','').replace('https:www.gutenberg.orgcacheepub', '')
        print(filename)

        with open(f'corpus/{dynasty}/{filename}', 'w', encoding='utf8') as file:
            file.write(html)
    