from fileloader import download
from readxmlfile import get_image_urls


# define main class for the app
class App:
    # initialize the class
    def __init__(self, folder='images', xml_file='exported_image_data.xml', xml_element='wp:attachment_url'):
        self.xml_file = xml_file
        self.xml_element = xml_element
        self.folder = folder
        self.main()

    def main(self):
        urls = get_image_urls(self.xml_file, self.xml_element)

        for url in urls:
            if len(url) > 1:
                print(f'Downloading file {url} :: {len(url)}')
                download(url, self.folder)
        print(f'All done, there were {len(urls)} files to download')


if __name__ == '__main__':
    # initialise app class
    App()
