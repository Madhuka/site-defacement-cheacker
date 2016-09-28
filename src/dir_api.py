# Website Defacement Monitoring Tool
# code structure :: http://docs.python-guide.org/en/latest/writing/structure/


import fnmatch
import os
import os.path

from datetime import timedelta , datetime

import file
from application_logger import logger  as log


class DirAPI:
    # list files in dir and extension
    def list_file ( self , root_path , extension ):
        files_list = [ ] ;
        extension = "*" if (extension == 'none') else extension
        file_reg = '*.' + extension
        for root , dirnames , filenames in os.walk ( root_path ):
            for filename in fnmatch.filter ( filenames , file_reg ):
                path = os.path.join ( root , filename )
                info = os.stat ( path )
                last_modified_date = datetime.fromtimestamp ( info.st_mtime )
                last_access_date = datetime.fromtimestamp ( info.st_atime )
                size = info.st_size
                files_obj = file.Files ( filename , path , last_modified_date , last_access_date , size )
                files_list.append ( files_obj )
        log.info ( 'DirAPI: Total file count in ' + root_path + ' : ' + str ( len ( files_list ) ) )
        return files_list

    # liest files in dir and extension with recently modified
    def list_files_recently ( self , root_path , extension , hourcount ):
        file_list = [ ]
        files = self.list_file ( root_path , extension )
        hour_count = 1 if (hourcount == 0) else hourcount
        hours_behide_now = DirAPI ( ).get_behide_time ( hour_count )
        log.debug ( 'DirAPI: File list count in ' + root_path + ' : ' + str ( len ( files ) ) )
        for file in files:
            if (hours_behide_now < file.modified_date):
                file_list.append ( file )
                log.info ( file.path + ' is modified ' + str ( hour_count ) + ' hours ago' )
                log.debug ( file.path + ' is modified at ' + str ( file.modified_date ) )
        return file_list

    def get_behide_time ( self , hour_count ):
        current_datetime = datetime.now ( )
        hours_behide_now = current_datetime - timedelta ( hours=hour_count )
        log.info ( 'DirAPI: Get behide time ' + str ( hours_behide_now ) )
        return hours_behide_now

    def display_file_list ( self , file_list , description ):
        # value_when_true if condition else value_when_false
        ltr = 'are ' if (len ( file_list ) > 1) else 'is '
        log.info ( 'File API: There ' + ltr + str ( len ( file_list ) ) + ' files ' + description ) ;
        for file in file_list:
            log.info (description + ' ' + file.name)
