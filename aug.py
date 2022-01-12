from PIL import Image
import os

path_orign = 'training_hr_images/'
path_augment = 'training_hr_images_augment/'
files = os.listdir(path_orign)

count = 0
for file in files:
    print(f'Preocessing #{count}......')
    img = Image.open(path_orign + file)
    
    img_rot90 = img.rotate(90)
    img_rot90.save(path_augment + file.replace('.png', '_rot90.png'))

    img_rot180 = img.rotate(180)
    img_rot180.save(path_augment + file.replace('.png', '_rot180.png'))

    img_rot270 = img.rotate(270)
    img_rot270.save(path_augment + file.replace('.png', '_rot270.png'))

    img_flip_horizontal = img.transpose(Image.FLIP_LEFT_RIGHT)
    img_flip_horizontal.save(path_augment + file.replace('.png', '_flipLR.png'))

    img_flip_vertical = img.transpose(Image.FLIP_TOP_BOTTOM)
    img_flip_vertical.save(path_augment + file.replace('.png', '_flipTB.png'))

    count += 1
print(f'Finish processing {count} images.')