import base64

img = open('deity.png','rb').read()
b64 = 'data:image/png;base64,' + base64.b64encode(img).decode()

with open('wedding-invitation (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

if 'deity.png' in html:
    html = html.replace('href="deity.png"', f'href="{b64}"')
    with open('wedding-invitation (1).html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Replaced deity.png. Size:', len(html)//1024, 'KB')
elif 'DEITY_IMAGE_PLACEHOLDER' in html:
    html = html.replace('DEITY_IMAGE_PLACEHOLDER', b64)
    with open('wedding-invitation (1).html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Replaced placeholder. Size:', len(html)//1024, 'KB')
else:
    # Search what's there
    idx = html.find('Deity image')
    print('Found deity comment at:', idx)
    if idx != -1:
        print(html[idx:idx+300])
    else:
        print('No deity marker found. First 1000 chars:')
        print(html[:1000])
