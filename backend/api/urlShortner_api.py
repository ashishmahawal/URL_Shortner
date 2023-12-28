from fastapi import APIRouter, Response, status
from utils.url_shorten_helper import URLShortenHelper
from utils.datastore_helper import SqlDB

url_shorten_router = APIRouter(
    prefix= "/v1/shorten",
    tags= ["URL shortner"]
)

url_shortner_helper = URLShortenHelper()
server_base_url = "http://squeezer/"
sqlHelper = SqlDB()

@url_shorten_router.post("/")
def create_short_url(url,response:Response,status_code=201):
    
    long_url = url
    res = sqlHelper.checkLongUrl(long_url)
    urlResponse = {
        "uid":None,
        "short_url":None,
        "long_url": None
    }
    if res is not None:
        urlResponse["uid"] = res[0]
        urlResponse["short_url"] = res[1]
        urlResponse["long_url"] = res[2]
        return urlResponse
    uid = url_shortner_helper.snowflakeId()
    short_url = server_base_url + url_shortner_helper.getBase62(uid)
    sqlHelper.putData(uid,short_url,long_url)
    response.status_code = status.HTTP_201_CREATED
    urlResponse["uid"] = uid
    urlResponse["short_url"] = short_url
    urlResponse["long_url"] = long_url
    return urlResponse

@url_shorten_router.get("/{short_url}")
def get_long_url(short_url:str):
    res = sqlHelper.getData(short_url)
    urlResponse = {
        "uid": res[0],
        "short_url": res[1],
        "long_url": res[2]
    }
    return urlResponse

