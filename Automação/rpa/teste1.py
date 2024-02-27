from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

nav = webdriver.Chrome(options=options)

nav.get("https://farmoquimicasa.sharepoint.com/sites/portalfqm/Pages/home.aspx")