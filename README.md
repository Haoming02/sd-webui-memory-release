# SD Webui Memory Release
This is an Extension for the [Automatic1111 Webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui), which *attempts to* clean up memory after each generation.

### But Why?
- A few Reddit posts/comments mentioned that CUDA sometimes can cause memory issues/leaks. This Extension *tries to* solve that by calling `torch.cuda.empty_cache()` after each generation.

### Features
- Perform `torch.cuda.empty_cache()` and `gc.collect()` after every generation automatically
- Add a `🧹` button that triggers the cleanup manually

<hr>

<sup>[1] Shout out to [@kgmkm_mkgm](https://twitter.com/kgmkm_mkgm/status/1658760768958140418) for sharing this Extension with tens of thousands of people </sup>

<sup>[2] Apparently, this indeed does help in [certain situations](https://github.com/Haoming02/sd-webui-memory-release/issues/3) </sup>
