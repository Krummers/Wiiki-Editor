import os
import platform as pf
import requests as rq
import shutil as sh
import subprocess as sp

def read_file(file):
    txt = open(file, "r", encoding = "utf-8")
    info = txt.readlines()
    txt.close()
    return info

def rewrite_line(file, index, line):
    txt = open(file, "r", encoding = "utf-8")
    l = txt.readlines()
    txt.close()
    
    l[index - 1] = line
    
    txt = open(file, "w", encoding = "utf-8")
    txt.writelines(l)
    txt.close()

def download_data(link, location):
    data = rq.get(link)
    
    with open(location, "wb") as k:
        k.write(data.content)

def main():
    # Get the latest version number
    
    download_data("https://test.pypi.org/project/wiiki-editor/", "version.txt")
    version = read_file("version.txt")[227]
    version = version[version.rfind(" ") + 1:-1]
    os.remove("version.txt")
    
    # Bump the patch version number
    
    patch_version = int(version[version.rfind(".") + 1:]) + 1
    version = version[:version.rfind(".") + 1] + str(patch_version)
    
    rewrite_line("pyproject.toml", 7, "version = \"{}\"\n".format(version))
    
    # Upload new module to the server
    
    api = read_file("api_token.txt")[0]
    
    if pf.uname()[0] == "Windows":
        commands = [["py", "-m", "build"], \
        ["py", "-m", "twine", "upload", "--repository", "testpypi", "dist/*", "--username", "__token__", "--password", api]]
    else:
        commands = [["python3", "-m", "build"], \
        ["python3", "-m", "twine", "upload", "--repository", "testpypi", "dist/*", "--username", "__token__", "--password", api]]
    
    if os.path.exists("dist"):
        sh.rmtree("dist")
    
    for command in commands:
        sp.run(command)

if __name__ == "__main__":
    main()
