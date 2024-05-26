# Quick Start Guide

## Table of contents

1. [Install ilab](#install-ilab)
2. [Initialize ilab](#%EF%B8%8F-initialize-ilab)
3. [Download the model](#-download-the-model)
4. [Serving the model](#-serving-the-model)
5. [Train the model](#%EF%B8%8F-training-and-interacting-with-the-model)

This Quick Start Guide will help you get InstructLab
working on your laptop or machine and is expected to take approximately XX minutes. If you'd like more details on this process, see [the Taxonomy README](https://github.com/instructlab/taxonomy/blob/main/README.md) or if you'd like more information on the `cli`, please see [the ilab CLI README](https://github.com/instructlab/instructlab/blob/main/README.md)

## ✅ Getting started

### 🧰 Installing `ilab`

1. When installing on Fedora Linux, install C++, Python 3.9+, and other necessary tools by running the following command:

   ```shell
   sudo dnf install g++ gcc make pip python3 python3-devel python3-GitPython
   ```

   Optional: If `g++` is not found, try `gcc-c++` by running the following command:

   ```shell
   sudo dnf install gcc-c++ gcc make pip python3 python3-devel python3-GitPython
   ```

   If you are running on macOS, this installation is not necessary and you can begin your process with the following step.  

2. Create a new directory called `instructlab` to store the files the `ilab` CLI needs when running and `cd` into the directory by running the following command:

   ```shell
   mkdir instructlab
   cd instructlab
   ```

   > **NOTE:** The following steps in this document use [Python venv](https://docs.python.org/3/library/venv.html) for virtual environments. However, if you use another tool such as [pyenv](https://github.com/pyenv/pyenv) or [Conda Miniforge](https://github.com/conda-forge/miniforge) for managing Python environments on your machine continue to use that tool instead. Otherwise, you may have issues with packages that are installed but not found in `venv`.

3. Install and activate your `venv` environment by running the following command:

   > **NOTE**: ⏳ `pip install` may take some time, depending on your internet connection. In case installation fails with error ``unsupported instruction `vpdpbusd'``, append `-C cmake.args="-DLLAMA_NATIVE=off"` to `pip install` command.

   See [the GPU acceleration documentation](./docs/gpu-acceleration.md) for how to
   to enable hardware acceleration for inference and training on AMD ROCm,
   Apple Metal Performance Shaders (MPS), and Nvidia CUDA.

   #### To install with no GPU acceleration and PyTorch without CUDA bindings

   ```shell
   python3 -m venv --upgrade-deps venv
   source venv/bin/activate
   (venv) $ pip cache remove llama_cpp_python
   (venv) $ pip install git+https://github.com/instructlab/instructlab.git@stable --extra-index-url=https://download.pytorch.org/whl/cpu
   ```

   #### To install with AMD ROCm

   ```shell
   python3 -m venv --upgrade-deps venv
   source venv/bin/activate
   (venv) $ pip cache remove llama_cpp_python
   (venv) $ pip install git+https://github.com/instructlab/instructlab.git@stable \
       --extra-index-url https://download.pytorch.org/whl/rocm6.0 \
       -C cmake.args="-DLLAMA_HIPBLAS=on" \
       -C cmake.args="-DAMDGPU_TARGETS=all" \
       -C cmake.args="-DCMAKE_C_COMPILER=/opt/rocm/llvm/bin/clang" \
       -C cmake.args="-DCMAKE_CXX_COMPILER=/opt/rocm/llvm/bin/clang++" \
       -C cmake.args="-DCMAKE_PREFIX_PATH=/opt/rocm"
   ```

   On Fedora 40+, use `-DCMAKE_C_COMPILER=clang-17` and `-DCMAKE_CXX_COMPILER=clang++-17`.

   #### To install with Apple Metal on M1/M2/M3 Mac

   ```shell
   python3 -m venv --upgrade-deps venv
   source venv/bin/activate
   (venv) $ pip cache remove llama_cpp_python
   (venv) $ pip install git+https://github.com/instructlab/instructlab.git@stable -C cmake.args="-DLLAMA_METAL=on"
   ```

   #### To install with Nvidia CUDA

   ```shell
   python3 -m venv --upgrade-deps venv
   source venv/bin/activate
   (venv) $ pip cache remove llama_cpp_python
   (venv) $ pip install git+https://github.com/instructlab/instructlab.git@stable -C cmake.args="-DLLAMA_CUBLAS=on"
   ```

4. From your `venv` environment, verify `ilab` is installed correctly, by running the `ilab` command.

   ```shell
   ilab
   ```

   #### Example output

   ```shell
   (venv) $ ilab
   Usage: ilab [OPTIONS] COMMAND [ARGS]...

   CLI for interacting with InstructLab.

   If this is your first time running InstructLab, it's best to start with `ilab init` to create the environment.

   Options:
   --config PATH  Path to a configuration file.  [default: config.yaml]
   --version      Show the version and exit.
   --help         Show this message and exit.

   Commands:
   chat      Run a chat using the modified model
   check     (Deprecated) Check that taxonomy is valid
   convert   Converts model to GGUF
   diff      Lists taxonomy files that have changed since <taxonomy-base>...
   download  Download the model(s) to train
   generate  Generates synthetic data to enhance your example data
   init      Initializes environment for InstructLab
   list      (Deprecated) Lists taxonomy files that have changed since <taxonomy-base>.
   serve     Start a local server
   test      Runs basic test to ensure model correctness
   train     Takes synthetic data generated locally with `ilab generate`...
   ```

   > **IMPORTANT:** every `ilab` command needs to be run from within your Python virtual environment. To enter the Python environment, run the following command:

   ```shell
   source venv/bin/activate
   ```

5. You may optionally enable tab completion for the `ilab` command.

   #### Bash (version 4.4 or newer)

   Enable tab completion in `bash` with the following command:

   ```sh
   eval "$(_ILAB_COMPLETE=bash_source ilab)"
   ```

   To have this enabled automatically every time you open a new shell,
   you can save the completion script and source it from `~/.bashrc`:

   ```sh
   _ILAB_COMPLETE=bash_source ilab > ~/.ilab-complete.bash
   echo ". ~/.ilab-complete.bash" >> ~/.bashrc
   ```

   #### Zsh

   Enable tab completion in `zsh` with the following command:

   ```sh
   eval "$(_ILAB_COMPLETE=zsh_source ilab)"
   ```

   To have this enabled automatically every time you open a new shell,
   you can save the completion script and source it from `~/.zshrc`:

   ```sh
   _ILAB_COMPLETE=zsh_source ilab > ~/.ilab-complete.zsh
   echo ". ~/.ilab-complete.zsh" >> ~/.zshrc
   ```

   #### Fish

   Enable tab completion in `fish` with the following command:

   ```sh
   _ILAB_COMPLETE=fish_source ilab | source
   ```

   To have this enabled automatically every time you open a new shell,
   you can save the completion script and source it from `~/.bashrc`:

   ```sh
   _ILAB_COMPLETE=fish_source ilab > ~/.config/fish/completions/ilab.fish
   ```

### 🏗️ Initialize `ilab`

1. Initialize `ilab` by running the following command:

   ```shell
   ilab init
   ```

   #### Example output

   ```shell
   Welcome to InstructLab CLI. This guide will help you set up your environment.
   Please provide the following values to initiate the environment [press Enter for defaults]:
   Path to taxonomy repo [taxonomy]: <ENTER>
   ```

2. When prompted by the interface, press **Enter** to add a new default `config.yaml` file.

3. When prompted, clone the `https://github.com/instructlab/taxonomy.git` repository into the current directory by typing **y**.

   **Optional**: If you want to point to an existing local clone of the `taxonomy` repository, you can pass the path interactively or alternatively with the `--taxonomy-path` flag.

   #### Example output

   ```shell
   (venv) $ ilab init
   Welcome to InstructLab CLI. This guide will help you set up your environment.
   Please provide the following values to initiate the environment [press Enter for defaults]:
   Path to taxonomy repo [taxonomy]: <ENTER>
   `taxonomy` seems to not exists or is empty. Should I clone https://github.com/instructlab/taxonomy.git for you? [y/N]: y
   Cloning https://github.com/instructlab/taxonomy.git...
   Generating `config.yaml` in the current directory...
   Initialization completed successfully, you're ready to start using `ilab`. Enjoy!
   ```

   `ilab` will use the default configuration file unless otherwise specified. You can override this behavior with the `--config` parameter for any `ilab` command.

   The taxonomy repository uses [submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) to incorporate the [taxonomy schema](https://github.com/instructlab/schema.git).
   When the `ilab init` command clones the taxonomy repository, it automatically handles the submodules.
   If you clone the taxonomy repository yourself, be sure to use the [`--recurse-submodules`](https://git-scm.com/docs/git-clone#Documentation/git-clone.txt---recurse-submodulesltpathspecgt) option on the `git clone` command and the `git pull` command when pulling updates from the remote repository.
   For example:

   ```shell
   git clone --recurse-submodules https://github.com/instructlab/taxonomy.git
   git pull --recurse-submodules
   ```

### 📥 Download the model

- Run the `ilab download`command.

  ```shell
  ilab download
  ```

  `ilab download` will download a pre-trained [model](https://huggingface.co/instructlab/) (~4.4G) from HuggingFace and store it in a `models` directory:

  ```shell
  (venv) $ ilab download
  Downloading model from instructlab/merlinite-7b-lab-GGUF@main to models...
  (venv) $ ls models
  merlinite-7b-lab-Q4_K_M.gguf
  ```

  > **NOTE** ⏳ This command can take few minutes or immediately depending on your internet connection or model is cached. If you have issues connecting to Hugging Face, refer to the [Hugging Face discussion forum](https://discuss.huggingface.co/) for more details.

### 🍴 Serving the model

- Serve the model by running the following command:

   ```shell
   ilab serve
   ```

   Once the model is served and ready, you'll see the following output:

   ```shell
   (venv) $ ilab serve
   INFO 2024-03-02 02:21:11,352 lab.py:201 Using model 'models/ggml-merlinite-7b-lab-Q4_K_M.gguf' with -1 gpu-layers and 4096 max context size.
   Starting server process
   After application startup complete see http://127.0.0.1:8000/docs for API.
   Press CTRL+C to shut down the server.
   ```

   > **NOTE:** If multiple `ilab` clients try to connect to the same InstructLab server at the same time, the 1st will connect to the server while the others will start their own temporary server. This will require additional resources on the host machine.

### 📣 Chat with the model (Optional)

Because you're serving the model in one terminal window, you will have to create a new window and re-activate your Python virtual environment to run `ilab chat` command:

```shell
source venv/bin/activate
ilab chat
```

Before you start adding new skills and knowledge to your model, you can check its baseline performance by asking it a question such as `what is the capital of Canada?`.

> **NOTE:** the model needs to be trained with the generated synthetic data to use the new skills or knowledge

```shell
(venv) $ ilab chat
╭────────────────────────────────────────────────────────────────────────────────────────────────────────────────── system ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Welcome to InstructLab Chat w/ GGML-MERLINITE-7B-lab-Q4_K_M (type /h for help)                                                                                                                                                                    │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
>>b> what is the capital of Canada                                                                                                                                                                                                 [S][default]
╭────────────────────────────────────────────────────────────────────────────────────────────────────── ggml-merlinite-7b-lab-Q4_K_M ───────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ The capital city of Canada is Ottawa. It is located in the province of Ontario, on the southern banks of the Ottawa River in the eastern portion of southern Ontario. The city serves as the political center for Canada, as it is home to │
│ Parliament Hill, which houses the House of Commons, Senate, Supreme Court, and Cabinet of Canada. Ottawa has a rich history and cultural significance, making it an essential part of Canada's identity.                                   │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── elapsed 12.008 seconds ─╯
>>>                                                                                                                                                                                                                               [S][default]
```
### 🏋️ Training and interacting with the model

Now that you have a working environment, you should see how we need to give it new knowledge.

Ask it a question (the default downloaded  model (from `ilab download` and `ilab chat`) gets this wrong, see <https://github.com/instructlab/taxonomy/pull/659>):

> When was the first British women's softball league established?

The answer may be incorrect, so lets add knowledge that teaches the model the correct year (1953)

1. Verify you have the `taxonomy` directory in the working directory you are in.

   ```bash
   ls -al taxonomy
   ```

1. Create the directory for softball

   ```bash
   mkdir -p taxonomy/knowledge/sports/overview/softball
   ```

1. Pull down the example `qna.yaml` from the repository, and put it in `/tmp/` or the like:

   ```bash
   wget -O /tmp/qna.yaml https://raw.githubusercontent.com/instructlab/taxonomy/62feaf54a2fbcd122f2dea419952090378ccb487/knowledge/sports/overview/softball/qna.yaml
   wget -O /tmp/attribution.txt https://raw.githubusercontent.com/instructlab/taxonomy/62feaf54a2fbcd122f2dea419952090378ccb487/knowledge/sports/overview/softball/attribution.txt
   head /tmp/qna.yaml
   head /tmp/attribution.txt
   ```

1. Copy the file into the new directory:

   ```bash
   cp /tmp/qna.yaml taxonomy/knowledge/sports/overview/softball/
   cp /tmp/attribution.txt taxonomy/knowledge/sports/overview/softball/
   ```

1. Verify the 1953 is in the file:

   ```bash
   grep -B1 -A3 1953 taxonomy/knowledge/sports/overview/softball/qna.yaml
   ```

1. Verify that the `yaml` file is correctly formatted and `ilab` can see that it's been changed.

   ```bash
   ilab diff
   ```

1. Create some generated questions from the `qna.yaml` file, **Note**: Depending on the computer you are running this can take some time. ☕x(3 or 4)

   ```bash
   time ilab generate
   ```

1. Take a look at the generated questions, see what the model has come up with (TODO LINK)

1. Now is the actual training time!
**Note**: If you are running on a CPU run the following command. If you want to leverage your GPU, run the `--help` to configure it.  Depending on the computer you are running this can take some time. ☕x(a lot)

   ```bash
   time ilab train
   # or
   ilab train --help
   ```

### Converting the trained model and serving it

- Convert the model to the `gguf` so you can serve it with `ilab serve`:

**Note**: this is only needed if you are on an M Mac, Linux you don't need this step.

   ```bash
   time ilab convert
   ```

- Serve your trained model!

   ```bash
   # Kill your previous model, Ctrl-C or something the original window otherwise you'll won't be using your new model.
   ilab serve --model-path ibm-merlinite-7b-mlx-q-fused-pt/ggml-model-Q4_K_M.gguf
   ```

- Start up another chat session with it:

   ```bash
   ilab chat
   ```

- Ask the original questions again:

> When was the first British women's softball league established?

The answer should be 1953!

## Conclusion

So you've successfully got `ilab` up and running. SUCCESS! Breathe in for a bit. We're proud of you, and I dare say you're an AI Engineer now.
You're  probably wondering what the next steps are, and frankly your guess is as good as mine but let me give you some suggestions.

- Start playing with knowledge additions. This is to give something "new" to the model. You give it a chunk of data, something it doesn't know about and then train it on that. It's the same workflow as above with a few more steps.
- Host your model someplace and ask it questions remotely. No reason to just run this on your laptop, set up a server and host it remotely, you can even use your iPhone! [Check this out](https://github.com/AugustDev/enchanted)
- PRs accepted for other suggestions!

### So do I need to do all of these steps every time?

No, you don't. Lets talk about the actual workflow here. This was a "quick start guide" to get you going, but this isn't the actual workflow you'd
use in real life. After getting `ilab` up and running the only thing you'll have to engage with is more or less these following commands:

```bash
# Create a new qna.yaml file and put it the correct place, like the /softball/ directory in the taxonomy tree
ilab diff
ilab generate
ilab train
ilab serve  --model-path ibm-merlinite-7b-mlx-q-fused-pt/ggml-model-Q4_K_M.gguf
ilab chat
```

As you can see after setting it up, it's pretty straight forward and most of the time will be creating the new taxonomy content and waiting for
the `ilab train` to finish.

Again, we're so happy you made it this far, and remember if you have questions we are here to help, and are excited to see what you come up with!
