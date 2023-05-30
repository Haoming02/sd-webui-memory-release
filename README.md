# SD Webui Memory Release
This is an Extension for the [Automatic1111 Webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui), that calls `torch.cuda.empty_cache()` after each generation.

### But Why?
- A few Reddit posts/comments mention that CUDA sometimes has memory issues, 
and if you trigger the **Out of Memory Error**, it can continue to leak memory still.
This Extension *tried to* solve that, by calling `torch.cuda.empty_cache()` after each generation.

- However, turns out `postprocess` is not called when the generation fails.
Therefore, I added a button to manually call `torch.cuda.empty_cache()`.

- Toggle `Debug` to see if the function is actually being called.

<p align="center"><img src="Sample.jpg"></p>

<hr>

<sup>[1] I'm 99.9% sure that this Extension helps nothing. You most likely do ***not*** need this. </sup>

<sup>[2] Shout out to [`@kgmkm_mkgm`](https://twitter.com/kgmkm_mkgm/status/1658760768958140418) for sharing this Extension with tens of thousands of people. </sup>