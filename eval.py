# Referenced: https://arxiv.org/abs/2206.10935

import torch_fidelity as torf

def main():
    metrics = torf.calculate_metrics(
        input1="gen_images",
        input2="train_images",
        kid=True,
        kid_subset_size=25,
        cuda=True)
    print(metrics)


if __name__ == "__main__":
    main()