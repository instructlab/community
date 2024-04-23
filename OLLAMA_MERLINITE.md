# `ollama` and `merlinite-7b-lab`

Here are some steps to getting `ollama` and `merlinite-7b-lab` working together.

Install ollama
```bash
curl https://ollama.ai/install.sh | sh
```

Pull model down from Huggingface
```bash
brew install git-lfs
# or
dnf install git-lfs
git lfs install
git clone https://huggingface.co/instructlab/merlinite-7b-lab
```

Convert to `gguf`
```bash
git clone https://github.com/ggerganov/llama.cpp.git
python3.11 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python convert.py -h
cd models/merlinite-7b-lab/
python ../../src/llama.cpp/convert.py . --outfile merlinite-7b-lab.gguf --outtype f32 --pad-vocab
cd ..
```

Create the Modelfile
```dockerfile
FROM ./merlinite-7b-lab/merlinite-7b-lab.gguf


TEMPLATE """{{ if .System }}<|im_start|>system
{{ .System }}<|im_end|>
{{ end }}{{ if .Prompt }}<|im_start|>user
{{ .Prompt }}<|im_end|>
{{ end }}<|im_start|>assistant
"""

SYSTEM """
You are an AI language model developed by IBM Research.
You are a cautious assistant.
You carefully follow instructions.
You are helpful and harmless and you follow ethical guidelines and promote positive behavior.
"""

PARAMETER stop '<|endoftext|>'
PARAMETER stop '<|im_start|>'
```

Create the model for ollama
```
ollama create merlinite -f Modelfile
ollama run merlinite
```

If you want to serve the model:
```bash
ollama serve # in a terminal or something (unless you want it in sysconfig)
ollama create merlinite -f Modelfile

