# File: app.py
import gradio as gr
import requests

API_URL = "https://KeshavaKumar-shopify-insights-fetcher.hf.space/fetch_insights"

def fetch_insights_from_url(shopify_url):
    try:
        response = requests.post(API_URL, json={"website_url": shopify_url})

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Request failed with status {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": str(e)}

iface = gr.Interface(
    fn=fetch_insights_from_url,
    inputs=gr.Textbox(label="Enter Shopify Store URL"),
    outputs=gr.JSON(label="Shopify Insights"),
    title="Shopify Insights Fetcher",
    description="Paste a Shopify store URL to fetch product and brand details."
)

if __name__ == "__main__":
    iface.launch()
