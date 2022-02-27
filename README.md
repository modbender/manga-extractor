# MEXT - Manga/Manhua/Manhwa Extractor

A simple manga extractor. Extracts any comic info, chapter list and chapter pages. This is an app that strictly provides API.

**Still in development.**

## Installations

Not yet on pypi but will soon be, and then it will be like below

`pip install mext`


## Usage

This package uses multiple provider codes to extract manga/manhua/manhwa data from online sites.

The providers and it's usage is listed below.

It's easy to use from python code.

- Step 1:
Import `MangaExtractor` like this

  `from mext import MangaExtractor`

- Step 2:
Get the URL of manga or chapter and pass it to object of `MangaExtractor`

  ```python
  manga_url = 'xxx1'
  chapter_url = 'xxx2'

  # To get manga
  me = MangaExtractor(['manga'], manga_url)

  # To get one particular chapter
  me = MangaExtractor(['chapter'], chapter_url)

  # Pass manga url to get chapter list belonging to manga
  me = MangaExtractor(['chapters'], manga_url)

  # Pass manga url when you need both manga and chapter
  me = MangaExtractor(['manga', 'chapters'], manga_url)
  ```

## Providers

- Mangadex
- ...others coming soon

### Mangadex

Get Manga

```python
from mext import MangaExtractor

url = 'https://mangadex.org/title/d1c0d3f9-f359-467c-8474-0b2ea8e06f3d/bocchi-sensei-teach-me-mangadex'

me = MangaExtractor(['manga'], url)
data = me.get() #You'll get back a dictionary
print(vars(data['manga']))
```

Get Chapter

```python
from mext import MangaExtractor

url = 'https://mangadex.org/chapter/e183d3f4-fde0-4288-a1ed-8547490f84b3'

me = MangaExtractor(['chapter'], url)
data = me.get() #You'll get back a dictionary
print(vars(data['chapter']))
```


## Credits

Mangadex API - [MangaDex.py](https://github.com/Proxymiity/MangaDex.py)
