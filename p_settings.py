import pip_load
pip_load.run()
from configparser import ConfigParser

def get(setting):
  config = ConfigParser()
  config.read("settings.ini")
  
  if setting == "user":
    return config.get("account","user")
    
  if setting == "pass":
    return config.get("account","pass")
    
  if setting == "files":
    return config.get("files","files")
