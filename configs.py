# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "17822592"))
    API_HASH = getenv("API_HASH", "a20b3dbbe07ed695563b4609a3e62012")
    BOT_TOKEN = getenv("BOT_TOKEN", "0")
    FSUB = getenv("FSUB", "mtpmasala")
    CHID = int(getenv("CHID", "-1002059817947"))
    SUDO = list(map(int, getenv("SUDO", "578811855").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sagatobots00001:sagatobots100@cluster00001.vgdshkw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster00001")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
