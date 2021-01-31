with open('filename.txt', 'w', encoding='utf-8') as f:
    with open('url.txt', 'r', encoding='utf-8') as fpp:
        for line in fpp:
            c = line.split('/')[-1]
            c = c.split('.')[0]
            f.write(c + "   --->" + line)
with open('filename.txt', 'r', encoding='utf-8') as fp:
    print(fp.read())
