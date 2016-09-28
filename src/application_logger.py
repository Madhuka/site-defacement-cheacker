import logging
import os.path

# logger handler
logger = logging.getLogger ( 'Defacement Checker' )
logger.setLevel ( logging.INFO )

# create console handler and set level to debug
ch = logging.StreamHandler ( )
ch.setLevel ( logging.DEBUG )

# create formatter
formatter = logging.Formatter ( '%(asctime)s - %(name)s - %(levelname)s - %(message)s' )

# add formatter to ch
ch.setFormatter ( formatter )

# add fh to logger
logger.addHandler ( ch )

def set_lof_file(log_dir_name):
    # log file handle
    dir_path = os.path.dirname ( os.path.realpath ( __file__ ) )
    log_dir = log_dir_name
    log_filename = 'application_log.log'
    log_file_dir = os.path.join ( dir_path , '..' , log_dir )
    if not os.path.exists ( log_file_dir ):
        os.makedirs ( log_file_dir )
    log_file_path = os.path.join ( dir_path , '..' , log_dir , log_filename )
    fh = logging.FileHandler ( log_file_path )
    fh.setLevel ( logging.DEBUG )
    fh.setFormatter ( formatter )
    # add fh to logger
    logger.addHandler ( fh )
