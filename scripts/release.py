from modules import script_callbacks, shared
import modules.sd_models as models
import modules.scripts as scripts
import gradio as gr
import torch
import gc

def mem_release():
    try:
        gc.collect()
        torch.cuda.empty_cache()
        torch.cuda.ipc_collect()
        gc.collect()

        if getattr(shared.opts, 'memre_debug', False):
            print('\nMemory Released!\n')

    except:
        if getattr(shared.opts, 'memre_debug', False):
            import traceback
            traceback.print_exc()

def reload_models():
    models.unload_model_weights()
    mem_release()
    models.send_model_to_device(shared.sd_model)

class Script(scripts.Script):

    def title(self):
        return "Memory Release"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with gr.Accordion('Memory Release', open=False):
            gr.Markdown('<h5 style="float: left;">Garbage Collect</h4> <h4 style="float: right;">Flush Checkpoint Memory</h5>')
            with gr.Row():
                release_button = gr.Button('🧹')
                reload_button = gr.Button('💥')

            release_button.click(fn=mem_release)
            reload_button.click(fn=reload_models)

    def setup(self, *args):
        if getattr(shared.opts, 'memre_unload', False):
            models.send_model_to_device(shared.sd_model)

    def postprocess_batch(self, *args, **kwargs):
        mem_release()

    def postprocess(self, *args):
        if getattr(shared.opts, 'memre_unload', False):
            models.unload_model_weights()

        mem_release()

def on_ui_settings():
    shared.opts.add_option("memre_debug", shared.OptionInfo(False, "Memory Release - Debug", section=("system", "System")))
    shared.opts.add_option("memre_unload", shared.OptionInfo(False, "Memory Release - Unload Checkpoint after Generation", section=("system", "System")).info('Same as ComfyUI'))

script_callbacks.on_ui_settings(on_ui_settings)
