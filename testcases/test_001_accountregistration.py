from pageobjects import Homepage
from pageobjects import Accountregistration
class test_accountreg:
    BaseUrl="https://demo.opencart.com/"

    def test_account(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.hp = Homepage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.regpage = Accountregistration(self.driver)

        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        #self.email = randomeString.random_string_generator() + '@gmail.com'
        self.regpage.setEmail("shreeteja355@gmail.com")
        #self.regpage.setEmail(self.email)
        self.regpage.setTelephone("65656565")
        self.regpage.setPassword("abcxyz")
        self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg = self.regpage.getconfirmationmsg()
        self.driver.close()
        if self.confmsg == "Your Account Has Been Created!":
         assert True
        else:
         assert False

