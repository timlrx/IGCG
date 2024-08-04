#!/bin/bash

# Clone the IGCG repository
git clone git@github.com:timlrx/IGCG.git
cd IGCG
pip install -r requirements.txt

# Install Git LFS and Tmux
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
apt-get install -y git-lfs tmux

# Configure Git to store credentials
git config --global credential.helper store
huggingface-cli login

# Clone the Llama-2-7b-chat-hf repository from Hugging Face
git clone https://huggingface.co/meta-llama/Llama-2-7b-chat-hf /home/LLM/Llama-2-7b-chat-hf