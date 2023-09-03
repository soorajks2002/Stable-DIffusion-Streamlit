import streamlit as st
import stable_diffusion_2
import stable_diffusion_xl_base_1
import stable_diffusion_xl_refiner_1
from PIL import Image

favicon = Image.open('favicon.ico')
st.set_page_config(page_title="Stable Diffusion", page_icon=favicon)

st.title("Stable Diffusion")

form = st.form("Input Form")

sd_models = ["Stable Diffusion 2", "Stable Diffusion XL Base 1", "Stable Diffusion Xl Refiner 1"]
sd_model_map = {sd_models[0]:stable_diffusion_2, sd_models[1]:stable_diffusion_xl_base_1, sd_models[2]:stable_diffusion_xl_refiner_1}

prompt = form.text_input("Enter prompt for image generation...")
model = form.radio("Select stable diffusion model", sd_models)

if form.form_submit_button("Generate Image") :
    if prompt == "":
        form.error("Please enter a valid prompt")
        
    else :
        with st.spinner("Generating Image...") :
            generated_output = sd_model_map[model].generate_image(prompt) 
            if generated_output["generation_successful"] :
                st.image(generated_output["image"])
            else :
                st.info(f"{model}'s Hugging Face Inference is BUSY !!")