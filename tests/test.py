import dotenv as de
import wiiki_editor as we

info = dict(de.dotenv_values("info.key"))
api = info["API"]
username = info["USERNAME"]
password = info["PASSWORD"]

wiiki = we.Wiiki(username, password, api)
