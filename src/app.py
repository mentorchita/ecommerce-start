# src/app.py
import streamlit as st
import pandas as pd

st.title("E-commerce Chat Agent - Базова версія (Модуль 1)")

@st.cache_data
def load_products():
    try:
        return pd.read_csv('data/products.csv')
    except FileNotFoundError:
        st.error("Дані не знайдено. Запустіть генератор даних!")
        return pd.DataFrame()

products = load_products()

if products.empty:
    st.warning("Завантажте дані за допомогою scripts/generate_data.py")
else:
    st.success(f"Завантажено {len(products)} продуктів")

# Історія чату
if "messages" not in st.session_state:
    st.session_state.messages = []
    for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Запитайте про товари (наприклад, 'навушники до 2000 грн')"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    query = prompt.lower()
    results = products[
        products['name'].str.lower().str.contains(query) |
        products['category'].str.lower().str.contains(query) |
        products['description'].str.lower().str.contains(query)
    ]

    if not results.empty:
        response = f"Знайдено {len(results)} товарів:\n\n"
        for _, row in results.head(5).iterrows():
            response += f"- **{row['name']}** ({row['category']}) - ${row['final_price']}\n  {row['description'][:150]}...\n\n"
    else:
        response = "Нічого не знайдено. Спробуйте інший запит!"

    for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Запитайте про товари (наприклад, 'навушники до 2000 грн')"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    query = prompt.lower()
    results = products[
        products['name'].str.lower().str.contains(query) |
        products['category'].str.lower().str.contains(query) |
        products['description'].str.lower().str.contains(query)
    ]

    if not results.empty:
        response = f"Знайдено {len(results)} товарів:\n\n"
        for _, row in results.head(5).iterrows():
            response += f"- **{row['name']}** ({row['category']}) - ${row['final_price']}\n  {row['description'][:150]}...\n\n"
    else:
        response = "Нічого не знайдено. Спробуйте інший запит!"

    st.session_state.messages.append({"role": "assistant", "content": response})
    
