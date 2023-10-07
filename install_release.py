import os
import requests as rq
import subprocess as sp

def main():
    def read_file(file):
        txt = open(file, "r", encoding = "utf-8")
        info = txt.readlines()
        txt.close()
        return info
    
    def download_data(link, location):
        data = rq.get(link)
        
        with open(location, "wb") as k:
            k.write(data.content)
    
    # Get the latest version number
    
    download_data("https://test.pypi.org/project/wiiki-editor/", "version.txt")
    version = read_file("version.txt")[732].strip()
    os.remove("version.txt")
    
    # Install the new module twice
    for x in range(2):
        sp.run(["pip", "install", "-i", "https://test.pypi.org/simple/", "wiiki-editor=={}".format(version)])

if __name__ == "__main__":
    main()
