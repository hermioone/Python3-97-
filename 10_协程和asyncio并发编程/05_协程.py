async def downloader(url):
    return "hermione"


async def download_url(url):
    html = await downloader(url)
    return html

if __name__ == "__main__":
    coro = download_url("http://www.hermione.com")
    coro.send(None)
