import dotenv as de
import wiiki_editor as we

def write_file(file, info):
    txt = open(file, "w", encoding = "utf-8")
    txt.writelines(info)
    txt.close()
    
def read_file(file):
    txt = open(file, "r", encoding = "utf-8")
    info = txt.readlines()
    txt.close()
    return info

information = dict(de.dotenv_values("info.key"))
api = information["API"]
username = information["USERNAME"]
password = information["PASSWORD"]

wiiki = we.Wiiki(username, password, api)

lrog = wiiki.article("List of Retro Tracks from Non-Mario Kart Games")

wiiki.edit(lrog.title, str(lrog), "Sorted list")
