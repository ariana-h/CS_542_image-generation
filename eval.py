import torch_fidelity as torf

def main():
    metrics = torf.calculate_metrics(
        input1="gen_images",
        input2="train_images",
        fid=True,
        kid=True,
        kid_subset_size=25, # Just doing this for expediency 200,
        cuda=True)
    print(metrics)


if __name__ == "__main__":
    main()