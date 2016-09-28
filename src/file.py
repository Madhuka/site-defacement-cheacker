class Files:
    '''
    size - size of file(bytes)
    recent_access - time of most recent access
    modified_date - time of most recent content modification
    '''

    def __init__ ( self , name , path , modified_date , recent_access , size ):
        self.name = name
        self.path = path
        self.modified_date = modified_date
        self.recent_access = recent_access
        self.size = size

    def get_name ( self ):
        return self.name
