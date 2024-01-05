# SD Webui Memory Release
This is an Extension for the [Automatic1111 Webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui), that calls `torch.cuda.empty_cache()` after each generation.

### But Why?
- A few Reddit posts/comments mentioned that CUDA sometimes can cause memory issues/leaks. 
This Extension *tries to* mediate that by calling `torch.cuda.empty_cache()` after each generation.

### "Features"
- `gc.collect()` and `torch.cuda.empty_cache()` after every generation
- A *placebo*™️ button to manually free the memory
- Another button to reload the checkpoint
    - *This is just the same built-in functions in the **Actions** section of the **Settings** tab*

<p align="center">
<img src="Sample.jpg" width=512>
</p>

<hr>

<sup>[0] Webui nowdays does a pretty good job cleaning the memory. The graph above is severely outdated. </sup>

<sup>[1] I'm 99.999% sure that this Extension helps nothing. You most likely do **not** need this. </sup>

<sup>[2] Shout out to [`@kgmkm_mkgm`](https://twitter.com/kgmkm_mkgm/status/1658760768958140418) for sharing this Extension with tens of thousands of people. </sup>

<sup>[3] ~~Seriously, why are people downloading this? Why do people even Star this? What does this actually help?~~ </sup>

<sup>[4] ~~Why do I still update this? Eh, it doesn't hurt to install anyway.~~ </sup>
