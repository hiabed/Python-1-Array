import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    weights = np.array(weight) # convert the weight list to a numpy array
    heights = np.array(height)
    bmi = weights / (heights ** 2)
    return bmi

# def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
