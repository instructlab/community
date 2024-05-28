# Quick Start Guide

## Table of contents

1. [Install ilab](#install-ilab)
2. [Initialize ilab](#%EF%B8%8F-initialize-ilab)
3. [Download the model](#-download-the-model)
4. [Serving the model](#-serving-the-model)
5. [Train the model](#%EF%B8%8F-training-and-interacting-with-the-model)

This Quick Start Guide will help you get InstructLab
working on your laptop or machine and is expected to take approximately XX minutes. If you'd like more details on this process, see [the Taxonomy README](https://github.com/instructlab/taxonomy/blob/main/README.md) or if you'd like more information on the `cli`, please see [the ilab CLI README](https://github.com/instructlab/instructlab/blob/main/README.md)

### Install `ilab`

## 📋 Requirements

- **🍎 Apple M1/M2/M3 Mac or 🐧 Linux system** (tested on Fedora). We anticipate support for more operating systems in the future.
- C++ compiler
- Python 3.9+
- Approximately 60GB disk space (entire process)

## ✅ Getting started

### 🧰 Installing `ilab`

1. If you are on Fedora Linux, install C++, Python 3.9+, and other necessary tools by running the following command:

    ```bash
    sudo dnf install g++ gcc make pip python3 python3-devel python3-GitPython
    ```

   Optional: If g++ is not found, try 'gcc-c++' by running the following command:

     ```bash
     sudo dnf install gcc-c++ gcc make pip python3 python3-devel python3-GitPython
     ```

2. Create a new directory called `instructlab` to store the files the `ilab` CLI needs when running and CD into the directory by running the following command:

   ```bash
   mkdir instructlab
   cd instructlab
   ```

   > **NOTE:** The following steps in this document use [Python venv](https://docs.python.org/3/library/venv.html) for virtual environments. However, if you use another tool such as [pyenv](https://github.com/pyenv/pyenv) or [Miniforge](https://github.com/conda-forge/miniforge) for managing Python environments on your machine continue to use that tool instead. Otherwise, you may have issues with packages that are installed but not found in `venv`.

3. Install and activate your `venv` environment by running the following command:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install git+https://github.com/instructlab/instructlab.git@stable
   # or
   pip install instructlab
   ```

   > **NOTE**: ⏳ `pip install` may take some time, depending on your internet connection.

4. From your `venv` environment, verify `ilab` is installed correctly, by running the `ilab` command.

   ```bash
   ilab
   ```

#### Example output

   ```shell
   (venv) $ ilab
   Usage: ilab [OPTIONS] COMMAND [ARGS]...

   CLI for interacting with InstructLab.

   If this is your first time running `ilab`, it's best to start with `ilab init`
   to create the environment

   Options:
   --config PATH  Path to a configuration file.  [default: config.yaml]
   --help         Show this message and exit.

   Commands:
   chat      Run a chat using the modified model
   check     Check that taxonomy is valid
   convert   Converts model to GGUF
   download  Download the model(s) to train
   generate  Generates synthetic data to enhance your example data
   init      Initializes environment for InstructLab
   list      Lists taxonomy files that have changed since a reference commit (default origin/main)
   serve     Start a local server
   test      Runs basic test to ensure model correctness
   train     Takes synthetic data generated locally with `ilab generate`...
   ```

   > **IMPORTANT:** every `ilab` command needs to be run from within your Python virtual environment. To enter the Python environment, run the following command:

   ```bash
   source venv/bin/activate
   ```

### 🏗️ Initialize `ilab`

1. Initialize `ilab` by running the following command:

   ```bash
   ilab init
   ```

   Example output:

   ```bash
   Welcome to InstructLab CLI. This guide will help you set up your environment.
   Please provide the following values to initiate the environment [press Enter for defaults]:
   Path to taxonomy repo [taxonomy]: <ENTER>
   ```

2. When prompted by the interface, press **Enter** to add a new default `config.yaml` file.

3. When prompted, clone the `git@github.com:instructlab/taxonomy.git` repository into the current directory by typing **y**.

   **Optional**: If you want to point to an existing local clone of the `taxonomy` repository, you can pass the path interactively or alternatively with the `--taxonomy-path` flag.

   Example output:

   ```bash
   (venv) $ ilab init
   Welcome to InstructLab CLI. This guide will help you set up your environment.
   Please provide the following values to initiate the environment [press Enter for defaults]:
   Path to taxonomy repo [taxonomy]: <ENTER>
   `taxonomy` seems to not exists or is empty. Should I clone git@github.com:instructlab/taxonomy.git for you? [y/N]: y
   Cloning git@github.com:instructlab/taxonomy.git...
   Generating `config.yaml` in the current directory...
   Initialization completed successfully, you're ready to start using `lab`. Enjoy!
   ```

   `ilab` will use the default configuration file unless otherwise specified. You can override this behavior with the `--config` parameter for any `ilab` command.

### 📥 Download the model

- Run the `ilab download`command.

  ```bash
  ilab download
  ```

  `ilab download` will download a pre-trained [model](https://huggingface.co/ibm/) (~4.4G) from HuggingFace and store it in a `models` directory:

  ```bash
  (venv) $ ilab download
  Downloading model from ibm/merlinite-7b-GGUF@main to models...
  (venv) $ ls models
  merlinite-7b-Q4_K_M.gguf
   ```

  > **NOTE** ⏳ This command can take few minutes or immediately depending on your internet connection or model is cached. If you have issues connecting to Hugging Face, refer to the [Hugging Face discussion forum](https://discuss.huggingface.co/) for more details.

### 🍴 Serving the model

- Serve the model by running the following command:

   ```bash
   ilab serve
   ```

   Once the model is served and ready, you'll see the following output:

   ```bash
   (venv) $ ilab serve
   INFO 2024-03-02 02:21:11,352 lab.py:201 Using model 'models/ggml-merlinite-7b-0302-Q4_K_M.gguf' with -1 gpu-layers and 4096 max context size.
   Starting server process
   After application startup complete see http://127.0.0.1:8000/docs for API.
   Press CTRL+C to shut down the server.
   ```

   > **NOTE:** If multiple `ilab` clients try to connect to the same ilab server at the same time, the 1st will connect to the server while the others will start their own temporary server. This will require additional resources on the host machine.

### 📣 Chat with the model

Because you're serving the model in one terminal window, you will have to create a new window and re-activate your Python virtual environment to run `ilab chat` command:

   ```bash
   source venv/bin/activate
   ilab chat
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
