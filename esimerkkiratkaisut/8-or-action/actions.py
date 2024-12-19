"""
A simple AI Action.

See:
https://github.com/sema4ai/actions/blob/master/README.md

"""

import os
from sema4ai.actions import action
from robocorp import browser

HEADLESS_BROWSER = not os.getenv("HEADLESS_BROWSER")

@action
def calculate_BMI(height:str, weight:str) -> str:
    """
    Calculates BMI.

    Args:
        height: Height in cm.
        weight: Weight in kg.
    """
    # Konfigutoidaan selainajuri
    browser.configure(browser_engine="chromium", headless=HEADLESS_BROWSER)

    # Tai selainikkuna näkyvillä ja hidatettuna
    '''
    browser.configure(
        browser_engine="chromium",
        headless=False,
        slowmo=2000
    )
    '''

    # Avataan BMI-laskurisivu, täytetään kentät ja painetaan No
    page = browser.goto("https://rainekk.github.io/bmi/bmi.html")
    page.fill("#height", height)
    page.fill("#weight", weight)
    page.click("#no")

    # Haetaan laskettu BMI-arvo muuttujaan
    element = page.locator("#calculatedBMI > p")
    bmi = element.inner_text()

    # Tulostetaan ja palautetaan bmi
    print (bmi)
    return bmi

@action
def get_wikipedia_article_summary(article_url: str) -> str:
    """
    Retrieves the summary (first paragraph) of given Wikipedia article.

    Args:
        article_url: URL of the article to get the summary of.

    Returns:
        Summary of the article.
    """

    browser.configure(browser_engine="chromium", headless=HEADLESS_BROWSER)

    page = browser.goto(article_url)

    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")

    paragraphs = page.query_selector_all('.mw-content-ltr>p:not(.mw-empty-elt)')
    summary = paragraphs[0].inner_text()

    # Pretty print for log
    print(summary)

    return summary