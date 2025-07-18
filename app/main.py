from fastapi import FastAPI, HTTPException
from .models import StoreRequest
from .utils import get_html
from .scraper import (
    extract_products,
    extract_home_products,
    extract_policies,
    extract_faq,
    extract_social_links,
    extract_contact_details,
    extract_about,
    extract_important_links,
)

app = FastAPI()

@app.post("/fetch_insights")
async def fetch_insights(req: StoreRequest):
    website = req.website_url.strip().rstrip('/')

    html = get_html(website)
    if html is None:
        raise HTTPException(status_code=401, detail="Website not found or not accessible")

    try:
        products = extract_products(website)
        hero_products = extract_home_products(html)
        policies = extract_policies(website)
        faqs = extract_faq(html)
        socials = extract_social_links(html)
        contact = extract_contact_details(html)
        about = extract_about(website)
        links = extract_important_links(html)

        result = {
            "brand_name": website.replace("https://", "").replace("http://", "").split(".")[0],
            "product_catalog": products,
            "hero_products": hero_products,
            **policies,
            "faqs": faqs,
            "social_handles": socials,
            "contact_info": contact,
            "brand_about": about,
            "important_links": links
        }

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
