from robocorp.tasks import task
from robocorp import browser

@task
def calculate_bmi():
    # a)
    # Konfiguroidaan selainajuri
    browser.configure(
        browser_engine="chromium",
        screenshot="only-on-failure",
        headless=False,
        slowmo=1000
    )

    # Avataan sivu ja otetaan kuvankaappaus
    page = browser.goto("https://rainekk.github.io/bmi/bmi.html")
    browser.screenshot()

    # b)
    # Täytetään pituus ja paino sekä painetaan "No"
    page.fill("#height", "175")
    page.fill("#weight", "81")
    page.click("#no")

    # c)
    # Täytetään kentät uudestaan ja painetaan "No"
    page.get_by_label("Height (cm):").fill("162")
    page.fill("//input[@id='weight']", "52")
    page.click("#no")

    # d)
    # Lisätään painoa 3 kg:lla ja painetaan "No"
    element = page.locator("#weight")
    weight = int(element.input_value())
    weight = weight + 3
    page.fill("#weight", str(weight))
    page.click("#no")

    # Haetaan viimeisin laskettu BMI-arvo muuttujaan bmi
    element = page.locator("#calculatedBMI > p")
    bmi = element.inner_text()
