import albumentations as A

def get_filters():
    filters = [
            A.RandomBrightnessContrast(brightness_limit=0.2, contrast_limit=0.2, p=0.5),
            A.RandomGamma(gamma_limit=(80, 120), p=0.5),
            A.CLAHE(p=0.5),
            A.HueSaturationValue(p=0.5),
            A.RGBShift(p=0.5),
    ]

    return filters

