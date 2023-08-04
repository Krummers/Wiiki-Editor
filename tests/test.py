import dotenv as de
import wiiki_editor as we

def write_file(file, info):
    txt = open(file, "w", encoding = "utf-8")
    txt.writelines(info)
    txt.close()

information = dict(de.dotenv_values("info.key"))
api = information["API"]
username = information["USERNAME"]
password = information["PASSWORD"]

wiiki = we.Wiiki(username, password, api)

lct = wiiki.article("List of Custom Tracks")
entry = we.Entry("[[Terrific Tanzania]]", "[[Krummers]]", "2023-08-04", "&mdash;")
lct.table += entry
wiiki.edit("Test", str(lct), "Test")
