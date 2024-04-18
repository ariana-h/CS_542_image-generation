# CS 542 Machine Learning: Diffusers Pipeline for Image Generation  
## Getting the dataset from Kaggle
https://www.kaggle.com/datasets/jessicali9530/celeba-dataset

**Using the dataset:**
1. Download the dataset from https://www.kaggle.com/datasets/jessicali9530/celeba-dataset
2. It will download as archive.zip
3. Unzip the file to a folder in your repository.
4. Copy the relative path of the unzipped folder, "img_align_celeba".
5. Ensure that `source_folder_path = 'img_align_celeba'` in the `data.py` script.
6. Run the `data.py` script.
7. Run the `train.py` script.
8. Run the `gen.py` script.
9. Run the `eval.py` script.

**Dependencies**
1. Use a Conda environment with Python 3.10. In version 3.11 of Python, the Cuda version of pytorch is unable to be installed, only the CPU version. A machine with an NVIDIA GPU is recommended. 
2. To install pytorch-cuda in an environment using Python 3.10, run the following command: `conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia`.
3. Install additional dependencies as needed. These may include `pip install opencv-python`, `pip install diffusers`, `pip install transformers`, `pip install accelerate`, and `pip install torch-fidelity`. 