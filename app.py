
import gradio as gr
import requests
import sqlite3
from datetime import datetime
import threading

API_URL = "https://KeshavaKumar-shopify-insights-fetcher2.hf.space/fetch_insights"

thread_local = threading.local()

def get_db_connection():
    if not hasattr(thread_local, "connection"):
        thread_local.connection = sqlite3.connect("insights.db", check_same_thread=False)
    return thread_local.connection

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS insights (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        timestamp TEXT,
        data TEXT
    )
    ''')
    conn.commit()

init_db()

def fetch_insights_from_url(shopify_url):
    try:
        response = requests.post(API_URL, json={"website_url": shopify_url})
        if response.status_code == 200:
            data = response.json()
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO insights (url, timestamp, data) VALUES (?, ?, ?)",
                           (shopify_url, datetime.now().isoformat(), str(data)))
            conn.commit()
            return data
        else:
            return {"error": f"Request failed: {response.status_code} - {response.text}"}
    except Exception as e:
        return {"error": str(e)}

def show_all_sql_data():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT url, timestamp, data FROM insights ORDER BY timestamp DESC")
        rows = cursor.fetchall()
        formatted = [{"url": url, "timestamp": timestamp, "data": eval(data)} for url, timestamp, data in rows]
        return formatted
    except Exception as e:
        return {"error": f"Failed to load from database: {str(e)}"}

with gr.Blocks() as demo:
    gr.Markdown("## 🛒 Shopify Insights Fetcher")

    with gr.Row():
        url_input = gr.Textbox(label="Enter Shopify Store URL")
        fetch_button = gr.Button("🔍 Fetch Store Insights")

    output_json = gr.JSON(label="Fetched Insights")

    fetch_button.click(fetch_insights_from_url, inputs=url_input, outputs=output_json)

    gr.Markdown("---")

    gr.Markdown("### 📜 View All Stored Insights")
    show_button = gr.Button("Show SQL Data")
    sql_output = gr.JSON(label="Stored Data")

    show_button.click(fn=show_all_sql_data, inputs=None, outputs=sql_output)

if __name__ == "__main__":
    demo.launch()
