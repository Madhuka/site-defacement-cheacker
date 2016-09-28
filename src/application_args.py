import argparse


def get_args ( ):
    '''This function parses and return arguments passed in'''
    # Assign description to the help to the Website Defacement Monitoring Tool
    parser = argparse.ArgumentParser (
        description='Website Defacement Monitoring Tool' )
    # Add arguments
    parser.add_argument (
        '-e' , '--files_extension' , type=str , help='File extension' , required=False , default="none" )
    parser.add_argument (
        '-d' , '--website_location' , type=str , help='Path to web application' , required=False , default="." )
    parser.add_argument (
        '-t' , '--hour_count' , type=float , help='Loop back time in hour count' , required=False , default=0 )
    parser.add_argument (
        '-r' , '--recursive_directory' , type=bool , help='Recursive the directory' , required=False , default=False )
    parser.add_argument (
        '-l' , '--log_directory' , type=str , help='Directory name for the log' , required=False , default="log" )
    parser.add_argument (
        '-s' , '--skip_dir' , type=str , help='Skip directory name' , required=False , default="none" )
    parser.add_argument (
        '-c' , '--configuration_name' , type=str , help='Configuration name' , required=False , default="Default" )
    # Array for all arguments passed to script
    args = parser.parse_args ( )

    # Assign args to variables
    files_extension = args.files_extension
    website_dir_location = args.website_location
    hour_count = args.hour_count
    log_directory = args.log_directory
    recursive_directory = args.recursive_directory
    configuration_name = args.configuration_name
    skip_dir = args.skip_dir

    # Return all variable values
    # parser.print_help()

    return files_extension , website_dir_location , hour_count , log_directory , recursive_directory, \
           configuration_name, skip_dir,
