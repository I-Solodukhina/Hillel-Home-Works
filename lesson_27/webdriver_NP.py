from playwright.sync_api import sync_playwright
from time import sleep


def main(track):
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=True)
        page = browser.new_page()
        page.goto('https://novaposhta.ua/')
        page.wait_for_load_state('networkidle')
        page.locator('.search_cargo_form > form:nth-child(1) > input:nth-child(2)').click()
        page.locator('#en').fill(track)
        sleep(1)
        page.locator('#np-number-input-desktop-btn-search-en').click()
        sleep(2)
        try:
            if page.locator('.header__status-text').count() > 0:
                if page.locator('.header__status-text').text_content().replace(' ', '').lower() == 'отримана':
                    return 'Посилка отримана'
                else:
                    return page.locator('.header__status-text').text_content()
            elif page.locator('.tracking__error-text').count() > 0:
                return page.locator('.tracking__error-text').text_content()
            elif page.locator('#np-number-input-desktop-message-error-message > span:nth-child(1)').count() > 0:
                return page.locator('#np-number-input-desktop-message-error-message > span:nth-child(1)').text_content()
            else:
                return 'Unknown error'
        except Exception as e:
            return e
        finally:
            browser.close()


if __name__ == '__main__':
    parcel = '20451004353678'
    print(main(parcel))
