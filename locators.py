from selenium.webdriver.common.by import By


class TestLocators:
    personal_account_button = By.XPATH, './/p[text()="Личный Кабинет"]'  # Кнопка "Личный кабинет"
    constructor_button = By.XPATH, './/p[text()="Конструктор"]'  # Кнопка "Конструктор"
    login_button = By.XPATH, '//button[contains(text(), "Войти")]'  # Кнопка входа в аккаунт
    logout_button = By.XPATH, '//button[contains(text(), "Выход")]' # Кнопка "Выход"
    sign_up_button = By.XPATH, './/button[text()="Зарегистрироваться"]'  # Кнопка "Зарегистрироваться"
    login_link = By.XPATH, './/a[text()="Войти"]' # Гиперссылка "Войти"
    reset_password_link = By.XPATH, './/a[text()="Восстановить пароль"]'  # Гиперссылка "Восстановить пароль"
    name_input_box = By.XPATH, './/label[text()="Имя"]/following-sibling::input' # Текстовое поле для ввода имени
    email_input_box = By.XPATH, './/label[text()="Email"]/following-sibling::input'  # Текстовое поле для ввода электронной почты
    password_input_box = By.XPATH, './/label[text()="Пароль"]/following-sibling::input'  # Текстовое поле для ввода пароля
    header_logo = By.XPATH, './/div[contains(@class, "header__logo")]'  # Логотип "Stellar Burgers"
    sauces_tab = By.XPATH, ".//span[(@class = 'text text_type_main-default' and text()='Соусы')]/parent::div"  # Таба с соусами
    buns_tab = By.XPATH, ".//span[(@class = 'text text_type_main-default' and text()='Булки')]/parent::div"  # Таба с булками
    toppings_tab = By.XPATH, ".//span[(@class = 'text text_type_main-default' and text()='Начинки')]/parent::div"  # Таба с начинками
    invalid_password_error = By.XPATH, ".//p[contains(text(), 'Некорректный пароль')]" #  Валидационное сообщение о некорректном пароле
