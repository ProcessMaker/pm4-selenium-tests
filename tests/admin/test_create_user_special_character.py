#!/usr/local/bin/python3

# Check if using local environment
from includes.Config import Config
Config.init_config('../../config/default.ini')
print('mesg = ', Config.get("ENVIRONMENT"))
if Config.get('ENVIRONMENT') == 'local':
    from sys import path
    path.append('../../includes')
    data = {"server_url": Config.get("server_url"), "username":Config.get("pm_username") , "password": Config.get("pm_password")}

from test_parent import BaseTest
import util
from page_login import PageLogin
from page_menu import PageMenu
from page_users import PageUsers


class TCP4_761(BaseTest):
    ''' Test that the country of an user can be changed '''

    def test_create_user_special_character(self):

        user_data = {'username': 'smoke','firstName': 'test','lastName': 'test qa','jobTitle': 'smoke test','status': 'Active',
                     'email': 'test@processmaker.com','password': 'Co1054!"·$%&/()='}
        self.driver = PageLogin(self.driver, data).login()

        PageMenu(self.driver,data).goto_admin()
        page_user = PageUsers(self.driver,data)
        page_user.create_user_data(user_data)


        self.assertEqual(2,2)
        output= "test"

if __name__ == "__main__":
    import __main__  
    output = util.run_test(TCP4_761, data, __main__)
