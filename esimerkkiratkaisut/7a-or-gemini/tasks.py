from robocorp.tasks import task
from RPA.Robocorp.Vault import Vault
import google.generativeai as genai

_secret = Vault().get_secret("api-keys")
GEMINI = _secret["gemini"]

@task
def generate_quote():
    genai.configure(api_key=GEMINI)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Generate one motivational quote for IT experts")
    print(response.text)
