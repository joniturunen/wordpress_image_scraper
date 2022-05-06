from bs4 import BeautifulSoup

def get_tags(xml_file: str, search_tag: str):
    # Reading the data inside the xml
    # file to a 'data' variable
    with open(xml_file, 'r') as f:
        data = f.read()

    # Passing the stored data inside
    # the beautifulsoup parser, storing
    # the returned object
    soup = BeautifulSoup(data, "xml")

    # Finding all instances of search_tag
    tags = soup.find_all(search_tag)
    
    return tags


def extract_values_from_tags(tags):
    urls = []
    for tag in tags:
        urls.append(tag.string)
    return urls


def get_image_urls(xml_file: str, search_tag: str):
    urls = extract_values_from_tags(get_tags(xml_file, search_tag))
    return urls