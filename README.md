# 🛍️ Shopify Insights Fetcher Application

![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## 📌 Project Overview

The **Shopify Insights Fetcher Application** is a powerful tool that scrapes publicly available data from any Shopify-based e-commerce site without requiring Shopify’s official API. It allows users to explore rich metadata such as:

- Product catalogs
- Homepage highlights
- Policy information
- FAQs
- Social media handles
- Contact info
- Brand context

This app is ideal for **market researchers**, **analysts**, and **competitor insight teams** who want fast and flexible access to publicly available e-commerce data.

👉 **Live App:** [Explore the Deployed Application on Hugging Face Spaces](https://huggingface.co/spaces/KeshavaKumar/Shopify-Insights-Fetcher-Appliacation)

---

## 🚀 Key Features

- 🔎 Scrapes **homepage, product listings, FAQs, contact, and policy** pages.
- 💾 **SQL Database integration** for structured storage and querying.
- 📊 **Dynamic Data Display** with product titles, prices, and links.
- 🧠 Designed with **future AI integration** in mind (LLMs for insight extraction).
- 💡 Minimal, responsive, and user-friendly interface built using Gradio.

---

## 🧰 Tech Stack

| Layer           | Technology     |
|----------------|----------------|
| Frontend UI    | Gradio         |
| Backend Logic  | Python, FastAPI |
| Database       | SQLite         |
| Deployment     | Hugging Face Spaces |
| Hosting        | `spaces/Gradio` SDK |

---

## 🛠 How It Works

1. **User Input**: Enter a valid Shopify store URL.
2. **Scraping Module**: BeautifulSoup-based scraping system navigates key routes (`/products`, `/policies`, `/contact`, etc.).
3. **SQL Integration**: Parsed results are structured and stored in a SQLite database.
4. **Frontend Display**: Displayed in a tabular and clean format via Gradio UI.
5. **Download Option**: Users can **download the SQLite database** file for further analysis.

---

## 🖼 UI Preview

> 📌 *Screenshots of the deployed Hugging Face Space interface*

![App Screenshot 1](https://github.com/KeshavaKumarBoddepalli/Shopify-Insights-Fetcher/blob/main/Screenshot%202025-07-18%20170514.png)
![App Screenshot 2](https://github.com/KeshavaKumarBoddepalli/Shopify-Insights-Fetcher/blob/main/Screenshot%202025-07-18%20170627.png)

---

## 🧑‍💻 My Role & Contributions

- ✅ Designed and implemented the **complete data scraping pipeline**.
- ✅ Integrated **SQL database storage** and created **downloadable DB export**.
- ✅ Built a **user-friendly interface** with **Gradio** and deployed on **Hugging Face Spaces**.
- ✅ Managed edge cases like 404 errors, invalid Shopify domains, and missing fields.

---

## 🔮 Future Work

- 🤖 **LLM-Powered Insight Extraction**:
  - Integrate a large language model (LLM) to parse stored SQL data and generate natural language summaries.
  - For example: *“What’s the average price range of skincare products?”* → Automatically answered.
  
- 🔍 **Question-Answering Model Integration**:
  - Allow users to type natural questions, and the backend will query the SQLite database and return relevant insights.
  
- 🔗 **LLM Chat Interface**:
  - Implement a chat-based UI to interact with your Shopify data, powered by an open-source LLM like Mistral or Llama3.

---

## 🧪 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/KeshavaKumar/Shopify-Insights-Fetcher-Appliacation.git
cd Shopify-Insights-Fetcher-Appliacation

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
