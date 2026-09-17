import streamlit as st
import random
 
st.set_page_config(page_title="Мій Супер-Додаток", layout="wide")
 
st.title("Ласкаво просимо до мого додатку! 🚀")
 
tab1, tab2, tab3 = st.tabs(["Про мене", "Мій Інструмент", "🔗 Корисні посилання"])
with tab1:
    st.header("Знайомство з автором")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://thumb.wikimedia.org/wikipedia/commons/thumb/5/59/User-avatar.svg/1280px-User-avatar.svg.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail", width=200)
    with col2:
        st.subheader("Привіт, я майбутній Python Developer!")
        st.write("Я навчаюсь в Малій Комп`ютерній Академії IT STEP. Створюю круті веб-додатки та вивчаю штучний інтелект.")
 
        with st.container():
            st.info("Контакти для зв`язку.")
            st.markdown("- GitHub: [](https://github.com)")
            st.markdown("- Email: xxxxxxxx@itstep.org")
 
with tab2:
    st.header("Корисний Інструмент: Конвертор температури")
    st.write("Цей інструмент допоможе швидко перевести градуси Цельсій у Фаренгейти.")
    c1, c2 = st.columns(2)
    with c1:
        cl1 = st.text_input("Введите число цельсие")
        result = st.button("Перевести")
        
        
        if 'secret_number' not in st.session_state:
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0
            st.session_state.game_over = False
 
        st.subheader("🎲 Гра: Вгадай число від 1 до 100")
    
        user_guess = st.number_input("Твій варіант:", min_value=1, max_value=100, step=1)
    
        if st.button("Перевірити"):
            st.session_state.attempts += 1
            if user_guess < st.session_state.secret_number:
                st.info("📈 Загадане число БІЛЬШЕ!")
            elif user_guess > st.session_state.secret_number:
                st.info("📉 Загадане число МЕНШЕ!")
            else:
                st.success(f"🎉 Перемога! Ти вгадав число {st.session_state.secret_number} за {st.session_state.attempts} спроб!")
                st.session_state.game_over = True
                
        if st.button("Зіграти знову"):
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0
            st.session_state.game_over = False
            st.rerun()

    with c2:
        if result:
            cl = float(cl1)
            f1 = (cl * 9/5) + 32
            st.success(f"{cl} градусов ровно {f1} франгейтов")
    

with tab3:
    c1, c2 = st.columns(2)
    with c1:
        
        st.subheader("🔗 Посилання")
        st.markdown("""
                    * ⭐ [Python](https://www.python.org/) - завантажити пайтон
                    * 💎 [Gemini](https://gemini.google.com) - ші геміні
                    """)
    with c2:
        
        st.subheader("⚽ Ігри")
        st.markdown("""
                    * ❤️ [Steam](https://store.steampowered.com) - багато ігор
                    * ⛏️ [Minecraft](https://www.minecraft.net/ru-ru) - майнкрафт
                    * ⛏️ [Minecraft](https://www.minecraft.net/ru-ru) - майнкрафт
                    """)
