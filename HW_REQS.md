## 📋 Hardware requirements

The local training is the most hardware intensive part of this process. 
Your hardware determines how fast/slow training the model locally will take.
To run and train InstructLab locally, you must meet the following requirements:

The local training is the most hardware intensive part of this process. Your hardware determines how fast/slow training
the model locally will take.

To run and train InstructLab locally, you must meet the following requirements:

1. A supported operating system
   - A Linux-based operating system
   - An Apple Silicon M1, M2, or M3 system
   - A Windows system with WSL (Windows Subsystem for Linux)
2. Python 3.10 or 3.11, including the development headers
3. Approximately 10GB of free disk space to get through the `ilab generate` step
4. Approximately 60GB of free disk space is needed to run the entire process locally on Apple hardware
5. About 32 GB RAM

> **NOTE:** Python 3.12 is currently not supported, because some dependencies don't work on Python 3.12, yet.
<!-- -->
> **NOTE:** When installing the `ilab` CLI on macOS, you may have to run the 
> `xcode-select --install` command, installing the required packages previously listed.