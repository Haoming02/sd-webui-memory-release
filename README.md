# SD Webui Memory Release
This is an Extension for the [Automatic1111 Webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui), that calls `torch.cuda.empty_cache()` after each generation.

### But Why?
- A few Reddit posts/comments mention that CUDA sometimes has memory issues, and the webui may cause memory leaks. 
This Extension *tried to* mediate that by calling `torch.cuda.empty_cache()` after each generation.

### "Features"
- Turns out `postprocess` is not called when a generation fails. Thus, I added a button to manually try releasing the memory.

- Also comes with another button that unloads and reloads the checkpoint for the maximum cleanse.
    - ~~*This just calls the same functions that you can already find in the **Actions** section of the **Settings** tab*~~

- In the **System** section of the **Settings** tab, you can also turn on debug log or enable additionally refreshing the `torch` networks.

<p align="center"><img src="Sample.jpg"></p>

<hr>

<sup>[1] I'm 99.99% sure that this Extension helps nothing. You most likely do **not** need this. </sup>

<sup>[2] Shout out to [`@kgmkm_mkgm`](https://twitter.com/kgmkm_mkgm/status/1658760768958140418) for sharing this Extension with tens of thousands of people. </sup>

<sup>[3] ~~Seriously, why are people downloading this? Why are people even Star-ing this? What does this actually help?~~ </sup>