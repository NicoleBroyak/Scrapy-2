from selenium import webdriver
import os
import itertools

class Scrapper():
        def __init__(self) -> None:
                self.scrapper = self.scrapper_init()


        def scrapper_init(self):
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--window-size=800,800')
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--disable-gpu')
                scrapper = webdriver.Chrome(options=chrome_options)
                return scrapper

        def reset_scrapper(self):
                self.scrapper.delete_all_cookies()
                self.scrapper.quit()
                self.scrapper = None
                self.scrapper = self.scrapper_init()

        def scrap_url_list(self, url: str):
                
                urls = list()
                self.scrapper.get(url)
                for i in itertools.count():
                        with open(f'page{i}.html', 'w') as file:
                                file.write(self.scrapper.page_source)
                        page = 'file://' + os.getcwd() + f'/page{i}.html'
                        urls.append(page)
                        try:
                                self.scrapper.find_element_by_partial_link_text('Next').click()
                        except:
                                self.reset_scrapper()
                                break
                return urls

scrap = Scrapper()