from robocorp.tasks import task
from robocorp import windows

@task
def calculator_task():
    # Avataan Laskin.
    windows.desktop().windows_run(f"calc.exe")

    # Haetaan pointteri Laskin-ikkunaan
    calc = windows.find_window("name:Laskin")

    # Painetaan Laskin-ikkunassa painiketta "1"
    button = calc.find('automationid:"num1Button"')
    button.click()

    # Painetaan Laskin-ikkunassa painiketta "C"
    button = calc.find('automationid:"clearButton"')
    button.click()

    # Lähetään näppäimenpainalluksia Laskimeen
    calc.send_keys(keys="96+4=")

    # Suljetaan ikkuna
    calc.close_window()
