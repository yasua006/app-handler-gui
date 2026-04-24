def open_guarded(app_name: str, privilege_lvl: str):
    if app_name == "Finder" and privilege_lvl != "System".lower():
        return "Safe guard: cannot open Finder as 'User'. Switch privilege!"

def close_guarded(app_name: str):
    if app_name == "Finder":
        return "Safe guard: cannot close Finder!"
