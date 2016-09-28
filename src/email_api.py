import errno
import smtplib
import time
from email.mime.text import MIMEText
from socket import error as socket_error
from application_logger import logger  as log
from application_config import ConfigSectionMap as config


# sending emial
class EmailAPI:
    def send_mail ( self , files_list , config_name ):
        site_name = config ( config_name )[ 'siteurl' ]
        localtime = time.asctime ( time.localtime ( time.time ( ) ) )

        mail_from = config ( "Email" )[ 'from' ]
        to_list = config ( config_name )[ 'to' ]
        # setting mime
        text_msg = 'Dear Sir / Madam,\n\nWeb site \'' + site_name + '\' has modified recently'
        for file in files_list:
            text_msg += '\n\t- ' + file.name + ' has modified at ' + str ( file.modified_date )
        foot_text = '\n\n--\nThanks,\nDefacement Checker,\n'
        foot_text += str(config ( "Email" )[ 'signature' ])
        text_msg += foot_text
        msg = MIMEText ( text_msg )
        title = config ( "Email" )[ 'appname' ]
        msg[ 'Subject' ] = '[' + title + '] ' + site_name + ' Site is Modified'
        msg[ 'Date' ] = localtime
        msg[ 'From' ] = mail_from
        msg[ 'To' ] = to_list
        try:
            # Send the message via our own SMTP server, but don't include the
            # envelope header.
            s = smtplib.SMTP ( config ( "Email" )[ 'server' ] )
            send_to_list = to_list.split ( ',' )
            s.sendmail ( mail_from , send_to_list , str ( msg ) )
            s.quit ( )
            log.info('Email is sent')
        except socket_error as serr:
            log.error('Issue with connecting to email server '+config ( "Email" )[ 'server' ])
            print 'serr'
            if serr.errno == errno.EFAULT:
                log.error ( 'Fault in Email Server' )
                # Not the error we are looking for, re-raise
                #raise serr
        except smtplib.SMTPServerDisconnected:
            log.error ( 'SMTP Server ' + config ( "Email" )[ 'server' ] + 'Disconnected' )
# EmailAPI().send_mail(['sss'],'NIC');
