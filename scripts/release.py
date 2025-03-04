from modules.script_callbacks import on_ui_settings
from modules.shared import opts, OptionInfo
from modules import scripts

from gradio import Accordion, Button

try:
    from backend.memory_management import soft_empty_cache
except ImportError:
    try:
        from ldm_patched.modules.model_management import soft_empty_cache
    except ImportError:

        import torch
        import gc

        def soft_empty_cache():
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()
            gc.collect()


class MemRel(scripts.Script):

    def title(self):
        return "Memory Release"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with Accordion(label="Memory Release", open=False):
            release_button = Button(
                value="🧹",
                tooltip="Garbage Collect",
                elem_id=self.elem_id("memre_btn"),
            )
            release_button.click(fn=MemRel.mem_release, queue=False)

    def postprocess_batch(self, *args, **kwargs):
        MemRel.mem_release()

    def postprocess(self, *args, **kwargs):
        MemRel.mem_release()

    @staticmethod
    def mem_release():
        try:
            soft_empty_cache()
        except Exception as e:
            if getattr(opts, "memre_debug", False):
                from modules.errors import display

                display(e, "Memory Release")
        else:
            if getattr(opts, "memre_debug", False):
                print("\nMemory Released!\n")


def on_mem_settings():
    opts.add_option(
        "memre_debug",
        OptionInfo(
            False,
            "Memory Release - Debug",
            section=("system", "System"),
            category_id="system",
        ),
    )


on_ui_settings(on_mem_settings)
