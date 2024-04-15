# Quick Start Guide


## Table of contents
1. [Install ilab](#install-ilab)
2. [Initialize ilab](#%EF%B8%8F-initialize-ilab)
3. [Download the model](#-download-the-model)
4. [Serving the model](#-serving-the-model)
5. [Train the model](#%EF%B8%8F-training-and-interacting-with-the-model)

This document is the quickest of starting of the steps you need to do to get InstructLab
working on your laptop or machine. If you need more details please take a look at:
- [The Taxonomy README](https://github.com/instruct-lab/taxonomy/blob/main/README.md)
- [The ilab CLI README](https://github.com/instruct-lab/cli/blob/main/README.md)

## Steps

### Install `ilab`

## 📋 Requirements

- **🍎 Apple M1/M2/M3 Mac or 🐧 Linux system** (tested on Fedora). We anticipate support for more operating systems in the future.
- C++ compiler
- Python 3.9+
- Approximately 60GB disk space (entire process)


## ✅ Getting started

### 🧰 Installing `ilab`

1. If you are on Fedora Linux, install C++, Python 3.9+, and other necessary tools by running the following command:

    ```shell
   sudo dnf install g++ gcc make pip python3 python3-devel python3-GitPython
   ```

   Optional: If g++ is not found, try 'gcc-c++' by running the following command:

     ```shell
     sudo dnf install gcc-c++ gcc make pip python3 python3-devel python3-GitPython
     ```

2. Create a new directory called `instruct-lab` to store the files the `ilab` CLI needs when running and CD into the directory by running the following command:

   ```shell
   mkdir instruct-lab
   cd instruct-lab
   ```
   > **NOTE:** The following steps in this document use [Python venv](https://docs.python.org/3/library/venv.html) for virtual environments. However, if you use another tool such as [pyenv](https://github.com/pyenv/pyenv) or [Conda Miniforge](https://github.com/conda-forge/miniforge) for managing Python environments on your machine continue to use that tool instead. Otherwise, you may have issues with packages that are installed but not found in `venv`.

3. Install and activate your `venv` environment by running the following command:

   ```shell
   python3 -m venv venv
   source venv/bin/activate
   pip install git+ssh://git@github.com/instruct-lab/cli.git@stable
   ```
   > **NOTE**: ⏳ `pip install` may take some time, depending on your internet connection.

4. From your `venv` environment, verify `ilab` is installed correctly, by running the `ilab` command.

   ```shell
   ilab
   ```

   #### Example output:
   ```
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

   ```shell
   source venv/bin/activate
   ```

### 🏗️ Initialize `ilab`

1. Initialize `ilab` by running the following command:

   ```shell
   ilab init
   ```


   #### Example output:

   ```shell
   Welcome to InstructLab CLI. This guide will help you set up your environment.
   Please provide the following values to initiate the environment [press Enter for defaults]:
   Path to taxonomy repo [taxonomy]: <ENTER>
   ```

2. When prompted by the interface, press **Enter** to add a new default `config.yaml` file.

3. When prompted, clone the `git@github.com:instruct-lab/taxonomy.git` repository into the current directory by typing **y**.

   **Optional**: If you want to point to an existing local clone of the `taxonomy` repository, you can pass the path interactively or alternatively with the `--taxonomy-path` flag.

   #### Example output:

   ```shell
   (venv) $ ilab init
   Welcome to InstructLab CLI. This guide will help you set up your environment.
   Please provide the following values to initiate the environment [press Enter for defaults]:
   Path to taxonomy repo [taxonomy]: <ENTER>
   `taxonomy` seems to not exists or is empty. Should I clone git@github.com:instruct-lab/taxonomy.git for you? [y/N]: y
   Cloning git@github.com:instruct-lab/taxonomy.git...
   Generating `config.yaml` in the current directory...
   Initialization completed successfully, you're ready to start using `lab`. Enjoy!
   ```
   `ilab` will use the default configuration file unless otherwise specified. You can override this behavior with the `--config` parameter for any `ilab` command.

### 📥 Download the model

* Run the `ilab download`command.

  ```shell
  ilab download
  ```

  `ilab download` will download a pre-trained [model](https://huggingface.co/ibm/) (~4.4G) from HuggingFace and store it in a `models` directory:

  ```shell
  (venv) $ ilab download
  Downloading model from ibm/merlinite-7b-GGUF@main to models...
  (venv) $ ls models
  merlinite-7b-Q4_K_M.gguf
   ```

  > **NOTE** ⏳ This command can take few minutes or immediately depending on your internet connection or model is cached. If you have issues connecting to Hugging Face, refer to the [Hugging Face discussion forum](https://discuss.huggingface.co/) for more details.

### 🍴 Serving the model

* Serve the model by running the following command:

   ```shell
   ilab serve
   ```

   Once the model is served and ready, you'll see the following output:

   ```shell
   (venv) $ ilab serve
   INFO 2024-03-02 02:21:11,352 lab.py:201 Using model 'models/ggml-merlinite-7b-0302-Q4_K_M.gguf' with -1 gpu-layers and 4096 max context size.
   Starting server process
   After application startup complete see http://127.0.0.1:8000/docs for API.
   Press CTRL+C to shut down the server.
   ```

   > **NOTE:** If multiple `ilab` clients try to connect to the same ilab server at the same time, the 1st will connect to the server while the others will start their own temporary server. This will require additional resources on the host machine.

### 📣 Chat with the model

Because you're serving the model in one terminal window, you will have to create a new window and re-activate your Python virtual environment to run `ilab chat` command:

```shell
source venv/bin/activate
$ilab chat
```

### 🏋️ Training and interacting with the model

Now that you have a working environment, you should see how we need to give it new knowledge.

Ask it a question (the base model gets this wrong, see https://github.com/instruct-lab/taxonomy/pull/659):

> When was the first British women's softball leauge established?

This should be incorrect, lets add knowledge that teaches the mode the correct year (1953)

1. Verify you have the `taxonomy` directory in the working directory you are in.
    ```bash
   ls -al taxonomy
   ```

2. Create the directory for softball by running the following command:
    ```
    mkdir -p taxonomy/knowledge/sports/overview/softball
    ```

3. Pull down the example `qna.yaml` from the repository, and put it in `/tmp/` or the like:

    ```bash
    wget -O /tmp/qna.yaml https://raw.githubusercontent.com/instruct-lab/taxonomy/094745b5067b68a5f780d6db241550d72310c196/knowledge/sports/overview/softball/qna.yaml
    head /tmp/qna.yaml
    ```

4. Copy the file into the new directory:
    ```bash
    cp /tmp/qna.yaml taxonomy/knowledge/sports/overview/softball/
    ```

5. Verify the 1953 is in the file:
    ```bash
    grep -B1 -A3 1953 taxonomy/knowledge/sports/overview/softball/qna.yaml
    ```

6. Verify that the `yaml` file is correctly formatted and that `ilab` can see that it's been changed by running the following command:
    ```bash
    ilab diff
    ```

7. Create some generated questions from the `qna.yaml` file.
    >**Note**: Depending on the computer you are running this can take some time. ☕x(3 or 4)
    ```bash
    time ilab generate
    ```

8. Take a look at the output questions, see what the model has come up with (TODO LINK)

9. Now is the actual training time! If you have a non-gpu run the following command, if you have a GPU and want to use that the second command and configure to your setup:

   >**Note**: Depending on the computer you are running this can take some time. ☕x(a lot)
    ```bash
    time ilab train
    ```
   >Optional:
    ```shell
    ilab train --help
    ```

### Converting the model and reserving serving it
1. Convert the model to the `gguf` so you can serve it with `ilab serve` command by running the following command:
   >**Note**: this is only needed if you are on an M Mac, Linux you don't need this step.
    ```bash
    time ilab convert
    ```

2. Serve your new model by running the following command:
    ```bash
    ilab serve --model-path ibm-merlinite-7b-mlx-q-fused-pt/ggml-model-Q4_K_M.gguf
    ```

3. Start up another chat session with it:
    ```bash
    ilab chat
    ```

4. Ask the original questions again:

   > When was the first British women's softball leauge established?

   The answer should be 1953!

## Conclusion

So you've successfully got `ilab` up and running. SUCCESS! Breathe in for a bit. We're proud of you, and I dare say you're an AI Engineer now.
You're  probably wondering what the next steps are, and frankly your guess is as good as mine but let me give you some suggestions.

- Start playing with knowledge additions. This is to give something "new" to the model. You give it a chunk of data, something it doesn't know about and then train it on that. It's the same workflow as above with a few more steps.
- Host your model someplace and ask it questions remotely. No reason to just run this on your laptop, set up a server and host it remotely, you can even use your iPhone! [Check this out](https://github.com/AugustDev/enchanted)
- TODO MORE HERE

Finally, lets talk about the actual workflow here. This was a "quick start guide" to get you going, but this isn't the actual workflow you'd
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

Again, we're so happy you made it this far, and remember if you have qusetions we are here to help, and are excited to see what you come up with!
