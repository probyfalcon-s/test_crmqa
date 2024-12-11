from selenium.webdriver.common.by import By

class Locators:
    #___CREATE_ACCOUNT
    USERNAME_INPUT = By.XPATH, "//input[@placeholder='Username']"
    PASSWORD_INPUT = By.XPATH, "//div/input[@id='username_password']"
    SUBMIT_BUTTON = By.ID, "//input[@id='bigbutton']"
    ACCOUNTS_BUTTON = By.XPATH, "//a[@id='moduleTab_2_Accounts']"
    CREATE_ACCOUNT_BUTTON = By.XPATH, "//div[text()='Create Account']"
    NAME_INPUT = By.XPATH, "//input[@id='name']"
    PHONE_INPUT = By.XPATH, "//input[@id='phone_office']"
    SAVE_BUTTON = By.XPATH, "//input[@title='Save']"
    SUCCESS_NAME_ACCOUNT = By.XPATH, "//h2[text()=' name_auto ']"
    #___CREATE_LEADS
    CREATE_LEADS_BUTTON = By.XPATH, "//div[text()='Create Lead']"
    LEADS_BUTTON = By.XPATH, "//a[@id='moduleTab_2_Leads']"
    NAME_LEADS_INPUT = By.XPATH, "//input[@id='first_name']"
    LASTNAME_LEADS_INPUT = By.XPATH, "//input[@id='last_name']"
    PHONE_LEADS_INPUT = By.XPATH, "//input[@id='phone_work']"
    SUCCESS_NAME_LEADS = By.XPATH, "//h2[text()=' name_leads ']"
    #____ADD_LEADS_ACCOUNT
    TAB_NAME_ACCOUNT = By.XPATH, "//span[text()='name_auto']"
    OPEN_LEADS_BUTTON = By.XPATH, "//a[@id='subpanel_title_leads']"
    SELECT_CHANGE_CREATE = By.XPATH, "//a[@id='account_leads_create_button']"
    SELECT_CHANGE_SELECT = By.XPATH, "//a[@id='account_leads_select_button']"
    ADD_LEADS_BUTTON = By.XPATH, "//a[text()='Rob Dougan']"


