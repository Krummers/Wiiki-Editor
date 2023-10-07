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

# lrog.tracks += we.LROGEntry("Flower Road", "FGKR", \
#                             "''[[wikipedia:Family Go-Kart Racing|Family Go-Kart Racing]]''", \
#                             "{{yes|Cool20}}", "2023-08-28", "&mdash;")
# lrog.tracks += we.LROGEntry("Happy Up-Down", "FGKR", \
#                             "''[[wikipedia:Family Go-Kart Racing|Family Go-Kart Racing]]''", \
#                             "{{yes|Cool20}}", "2023-08-28", "&mdash;")

wiiki.edit(lrog.title, str(lrog), "Added two new tracks.")
