import modules.scripts as scripts
import modules.devices as devices
import gc
import gradio as gr

def mem_release(debug = True):
    try:
        gc.collect()
        devices.torch_gc
        gc.collect()

        if debug == True:
            print('\n Memory Released!\n')

    except:
        if debug == True:
            print('\n\n Memory Release Failed...!\n\n')

class Script(scripts.Script):

    def title(self):
        return "Memory Release"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with gr.Accordion('Memory Release', open=False):
            with gr.Row():
                reload_button = gr.Button('🧹')
                reload_button.click(fn=mem_release)

                debug = gr.Checkbox(label='Debug')

        return [debug]

    def postprocess(self, p, processed, debug:bool):
        mem_release(debug)
        return None