import cv2
import numpy as np
import torch # instale o kornia # pip install kornia
import matplotlib.pyplot as plt
import kornia 

# Read the image with OpenCV
img: np.ndarray = cv2.imread('lena_gray.bmp')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#convert image to tensor
data: torch.tensor = kornia.utils.image_to_tensor(img, keepdim=False)
data = data.float() / 255.

sharpen = kornia.filters.UnsharpMask((9,9), (2.5,2.5))
sharpened_tensor = sharpen(data)
difference = (sharpened_tensor - data).abs()


# Converting the sharpened tensor to image
sharpened_image = kornia.utils.tensor_to_image(sharpened_tensor) 
difference_image = kornia.utils.tensor_to_image(difference)


# To display the input image, sharpened image and the difference image
fig, axs = plt.subplots(1, 3, figsize=(16, 10))
axs = axs.ravel()

axs[0].axis('off')
axs[0].set_title('image source')
axs[0].imshow(img)

axs[1].axis('off')
axs[1].set_title('sharpened')
axs[1].imshow(sharpened_image)

axs[2].axis('off')
axs[2].set_title('difference')
axs[2].imshow(difference_image)
plt.show()
