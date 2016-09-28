import os.path

import application_args as args
import application_logger  as applog
import dir_api as dirapi
import email_api as email
import file_api as fileapi
from application_logger import logger  as log

# Run application_args
# get_args()
# Match return values from get_arguments()
# and assign to their respective variables
def start ( ):
    files_extension , website_dir_location , hour_count , log_directory , recursive_directory , \
    configuration_name, skip_dir = args.get_args ( )
    status ( files_extension , website_dir_location , hour_count , log_directory ,
             recursive_directory, configuration_name )
    applog.set_lof_file ( log_directory )
    dir_path = os.path.dirname ( os.path.realpath ( __file__ ) )
    if (website_dir_location != '.'):
        if os.path.exists ( website_dir_location ):
            dir_path = website_dir_location
            log.info ( 'Directory is updated to ' + dir_path )
        else:
            log.error ( dir_path + ' directory is not existing' )
    if (recursive_directory):
        current_api = dirapi.DirAPI ( )
        log.info ( 'API is updated to DirAPI' )
    else:
        current_api = fileapi.FileAPI ( ) ;
        log.info ( 'API is updated to FileAPI' )

    if (files_extension != 'none' and hour_count == 0):
        log.info ( 'Searching dir for files extension ' + files_extension )
        file_list = filter_file_list ( current_api.list_file ( dir_path , files_extension ) , skip_dir )
        current_api.display_file_list ( file_list , files_extension + ' extension' )

    if (files_extension == 'none' and hour_count == 0):
        file_list = current_api.list_file ( dir_path , files_extension )
        log.info ( 'Searching dir for all files ' )
        file_list = filter_file_list ( file_list , skip_dir )
        current_api.display_file_list ( file_list , 'existing' )

    if (files_extension == 'none' and hour_count != 0):
        log.info ( 'Searching dir for recent modified files ' )
        file_list = filter_file_list (
            current_api.list_files_recently ( dir_path , files_extension , hour_count ) , skip_dir )
        current_api.display_file_list ( file_list , 'modified' )
        sending_notifications( file_list, configuration_name )

    if (files_extension != 'none' and hour_count != 0):
        log.info ( 'Searching dir with files extension and recent modified files' )
        file_list = current_api.list_files_recently ( dir_path , files_extension , hour_count )
        current_api.display_file_list ( file_list , 'modified and it has ' + files_extension + ' extension' )
        sending_notifications ( file_list, configuration_name )


def status ( files_extension , website_dir_location , hour_count , log_directory , recursive_directory, conf_name ):
    log.info ( 'Files extension: ' + files_extension )
    log.info ( 'Website Directory location: ' + website_dir_location )
    log.info ( 'Hour count: ' + str ( hour_count ) )
    log.info ( 'Log Dir: ' + log_directory )
    log.info ( 'Recursive Directory: ' + str ( recursive_directory ) )
    log.info ( 'Configuration Name: ' + str ( conf_name ) )


def filter_file_list ( file_list , skip_dir ):
    filted_list = skip_dir_name ( file_list , skip_dir )
    return filted_list

def sending_notifications ( file_list, configuration_name ):
    if(len(file_list)>0):
        log.info ( 'Building the emails by ' + configuration_name )
        email.EmailAPI ( ).send_mail ( file_list, configuration_name )
    else:
        log.info( 'There is no notifications on '+ configuration_name)


def skip_dir_name ( file_list , skip_dir ):
    n = len ( file_list ) - 1
    i = 0
    while i <= n:
        file = file_list[ i ]
        i = i + 1
        if skip_dir in file.path:
            folder_list = str ( file.path ).split ( '\\' )
            for folder in folder_list:
                if (skip_dir == folder):
                    file_list.remove ( file )
                    i = i - 1
                    n = n - 1
    return file_list


start ( )
