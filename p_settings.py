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

  def set(setting,val):
    config = ConfigParser()
    config.read("settings.ini")
    
   if setting == "user":
     return config.get("account","user",val)
      
   if setting == "pass":
     return config.get("account","pass",val)
    
   if setting == "files":
     return config.get("files","files",val)
