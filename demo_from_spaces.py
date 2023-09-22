import gradio as gr

with gr.Blocks() as demo:
    with gr.Tab("Translate to Spanish"):
        gr.load("gradio/helsinki_translation_en_es", src="spaces")
    with gr.Tab("Translate to French"):
        gr.load("abidlabs/en2fr", src="spaces")

demo.launch()
