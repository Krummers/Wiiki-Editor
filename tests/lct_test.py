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

lct.table += we.LCTEntry("[[Back_RM_Race]]", "[[TheGamingBram]]", "2023-09-10", "&mdash;")
lct.table += we.LCTEntry("[[Drift Ridge]]", "[[TheGamingBram]]", "2023-09-10", "&mdash;")
lct.table += we.LCTEntry("[[Rocky Rocky Loop]]", "[[TheGamingBram]]", "2023-09-10", "&mdash;")
lct.table += we.LCTEntry("[[Painted Swamp Circuit]]", "[[TheGamingBram]]", "2023-09-10", "&mdash;")
lct.table += we.LCTEntry("[[Sparkling Pass]]", "[[EpicCrossover]]", "2023-09-10", "&mdash;")
lct.table += we.LCTEntry("[[Torpedo Ship]]", "ignis", "2023-09-10", "&mdash;")

# wiiki.edit(lct.title, str(lct), "Added some new custom tracks.")
