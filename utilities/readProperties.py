import configparser
import os.path

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir) + '\\configurations\\config.ini')


class Readconfig:
    @staticmethod
    def getApplicationUrl():
        url = (config.get('commonInfo', 'baseurl'))
        return url
    @staticmethod
    def getEmailId():
        email =(config.get('commonInfo','email_id'))
        return email
    @staticmethod
    def getpassword():
        password = (config.get('commonInfo', 'password'))
        return password


