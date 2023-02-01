from environs import Env

env = Env()
env.read_env()

DEBUG = env.bool("DEBUG", default=False)
FULLSCREEN = env.bool("FULLSCREEN", default=True)

EMULATE_GPIO = env.bool("EMULATE_GPIO", default=False)
GPIO_TAP_PIN = env.int("GPIO_TAP_PIN")

LIGHTNING_BACKEND = env.str("LIGHTNING_BACKEND", default=None)

DELAY_AFTER_PAYMENT = env.int("DELAY_AFTER_PAYMENT", default=10)
TAP_TIME = env.int("TAP_TIME", default=0)
PRICE_IN_EUROCENTS = env.int("PRICE_IN_EUROCENTS")

LNBITS_BASE_URL = env.str("LNBITS_BASE_URL")
LNBITS_INVOICE_KEY = env.str("LNBITS_INVOICE_KEY")

NFC_PATH = env.str("NFC_PATH")
NFC_TARGETS = [
    x.strip(" ") for x in env.list("NFC_TARGETS", default=['106A', '106B', '212F'], subcast=str)
]

