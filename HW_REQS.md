## 📋 Hardware requirements

The local training is the most hardware intensive part of this process. Your hardware determines how fast/slow training the model locally will take.
To run and train InstructLab locally, you must meet the following requirements:

1. We anticipate support for more operating systems in the future. For now the supported systems are: 
    - A Linux-based operating system (tested on Fedora)
    - An Apple Silicon M1, M2, or M3 system
    - A Windows system with WSL (Windows Subsystem for Linux) .
2. C++ compiler
3. Python 3.10 or Python 3.11
4. Approximately 60GB disk space (entire process)

> **NOTE:** Python 3.12 is currently not supported, because some dependencies don't work on Python 3.12, yet.
<!-- -->
> **NOTE:** When installing the `ilab` CLI on macOS, you may have to run the `xcode-select --install` command, installing the required packages previously listed.