
class RegistrationPage:
    def __init__(self, page):
        self.page = page
        self.first_name_input = self.page.locator('#signupName')
        self.last_name_input = self.page.locator('#signupLastName')
        self.email_input = self.page.locator('#signupEmail')
        self.password_input = self.page.locator('#signupPassword')
        self.confirm_password_input = self.page.locator('#signupRepeatPassword')

    def enter_first_name(self, first_name):
        self.first_name_input.fill(first_name)

    def enter_last_name(self, last_name):
        self.last_name_input.fill(last_name)

    def enter_email(self, email):
        self.email_input.fill(email)

    def enter_password(self, password):
        self.password_input.fill(password)

    def enter_confirm_password(self, password):
        self.confirm_password_input.fill(password)
