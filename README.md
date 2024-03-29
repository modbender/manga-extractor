# MEXT - Manga/Manhua/Manhwa Extractor

A simple manga extractor. Extracts any comic info, chapter list and chapter pages. This is an app that strictly provides API.

This package uses multiple provider codes to extract manga/manhua/manhwa data from online sites.

The providers and it's usage is listed below.

It's easy to use from python code.

**Still in development.**

This has been tested only on Windows 11 64-bit.

## Requirements

- Node.js

## Installations

```bash
pip install mext
```

<!-- **Important: It's necessary to have a virtual or real display to run this for best results** -->

## Proxy

To use proxy IP's
```bash
export HTTP_PROXY='http://10.10.10.10:8000'
export HTTPS_PROXY='http://10.10.10.10:1212'
```

## Steps:
1. Import `Mext` like this
    ```python
    from mext import Mext
    ```

2. Get the URL of manga or chapter and pass it to `Mext`

    ```python
    site_url = 'xxx0'
    manga_url = 'xxx1'
    chapter_url = 'xxx2'

    # Initialize
    me = Mext()

    # To get manga
    manga = me.get_manga(manga_url)

    # To get manga list
    manga_list = me.get_manga_list(site_url)

    # To get one particular chapter
    chapter = me.get_chapter(chapter_url)

    # Pass manga url to get chapter list belonging to manga
    chapter_list = me.get_manga_chapters(manga_url)
    ```

## Providers

1. MangaDex
2. AsuraScans
3. MangaUpdates (In development)
3. ReaperScans (In development)
3. ManhuaPlus (In development)

...others coming soon

## Usage

Get Manga using Manga URL

```python
from mext import Mext

manga_url = 'https://mangadex.org/title/d1c0d3f9-f359-467c-8474-0b2ea8e06f3d/bocchi-sensei-teach-me-mangadex'

manga = me.get_manga(manga_url) # You'll get back a instance of Mext with Manga data
print(manga.to_dict())
```

Get Chapter using Chapter URL

```python
from mext import Mext

chapter_url = 'https://mangadex.org/chapter/e183d3f4-fde0-4288-a1ed-8547490f84b3'

chapter = me.get_chapter(chapter_url) # You'll get back a instance of Mext with Chapter data
print(chapter.to_dict())
```

Get Chapters List belonging to a manga using Manga URL
```python
from mext import Mext

manga_url = 'https://mangadex.org/title/f7972eed-0040-4aac-b8de-fc99c522c25a/anti-kissmanga-anthology'

chapter_list = me.get_manga_chapters(manga_url) # You'll get back a list of instances of Mext with a list of Chapter data
chapter_list = me.chapter_list
print(chapter_list.to_dict())
```

## Credits

Made using
- Mangadex API Documentation [Mangadex API](https://api.mangadex.org/docs/)
- Manga-py [manga-py](https://github.com/manga-py/manga-py)
- Mangadex API - [MangaDex.py](https://github.com/Proxymiity/MangaDex.py)

## Contributions
Ready for any genuine support and valid pull requests.
