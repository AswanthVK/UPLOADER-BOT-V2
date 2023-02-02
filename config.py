import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1823808722:AAFlWM_qHhQbClnWzWHPD3mSCQlCDVVOFd8")
    
    API_ID = int(os.environ.get("API_ID", "663122"))
    
    API_HASH = os.environ.get("API_HASH", "23dac54b523173b5f83014ae566584bd"")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "662933911"))

    SESSION_NAME = "SuperDLBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://aswanthvk:aswanthvk@cluster0.ul7sp2m.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
