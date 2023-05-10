# Memory Release
This is an Extension for the [Automatic1111 Webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui), that calls `torch.cuda.empty_cache()` after each generation.

### But Why?
A few Reddit posts/comments mention that CUDA may have memory issues sometimes, 
and if you trigger the **Out of Memory Error**, it may continue to leak memory still.
This Extension *aims to* solve that, by calling `torch.cuda.empty_cache()` after each generation, which supposedly helps?

**Note:** I'm 99.9% sure that this Extension basically does absolutely **nothing.** Use it at your own risk~