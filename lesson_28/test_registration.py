import pytest
from faker import Faker

fake = Faker()
first_name = "TestUser"
last_name = "User"
email = fake.email(domain='example.com')
password = "Password123"


def test_registration(wd):
	# Введення даних
	wd.enter_first_name(first_name)
	wd.enter_last_name(last_name)
	wd.enter_email(email)
	wd.enter_password(password)
	wd.enter_confirm_password(password)
	wd.page.locator("button[class='btn btn-primary']").click()
	assert wd.page.url == "https://guest:welcome2qauto@qauto2.forstudy.space/"
	