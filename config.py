import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7752144250:AAE7jCXlkzZiZui2MHykvWCMEfeKJixOeaQ")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21268963"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "60239424717807c61aa7e446d443984f")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5955963998"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ninja:QPDM7nUyksO69tg2@cluster0.2ae8l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "renamerbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
