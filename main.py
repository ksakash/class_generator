from fastapi import FastAPI
from gen_app import create_class
from pydantic import BaseModel
import traceback
from fastapi.middleware.cors import CORSMiddleware

class CrawlerConfig(BaseModel):
    crawler_type: str
    site_name: str

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message":"Hello World!"}

def pascal_case(s):
    return "".join(x for x in s.title() if x.isalnum()) if type(s) == str else None

def snake_case(s):
    return "".join(x if x.isalnum() else "_" for x in s.lower()) if type(s) == str else None

def get_class_name(site_name, crawler_type):
    class_name = pascal_case(site_name)
    crawler_type = pascal_case(crawler_type)
    if class_name is None or crawler_type is None:
        raise Exception("Site name not string")
    return f"{class_name}{crawler_type}Crawler"

def get_file_name(site_name, crawler_type):
    file_name = snake_case(site_name)
    crawler_type = snake_case(crawler_type)
    if file_name is None or crawler_type is None:
        raise Exception("Site name not string")
    return f"{file_name}_{crawler_type}_crawler.py"

@app.post("/crawler_class")
def create_crawl_class(crawler_config: CrawlerConfig):

    try:
        crawler_type = crawler_config.crawler_type
        site_name = crawler_config.site_name
        class_name = get_class_name(site_name, crawler_type)
        class_filename = get_file_name(site_name, crawler_type)

        create_class(crawler_type, class_filename, class_name)
        return {"result": "Success"}
    except:
        return {"result": traceback.format_exc()}

