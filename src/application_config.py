import ConfigParser
import os.path

from application_logger import logger  as log

SETTING_FILE = 'settings.ini'

Config = ConfigParser.ConfigParser()
dir_path = os.path.dirname ( os.path.realpath ( __file__ ) )
config_path = os.path.join(dir_path,'..',SETTING_FILE)
Config.read(config_path)

def ConfigSectionMap(section):
    dict1 = {}
    try:
        options = Config.options(section)
        for option in options:
            try:
                dict1[option] = Config.get(section, option)
                if dict1[option] == -1:
                    print ("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
    except ConfigParser.NoSectionError:
        log.error('Config setection did not found '+ section)
    except ConfigParser.NoOptionError:
        log.error('Config Option did not found ' + option + ' in ' + section)
    except KeyError:
        log.error ( 'Config Key loading issue ' + option )
    except ConfigParser.Error:
        log.error ( 'Issue in Config loading ' + ConfigParser.Error.message)
    return dict1