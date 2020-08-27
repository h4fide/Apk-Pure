# <!-- OPEN SOURCE TEAM | JADILAH PROGRAMMER SEJATI
# <!-- Mengimpor Module Yang Dibutuhkan --!>
try:
    import requests
    import os
    from bs4 import BeautifulSoup as par
    import progressbar
except:
    os.system('pip2 install progressbar2')
    os.system('pip2 install requests')
    os.system('pip2 install bs4')

# <!-- Desain and Headers--!>
logo = '\n\x1b[1;92m         \xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\xa6\xe2\x95\x94\xe2\x95\x90   \x1b[1;97m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\xa6 \xe2\x95\xa6\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\n\x1b[1;92m         \xe2\x95\xa0\xe2\x95\x90\xe2\x95\xa3\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa0\xe2\x95\xa9\xe2\x95\x97\x1b[1;91m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91 \xe2\x95\x91\xe2\x95\xa0\xe2\x95\xa6\xe2\x95\x9d\xe2\x95\x91\xe2\x95\xa3\n\x1b[1;92m         \xe2\x95\xa9 \xe2\x95\xa9\xe2\x95\xa9  \xe2\x95\xa9 \xe2\x95\xa9   \x1b[1;97m\xe2\x95\xa9  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\n\x1b[1;91m     +-------------------------------+\n\x1b[1;97m       Author \x1b[1;91m: \x1b[1;96mRizky\n\x1b[1;97m       Github \x1b[1;91m: \x1b[1;96mgithub.com/hekelpro\n\x1b[1;91m     +-------------------------------+\n'
headers={'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'}

# <!-- Source Code Programming --!>
def progress():
    return progressbar.ProgressBar(
        redirect_stdout=True,
        redirect_stderr=True,
        widgets=[
            progressbar.Percentage(),
            progressbar.Bar(),
            ' (',
            progressbar.AdaptiveTransferSpeed(),
            ' ',
            progressbar.ETA(),
            ') ',
        ])

def unduh(url, out):
	print '\n\x1b[1;91m! \x1b[1;97mSedang Mengunduh\x1b[1;92m....'
	r = requests.get(url, headers=headers, stream=True)
	with open(out+'.apk', 'wb') as f:
		total_length = int(r.headers.get('content-length'))
		bar = progress()
		bar.start(total_length)
		readsofar = 0
		for chunk in r.iter_content(chunk_size=1024):
			if chunk:
				readsofar += len(chunk)
				bar.update(readsofar)
				f.write(chunk)
				f.flush()
		bar.finish()
	print '\x1b[1;91m! \x1b[1;97mSelesai\x1b[1;92m....'; print '\x1b[1;91m! \x1b[1;97mApk Disave \x1b[1;91m:\x1b[1;92m '+out+'.apk\n'

def main():
    os.system('clear')
    print logo
    nama = raw_input('\x1b[1;91m# \x1b[1;97mMasukan Nama Apk \x1b[1;91m:\x1b[1;92m ')
    link, no, garis = ([], 0, 45*'\x1b[1;92m-')
    try:
        req = requests.get('https://m.apkpure.com/id/search?q=' + nama.replace(' ', '+'), headers=headers).content
    except exceptions.ConnectionError:
        exit('\x1b[1;91m! \x1b[1;97mHidupkan Koneksi Anda\n')

    req = par(req, 'html.parser')
    print garis
    for a in req.find_all('a', attrs={'class': 'dd'}):
        ling = a.get('href')
        link.append(ling)

    for div in req.find_all('div', attrs={'class': 'r'}):
        no += 1
        jud = div.find('p', attrs={'class': 'p1'}).text
        dev = div.find('p', attrs={'class': 'p2'}).text
        jud = jud[:20]
        print '\x1b[1;97m' + str(no) + '   \x1b[32mAPLIKASI  \x1b[1;91m:\x1b[1;97m ' + jud + '...'
        print '    \x1b[32mDEVELOPER \x1b[1;91m:\x1b[1;97m ' + dev
        print garis

    try:
        pil = raw_input('\n\x1b[1;91m# \x1b[1;97mPilih Apk \x1b[1;91m:\x1b[1;92m ')
        if pil in ('', ' '):
            exit('\x1b[1;91m! \x1b[1;97mIsi Pilihan Anda\n')
    except IndexError:
        exit('\x1b[1;91m! \x1b[1;97mIsi Pilihan Anda\n')

    pil = int(pil) - 1
    out = raw_input('\x1b[1;91m# \x1b[1;97mOutput    \x1b[1;91m:\x1b[1;92m ')
    url = 'https://m.apkpure.com' + str(link[pil]) + '/download?from=details'
    run = requests.get(url, headers=headers)
    oks = par(run.content, 'html.parser')
    _find_1 = oks.find('div', attrs={'class': 'fast-download-box'})
    _find_2 = _find_1.find('a', attrs={'class': 'ga'})
    _find_3 = _find_1.find('span', attrs={'class': 'fsize'})
    size = _find_3.text
    print '\n\x1b[1;91m! \x1b[1;97mSize Aplikasi \x1b[1;91m:\x1b[1;92m ' + size.replace('(', '').replace(')', '')
    owh = raw_input('\x1b[1;91m! \x1b[1;97mYakin Untuk Mengunduh? [\x1b[1;92mY\x1b[1;97m/\x1b[1;91mT\x1b[1;97m]\n\x1b[1;97m        Jawab \x1b[1;91m:\x1b[1;92m ')
    if owh in ('', ' '):
        exit('\n\x1b[1;91m! \x1b[1;97mIsi Jawaban Anda\n')
    elif owh in ('Y', 'y'):
        file = _find_2.get('href')
        unduh(file, out)
    elif owh in ('T', 't'):
        exit('\n\x1b[1;91m* \x1b[1;97mProgram Terhenti\x1b[1;91m...\n')
    else:
        exit('\n\x1b[1;91m! \x1b[1;97mIsi Jawaban Anda\n')

# <!-- Hayyuk Gan Download Simontok Aja --!>
if __name__ == '__main__':
    main()
