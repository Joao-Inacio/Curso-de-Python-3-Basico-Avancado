import os
from pathlib import Path
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()

ROOT_FOLDER = Path(__file__).parent
EDGEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'msedgedriver.exe'


def make_edge_browser(*options: str) -> webdriver.Edge:
    edge_options = webdriver.EdgeOptions()
    edge_options.headless = False

    if options is not None:
        for option in options:
            edge_options.add_argument(option)

    edge_service = webdriver.EdgeService(
        executable_path=EDGEDRIVER_EXEC
    )

    edge_browser = webdriver.Edge(
        service=edge_service,
        options=edge_options,
    )

    return edge_browser


if __name__ == '__main__':
    TIME_TO_WAIT = 15

    # Configurando o User-Agent para o Edge no Windows 11
    user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38"
    )

    options = (
        '--enable-chrome-browser-cloud-management',
        '--disable-blink-features=AutomationControlled',
        '--disable-gpu',
        '--disable-extensions',
        '--disable-infobars',
        '--disable-dev-shm-usage',
        '--no-sandbox',
        f'user-agent={user_agent}',
    )

    browser = make_edge_browser(*options)

    browser.get('https://www.ganharnasredes.com/painel/')

    try:
        search_popup = WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[2]/div/div/div[3]/button")
            )
        )
        search_popup.click()
        sleep(1)
        search_email = WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.presence_of_element_located(
                (  
                    By.XPATH,
                    "/html/body/div[1]/div/div/div[2]/div/form/div/div[1]/div/input"
                )
            )
        )
        search_email.send_keys(os.getenv('EMAIL_REDE'))
        sleep(1)
        search_email = WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/div[1]/div/div/div[2]/div/form/div/div[2]/div/input")
            )
        )
        search_email.send_keys(os.getenv('SENHA_REDE'))
        sleep(1)
        search_login = WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/div[1]/div/div/div[2]/div/form/div/div[3]/button")
            )
        )
        search_login.click()
        sleep(5)
        # browser.execute_script("window.open('https://www.ganharnasredes.com/painel/?pagina=sistema', '_blank');")
        # sleep(5)
        # browser.switch_to.window(browser.window_handles[0])
        # sleep(5)
        browser.get('https://www.ganharnasredes.com/painel/?pagina=sistema')
        # sleep(5)
        # browser.close()
        # sleep(5)
        # browser.switch_to.window(browser.window_handles[1])
        sleep(5)
        search_tipo_acoe = WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/div[1]/div/div/div/div/form/select[2]/option[3]")
            )
        )
        search_tipo_acoe.click()
        sleep(TIME_TO_WAIT)
    except:
        search_email = WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/div[1]/div/div/div[2]/div/form/div/div[1]/div/input")
            )
        )
        search_email.send_keys(os.getenv('EMAIL_REDE'))
        sleep(1)
        search_email = WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/div[1]/div/div/div[2]/div/form/div/div[2]/div/input")
            )
        )
        search_email.send_keys(os.getenv('SENHA_REDE'))
        sleep(1)
        search_login = WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/div[1]/div/div/div[2]/div/form/div/div[3]/button")
            )
        )
        search_login.click()
        sleep(TIME_TO_WAIT)
        search_acoe = WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/div[1]/aside/div/nav/ul/li[9]/center/a")
            )
        )
        search_acoe.click()
        search_tipo_acoe = WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/div[1]/div/div/div/div/form/select[2]/option[3]")
            )
        )
        search_tipo_acoe.click()
        sleep(TIME_TO_WAIT)
