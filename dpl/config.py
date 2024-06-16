import os
import configparser

def reader():
    file_path = os.path.join(os.getenv("appdata"),"dpl/dpl.ini")
    config = configparser.ConfigParser()
    config.read(file_path)
    if 'URL' in config:
        url = config['URL']['DEPLOYED_GAS']
        return url 
    else:
        return None

def writer(url): 
    file_path = os.path.join(os.getenv("appdata"),"dpl\dpl.ini")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    config = configparser.ConfigParser()
    config['URL'] = {}
    config['URL']['DEPLOYED_GAS'] = url
    with open(file_path, 'x') as configfile:
        config.write(configfile)