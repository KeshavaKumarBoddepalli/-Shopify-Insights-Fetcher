from pydantic import BaseModel

class StoreRequest(BaseModel):
    website_url: str
