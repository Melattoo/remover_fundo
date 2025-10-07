import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="Removedor de Fundo", page_icon="🖼️", layout="centered")

st.title("🖼️ Removedor de Fundo de Imagem")
st.write("Faça upload de uma foto e remova o fundo automaticamente!")

uploaded_file = st.file_uploader("Envie sua imagem aqui:", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    original_image = Image.open(uploaded_file)
    st.image(original_image, caption="Imagem Original", use_container_width=True)

    with st.spinner("Removendo fundo..."):
        img_bytes = io.BytesIO()
        original_image.save(img_bytes, format="PNG")
        result = remove(img_bytes.getvalue())
        result_image = Image.open(io.BytesIO(result))

    st.success("✅ Fundo removido com sucesso!")

    st.image(result_image, caption="Imagem Sem Fundo", use_container_width=True)

    buf = io.BytesIO()
    result_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="📥 Baixar imagem sem fundo",
        data=byte_im,
        file_name="imagem_sem_fundo.png",
        mime="image/png",
    )