import streamlit as st
import pandas as pd

st.title("E-commerce Chat Agent - Базова версія (Модуль 1)")

@st.cache_data
def load_products():
    try:
        # Рекомендую перевірити шлях до файлу
        return pd.read_csv('data/products.csv')
    except FileNotFoundError:
        st.error("Дані не знайдено. Запустіть генератор даних!")
        return pd.DataFrame()

products = load_products()

if products.empty:
    st.warning("Завантажте дані за допомогою scripts/generate_data.py")
else:
    st.sidebar.success(f"Завантажено {len(products)} продуктів")

# Ініціалізація історії чату
if "messages" not in st.session_state:
    st.session_state.messages = []

# Відображення історії чату (виправлено відступи)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Обробка нового вводу користувача
if prompt := st.chat_input("Запитайте про товари (наприклад, 'phone')"):
    # Додаємо повідомлення користувача в історію та показуємо його
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Пошук товарів
    query = prompt.lower()
    results = products[
        products['name'].str.lower().str.contains(query, na=False) |
        products['category'].str.lower().str.contains(query, na=False) |
        products['description'].str.lower().str.contains(query, na=False)
    ]

    # Формування відповіді
    if not results.empty:
        response = f"Знайдено {len(results)} товарів:\n\n"
        for _, row in results.head(5).iterrows():
            response += f"- **{row['name']}** ({row['category']}) - ${row['final_price']}\n  {row['description'][:150]}...\n\n"
    else:
        response = "Нічого не знайдено. Спробуйте інший запит!"

    # Додаємо відповідь асистента в історію та показуємо її
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
