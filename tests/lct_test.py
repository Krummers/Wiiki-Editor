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

lct = wiiki.article("List of Custom Tracks")
for name in ["Krummers", "KantoEpic", "Trainiax", "Atlas", "Bruh de la Boi"]:
    entry = we.LCTEntry("[[1-1 but it's in Mario Kart Wii]]", "[[{}]]".format(name), "2023-08-04", "&mdash;")
    lct.table += entry
lct.table.update_release("[[1-1 but it's in Mario Kart Wii]]", "2023-08-08", "[[Atlas]]")
lct.table.update_release("[[10 Jumps to Victory]]", "2023-08-09")
lct.table.sort()
wiiki.edit("Test", str(lct), "Test")
