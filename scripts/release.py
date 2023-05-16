import modules.scripts as scripts
import torch
import gc
import gradio as gr

class Script(scripts.Script):

    def __init__(self):
        pass

    def title(self):
        return "Memory Release"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with gr.Accordion('Memory Release', open=False):
            reload_button = gr.Button('🧹')

            def release():
                torch.cuda.empty_cache()
                gc.collect()

            reload_button.click(fn=release)

        return [reload_button]

    def postprocess(self, p, processed, *args):
        torch.cuda.empty_cache()
        gc.collect()
        return