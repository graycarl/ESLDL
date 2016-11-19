# -*- coding: utf-8 -*-
import os
import click
import requests
from bs4 import BeautifulSoup


class Syncer(object):
    """Sync audios from eslpod.com to local"""
    entryurl = "https://www.eslpod.com/website/"

    def __init__(self, path):
        self.path = path

    def _log(self, fmt, *args, **kwargs):
        click.echo(unicode(fmt).format(*args, **kwargs))

    def __call__(self):
        for name, url in self.crawl():
            self.sync_item(name, url)
        self._log('Done.')

    def crawl(self):
        """Crawl the web page"""
        html = requests.get(self.entryurl).text
        soup = BeautifulSoup(html, 'html.parser')
        self._log('Html load ok.')
        items = soup.find_all('table', class_='podcast_table_home')
        if not items or len(items) <= 1:
            self._log('No items found, cancel.')
            raise click.Abort
        # the first one is a title, not the data
        items = items[1:]
        self._log('{} items found.', len(items)-1)
        for item in items:
            name = item.select('span.podcast_title a')[0].text.strip()
            a = next(a for a in item.find_all('a') 
                     if a.text.strip() == 'Download Podcast')
            url = a.attrs['href']
            yield name + '.mp3', url

    def sync_item(self, name, url):
        local = os.path.join(self.path, name)
        temp = os.path.join(self.path, name + '.downloading')
        if os.path.exists(local):
            self._log('[{}] is already exists, ignore.', name)
            return
        with open(temp, 'wb') as f:
            self._download_item(f, name, url)
        os.rename(temp, local)

    def _download_item(self, f, name, url):
        self._log('Start to download [{}]', name, url)
        resp = requests.get(url, stream=True)
        total_length = resp.headers.get('content-length')
        if total_length is None:
            f.write(resp.content)
        else:
            with click.progressbar(length=int(total_length),
                                   label='Downloading') as bar:
                for data in resp.iter_content(chunk_size=4096):
                    f.write(data)
                    bar.update(len(data))
                                    

@click.command()
@click.option('--path', type=click.Path(file_okay=False))
def cli(path):
    if not path:
        path = os.path.expanduser('~/Music/eslpods')
    if not os.path.exists(path):
        if click.confirm('Dir [{}] not exists, create it?'.format(path)):
            os.makedirs(path)
        else:
            raise click.Abort
    syncer = Syncer(path)
    syncer()
