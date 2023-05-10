import modules.scripts as scripts
import torch
import gc

class Script(scripts.Script):

    def __init__(self):
        pass

    def title(self):
        return "Memory Release"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def postprocess(self, p, processed, *args):
        gc.collect()
        torch.cuda.empty_cache()
        gc.collect()
        
        return