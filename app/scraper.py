from bs4 import BeautifulSoup
import re
from .utils import get_html, get_json

def extract_products(website):
    json_data = get_json(f"{website.rstrip('/')}/products.json")
    return json_data.get("products", []) if json_data else []

def extract_home_products(html):
    soup = BeautifulSoup(html, 'lxml')
    product_tags = soup.find_all('a', href=re.compile("/products/"))
    hero_products = list({tag.text.strip() for tag in product_tags if tag.text.strip()})
    return hero_products

def extract_policies(website):
    policy_data = {}
    pages = ["privacy-policy", "refund-policy", "return-policy"]
    for page in pages:
        html = get_html(f"{website.rstrip('/')}/policies/{page}") or get_html(f"{website.rstrip('/')}/pages/{page}")
        if html:
            soup = BeautifulSoup(html, 'lxml')
            policy_data[page.replace('-', '_')] = soup.get_text(" ", strip=True)
    return policy_data

def extract_faq(html):
    soup = BeautifulSoup(html, 'lxml')
    faqs = []
    questions = soup.find_all(text=re.compile(r'\\?|faq', re.I))
    for q in questions:
        parent = q.parent if hasattr(q, 'parent') else None
        answer = parent.find_next_sibling() if parent else None
        if answer:
            faqs.append({"question": str(q).strip(), "answer": answer.get_text(strip=True)})
    return faqs

def extract_social_links(html):
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('a', href=True)
    socials = {}
    from bs4.element import Tag
    for tag in links:
        if isinstance(tag, Tag):
            href = tag.get('href')
            if href and 'instagram.com' in href:
                socials['instagram'] = href
            elif href and 'facebook.com' in href:
                socials['facebook'] = href
            elif href and 'tiktok.com' in href:
                socials['tiktok'] = href
    return socials

def extract_contact_details(html):
    emails = list(set(re.findall(r"[\\w\\.-]+@[\\w\\.-]+", html)))
    phones = list(set(re.findall(r"\\+?\\d[\\d\\s\\-]{8,}\\d", html)))
    return {"emails": emails, "phones": phones}

def extract_about(website):
    html = get_html(f"{website.rstrip('/')}/pages/about") or get_html(f"{website.rstrip('/')}/pages/about-us")
    if html:
        soup = BeautifulSoup(html, 'lxml')
        return soup.get_text(" ", strip=True)
    return None

def extract_important_links(html):
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('a', href=True)
    data = {}
    from bs4.element import Tag
    for tag in links:
        if isinstance(tag, Tag):
            text = tag.get_text(strip=True).lower()
            if 'track' in text:
                data['order_tracking'] = tag.get('href')
            elif 'blog' in text:
                data['blogs'] = tag.get('href')
            elif 'contact' in text:
                data['contact_us'] = tag.get('href')
    return data
