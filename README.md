# FMCV Transcripts  
**Universal Broadcast Transcripts System**  

If you find this project useful, consider buying me a drink!  
[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://paypal.me/FMCVDRINK)  

---

## Quick Start  

1. Clone the repository:  
   ```bash
   git clone https://github.com/cyysky/FMCV_Transcripts
   ```

2. Copy the `.env` file:  
   ```bash
   cp .env.example .env
   ```

3. Download and install Docker Desktop:  
   [Docker Desktop](https://www.docker.com/products/docker-desktop/)  
  
  
4. Install ollama  
	[Ollama](https://ollama.com/download)  
	download ollama model  
	ollama run deepseek-r1:8b-llama-distill-q8_0  
	ollama run deepseek-r1:1.5b  

---

## Configuration  

### For NVIDIA GPU (16GB VRAM or higher)  
Recommended `.env` settings:  
```env
MIN_PROCESS_GAP_SECONDS = 0.5  
MAX_PROCESS_TIME_MINUTES = 1  
```  

Start the application with GPU support:  
```bash
docker compose --profile gpu up -d
```  

### For CPU (Experimental)  
Recommended `.env` settings:  
```env
MIN_PROCESS_GAP_SECONDS = 30  
MAX_PROCESS_TIME_MINUTES = 100  

WHISPER_MODEL=openai/openai/whisper-tiny
OPENAI_MODEL=deepseek-r1:1.5b

```  

Start the application with CPU support:  
```bash
docker compose --profile cpu up -d
```  

---

## Usage  
Access the application at:  
[http://localhost:8999](http://localhost:8999)  

---

## Introduction Video  
Watch the introduction video for more details:  
[![YouTube](https://img.shields.io/badge/YouTube-Introduction_Video-red)](https://youtu.be/Md_bWUXAWUw)  

[Introduction Video](https://www.youtube.com/watch?v=83HMr3q_Xz0)
--- 

Enjoy using **FMCV Transcripts**! 🚀

Contact : chong@fmcv.my⁠

