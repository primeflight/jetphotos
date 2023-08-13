from jetphotos.search import Search

links = Search.aircraft(prefix="PT-RVT")

for link in links:
    print(link)
