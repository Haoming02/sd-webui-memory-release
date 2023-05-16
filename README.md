# SD Webui Memory Release
This is an Extension for the [Automatic1111 Webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui), that calls `torch.cuda.empty_cache()` after each generation.

### But Why?
A few Reddit posts/comments mention that CUDA sometimes has memory issues, 
and if you trigger the **Out of Memory Error**, it can continue to leak memory still.
This Extension *tries to* solve that, by calling `torch.cuda.empty_cache()` after each generation.
However, turns out `postprocess` is not called when the generation fails.
So now I added a button to manually call `torch.cuda.empty_cache()`.

<p align="center"><img src="Sample.jpg"></p>

**Note:** I'm 99.9% sure that this Extension helps nothing. You basically do **not** need this. Use it at your own risk~