from bs4 import BeautifulSoup
import re
import os

dynasties = ['ming', 'qing', 'song', 'tang']

for dynasty in dynasties:
    directory = f'corpus/{dynasty}'
    totaltext = ''
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)

            with open(filepath, 'r', encoding='utf8') as file:
                html = file.read()
                
            soup = BeautifulSoup(html, 'lxml')
            text = soup.getText()
            text = text[text.find('*** START OF THE PROJECT GUTENBERG EBOOK'):text.find('*** END OF THE PROJECT GUTENBERG')]
            text = text.replace('*** START OF THE PROJECT GUTENBERG EBOOK ', '')
            text = ''.join(re.findall(r'[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff\U00020000-\U0002a6df]+', text))

            totaltext += text
    
    with open(f'corpus/{dynasty}/{dynasty}.txt', 'w', encoding='utf8') as file:
        file.write(totaltext)