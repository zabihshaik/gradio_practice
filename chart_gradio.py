import pandas as pd
import gradio as gr

URL = "https://docs.google.com/spreadsheets/d/1UoKzzRzOCt-FXLLqDKLbryEKEgllGAQUEJ5qtmmQwpU/edit#gid=0"
csv_url = URL.replace('/edit#gid=', '/export?format=csv&gid=')


def get_data():
    return pd.read_csv(csv_url)


with gr.Blocks() as demo:
    gr.Markdown("# 📈 Real-Time Line Plot")
    with gr.Row():
        with gr.Column():
            gr.DataFrame(get_data, every=5)
        with gr.Column():
            gr.LinePlot(get_data, every=5, x="Date", y="Sales",
                        y_title="Sales ($ millions)", overlay_point=True, width=500, height=500)

demo.queue().launch()  # Run the demo with queuing enabled
