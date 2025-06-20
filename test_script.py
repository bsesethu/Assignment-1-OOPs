# Resource PyTorch Dataloader https://www.geeksforgeeks.org/deep-learning/pytorch-dataloader/
import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# From another online source, didn't save it's info
# 1. Define a custom Dataset class
class CustomDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        # Return the total number of samples in the dataset
        return len(self.data)   

    def __getitem__(self, idx):
        # Return a single sample (data, label) at the given index
        sample_data = self.data[idx]
        sample_label = self.labels[idx]
        return torch.tensor(sample_data, dtype=torch.float32), torch.tensor(sample_label, dtype=torch.long)

# 2. Create some dummy data
num_samples = 100
data = np.random.rand(num_samples, 10)  # 100 samples, each with 10 features
labels = np.random.randint(0, 2, num_samples) # 100 labels (0 or 1)

# 3. Instantiate the custom Dataset
dataset = CustomDataset(data, labels)

# 4. Instantiate the DataLoader
batch_size = 16
shuffle_data = True # Set to True to shuffle data at each epoch
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle_data)

# 5. Iterate through the DataLoader to get batches of data
print(f"Number of batches: {len(dataloader)}")
for i, (batch_data, batch_labels) in enumerate(dataloader):
    print(f"Batch {i+1}: Data shape: {batch_data.shape}, Labels shape: {batch_labels.shape}")
    if i == 0: # Print first batch details for demonstration
        print(f"First batch data example:\n{batch_data[0]}")
        print(f"First batch label example: {batch_labels[0]}")
    if i >= 4: # Stop after a few batches for brevity
        break