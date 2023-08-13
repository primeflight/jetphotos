# jetphotos

Wrapper Python Web Site Jet Photos 

## Install

```bash
pip install -e git+https://github.com/primeflight/jetphotos.git@main#egg=jetphotos
```

## Usage

### Search photo aircraf by prefix.

```python
from jetphotos.search import Search

url_photo = Search.aircraft(prefix="PT-RVT")

print(url_photo)
```

Output
```bash
https://cdn.jetphotos.com/400/1/85322_1266979741.jpg
```