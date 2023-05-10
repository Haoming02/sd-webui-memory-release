import modules.scripts as scripts
import gradio as gr
import torch
import os

class Script(scripts.Script):

    def __init__(self):
        pass

    def title(self):
        return "Memory Release"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def postprocess(self, p, processed, *args):

        torch.cuda.empty_cache()
        
        return