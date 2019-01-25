# Extract 3D patches from 3D images

test = nib.load('/home/xinheng/Documents/Split/Brats18_2013_1_1_t1.nii.gz').get_fdata()
test = torch.tensor(test)
test.shape
S = 128 # channel dim
W = 64 # width
H = 128 # height
batch_size = 1

test.unsqueeze_(0) #add the first batch_size channel

size = 32 # patch size
stride =32# patch stride
patches = test.unfold(1, size, stride).unfold(2, size, stride).unfold(3, size, stride)
patches.contiguous().view(-1,32,32,32).shape # 32*32*32*32, got 32 batches, 32*32*32 patches

