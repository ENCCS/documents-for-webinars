# GPU programming using Python – A practical intro webinar

<https://enccs.se/events/gpu-programming-using-python-a-practical-intro/>

## About the webinar

In the past decade, Graphics Processing Units (GPUs) have ignited the dynamic evolution of data science. But GPUs can do a lot more than machine learning – these powerful devices can accelerate and massively parallelise any general-purpose computational load in domains involving big data and heavy number crunching. You can use the GPU in your personal computer, or scale up your application to run on a supercomputer. How can you get started?

In this webinar, we focus on GPU-accelerated computing with Python, one of the most popular programming languages for science, engineering, data analytics, and deep learning applications. Starting from familiar Python libraries such as Numpy and Pandas, we will guide you step-by-step into the world of GPU programming. Discover how to harness the power of GPU accelerators using libraries such as CuPy, cuDF, PyCUDA, Jax, and Numba, with a focus on their unique features and capabilities for high-performance computing.

## Who is the webinar for?

The GPU programming using Python webinar is for data scientists, software developers and researchers who want to start using GPUs to accelerate their computational workflows.

## Key takeaways

After attending this seminar, you will be able to:

- get started with GPUs in Python using high-level libraries
- familiarise yourself with the multiple vendors that compete with different software stacks, toolkits, and frameworks
- make informed decisions about your GPU workflows

## Installation

List of packages can be installed using [pixi], [conda] or [pip]. The installation has been tested along
with CUDA 11.5.1 driver in a Ubuntu 22.04 LTS distribution, which in turn was installed
using a `sudo apt install nvidia-cuda-dev` command.

[pixi]: https://pixi.sh
[conda]: https://conda-forge.org/download/
[pip]: https://pip.pypa.io/en/stable/installation/

> [!NOTE]
> The following steps would supply the application packages and their libraries
> and with pixi / conda even the CUDA Toolkit / SDK (for eg. the `nvcc` compiler).
> However CUDA drivers must be installed at the system level, subject to
> [compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/index.html).
> The packages may already be supplied by your distribution's package manager,
> but if not you can try Nvidia's [installation instructions](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)
> (proceed with caution).

### [pixi]

```
pixi run jupyter lab
```

### [conda]

```
conda env create -f environment.yaml
conda run -n gpu-python-webinar jupyter lab
```

### [pip]

Create a virtual environment, activate it and

```
pip install -r requirements.txt
jupyter lab
```

> [!WARNING]
> You may need to ensure that you have the CUDA SDK installed in the system.
