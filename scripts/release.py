from modules import script_callbacks, shared
import modules.sd_models as models
import modules.scripts as scripts
import gradio as gr
import torch
import gc

cleanNN = None

def refresh_LoRA():
    global cleanNN
    torch.nn.Linear.forward = cleanNN[0]
    torch.nn.Linear._load_from_state_dict = cleanNN[1]
    torch.nn.Conv2d.forward = cleanNN[2]
    torch.nn.Conv2d._load_from_state_dict = cleanNN[3]
    torch.nn.MultiheadAttention.forward = cleanNN[4]
    torch.nn.MultiheadAttention._load_from_state_dict = cleanNN[5]

def init_nn():
    global cleanNN
    cleanNN = [
        torch.nn.Linear.forward,
        torch.nn.Linear._load_from_state_dict,
        torch.nn.Conv2d.forward,
        torch.nn.Conv2d._load_from_state_dict,
        torch.nn.MultiheadAttention.forward,
        torch.nn.MultiheadAttention._load_from_state_dict
    ]

def mem_release():
    try:
        gc.collect()
        torch.cuda.empty_cache()
        torch.cuda.ipc_collect()
        gc.collect()
    
        if shared.opts.memre_dolora and shared.opts.memre_dolora is True:
            refresh_LoRA()

        if shared.opts.memre_debug and shared.opts.memre_debug is True:
            print('\nMemory Released!\n')

    except:
        if shared.opts.memre_debug and shared.opts.memre_debug is True:
            print('\n[Warning] Memory Release Failed...!\n')

def reload_models():
    models.unload_model_weights()
    mem_release()
    models.reload_model_weights()

class Script(scripts.Script):
    def __init__(self):
        global cleanNN
        if cleanNN is None:
            init_nn()

    def title(self):
        return "Memory Release"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with gr.Accordion('Memory Release', open=False):
            with gr.Row():
                release_button = gr.Button('🧹')
                reload_button = gr.Button('💥')

            release_button.click(fn=mem_release)
            reload_button.click(fn=reload_models)

        return None

    def postprocess(self, *args):
        mem_release()

def on_ui_settings():
    shared.opts.add_option("memre_debug", shared.OptionInfo(False, "Memory Release - Debug", section=("system", "System")))
    shared.opts.add_option("memre_dolora", shared.OptionInfo(False, "Memory Release - Refresh LoRA", section=("system", "System")))

script_callbacks.on_ui_settings(on_ui_settings)
