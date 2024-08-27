import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('210023K_SrcImage.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create the processed images
negative_image = 255 - gray_image
bright_image = np.clip(gray_image * 1.2, 0, 255).astype(np.uint8)
contrast_reduced_image = np.clip((gray_image - 125) * (50 / 255) + 125, 125, 175).astype(np.uint8)
fourbpp_image = np.floor_divide(gray_image, 16) * 16
mirror_image = cv2.flip(gray_image, 1)

#list of images
img_list = [(gray_image, 'Original Grayscale'),(negative_image, 'Negative Image'),(bright_image, 'Increased Brightness'),
            (contrast_reduced_image, 'Reduced Contrast'),(fourbpp_image, '4bpp Image'),(mirror_image, 'Vertical Mirror Image')]

#create the subplots
fig, axs = plt.subplots(2, 3, figsize=(10, 7))

# Populate the subplots 
for i in range(2):
    for j in range(3):
        index = i * 3 + j  
        axs[i, j].imshow(img_list[index][0], cmap="gray")
        cv2.imwrite('./Outputs/210023K_OPImage_grid({},{}).jpg'.format(i+1,j+1), img_list[index][0])
        axs[i, j].set_title(img_list[index][1])
        axs[i, j].axis("off")

# Display the plot
#plt.tight_layout()
#plt.show()        

#save the plot as image
fig.savefig('./Outputs/210023K_SubPlot.jpg')

