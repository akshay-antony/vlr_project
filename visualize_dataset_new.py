import numpy as np
import math
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
from tqdm import tqdm


def plot_proposals_gt(gt, proposal, pc_feature):
    image = np.ones((800,700), dtype=np.uint8)
    image = image * 255
    gt = gt.astype(np.int32)
    proposal = proposal.astype(np.int32)

    pc_feature = pc_feature.numpy()
    pc_feature = pc_feature[::-1, :, :-1]

    val = 1 - pc_feature.max(axis=2)
    val = val.astype(np.uint8)
    

    fig, ax = plt.subplots()
    ax.imshow(image)

    # plotting gt boxes
    for i in range(gt.shape[0]):
        y1 = gt[i, 0]
        x1 = gt[i, 1]
        y2 = gt[i, 2]
        x2 = gt[i, 3]
        height = y2 - y1
        width = x2 - x1
        corner = (x1, y1)
        rect = patches.Rectangle(corner, width, height, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

    # plotting proposal boxes
    for i in range(proposal.shape[0]):
        y1 = proposal[i, 0]
        x1 = proposal[i, 1]
        y2 = proposal[i, 2]
        x2 = proposal[i, 3]
        height = y2 - y1
        width = x2 - x1
        corner = (x1, y1)
        rect = patches.Rectangle(corner, width, height, linewidth=1, edgecolor='b', facecolor='none')
        ax.add_patch(rect)
    
    plt.show()
    


if __name__ == "__main__":
    gt = np.array([[0, 0, 100, 100], [100, 100, 200, 200], [200, 200, 300, 300]])
    proposal = np.array([[0, 0, 50, 50], [100, 100, 100, 100], [200, 200, 400, 400]])
    plot_proposals_gt(gt, proposal)