# CS 542 Machine Learning: Diffusers Pipeline for Image Generation  
## Dependencies
1. Use a Conda environment with Python 3.10. In version 3.11 of Python, the Cuda version of pytorch is unable to be installed, only the CPU version. A machine with an NVIDIA GPU is recommended. 
2. To install pytorch-cuda in an environment using Python 3.10, run the following command: `conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia`.
3. Install additional dependencies as needed. These may include `pip install opencv-python`, `pip install diffusers`, `pip install transformers`, `pip install accelerate`, and `pip install torch-fidelity`. 

## Getting the dataset from Kaggle
### Download:
Flowers *(Recommended)*:  
https://www.kaggle.com/datasets/l3llff/flowers?resource=download

CelebA:  
https://www.kaggle.com/datasets/jessicali9530/celeba-dataset


### Using the Flowers dataset:
1. Download the dataset from: https://www.kaggle.com/datasets/l3llff/flowers?resource=download
2. Unzip the file to a folder in your repository.
3. Copy the relative path of a subsection the unzipped folder, "flowers". We used `flowers/black_eyed_susan`.
4. Ensure that `source_folder_path = 'flowers/black_eyed_susan'` in the main function of the `data.py` script. 
5. Run the `data.py` script. This will create a folder called train_images that will be used by the `train.py` script.
6. Run the `train.py` script. Model checkpoints and sample images will be saved every 5 epochs in the `gen_model` folder. The frequency they are saved can be adjusted in this script.
7. Run the `gen.py` script. Generated images will be saved in the `gen_images` folder. We have 500 images being generated. This may take a while.
8. Run the `eval.py` script.

### Using the CelebA dataset:
1. Download the dataset from: https://www.kaggle.com/datasets/jessicali9530/celeba-dataset
2. Unzip the file to a folder in your repository.
3. Copy the relative path of the unzipped folder, "img_align_celeba".
4. Ensure that `source_folder_path = 'img_align_celeba'` in the `data.py` script.
5. Follow steps 5-8 above

## To recap if in need of a new environment
### Create a conda environment:
conda create -n cs542 python=3.10  
conda activate cs542  

### Installations for class:
conda install jupyter  
conda install pandas scikit-learn seaborn scipy  
conda install matplotlib tqdm  
conda install juptyer_client pydot  
pip install graphviz  
pip install pipwin  
pip install tensorflow  
conda scikit-image  
pip install --upgrade langchain  
pip install --upgrade langchain-experimental  
pip install --upgrade langchain-openai  
pip install --upgrade semantic-kernel  
pip install langchainhub   

### For this project we installed: 
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia  
pip install opencv-python  
pip install diffusers  
pip install transformers  
pip install accelerate  
pip install torch-fidelity  