import requests

class Downloader:
    def __init__(self, url_list):
        self.url_list = url_list
        
    def download(self, url, filename):
        try:
            myfile = requests.get(url)
            with open(filename, 'wb') as file:
                file.write(myfile.content)
        except: #Skal man skrive sin egen exception?
            print('404')
        else:
            print('Success')
            
    def multiDownload(self, url_list):
        pass
            
    