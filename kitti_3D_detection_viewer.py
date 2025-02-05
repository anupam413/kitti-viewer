from viewer.viewer import Viewer
import numpy as np
from dataset.kitti_dataset import KittiDetectionDataset

def kitti_viewer():
    root="./data/kitti_detection/training"
    label_path = "./data/kitti_detection/training/label_2"
    dataset = KittiDetectionDataset(root,label_path)

    vi = Viewer(box_type="Kitti")
    vi.set_ob_color_map('gnuplot')

    for i in range(len(dataset)):
        P2, V2C, points, image, ini_labels, labels, label_names = dataset[i]

        # print("da", dataset[i])
        # print("ini",ini_labels)
        # mask = any(label in ["Car"] for label in label_names)
        # mask = label_names == "Car" 
        mask = (label_names == "Car") | (label_names == "Pedestrian") | (label_names == "Cyclist") | (label_names == "Truck")  \
                | (label_names == "Van") | (label_names == "Tram") | (label_names == "Misc") | (label_names == "Person_sitting")

        # print("mask", mask)
        labels = labels[mask]
        ini_labels = ini_labels[mask]
        label_names = label_names[mask]

        vi.add_points(points[:,:3],scatter_filed=points[:,2],color_map_name='viridis')
        vi.add_3D_boxes(labels, box_info=label_names)
        vi.add_3D_cars(labels, box_info=label_names)
        vi.add_image(image)
        vi.set_extrinsic_mat(V2C)
        vi.set_intrinsic_mat(P2)
        vi.show_2D(ini_labels=ini_labels)
        vi.show_3D(ini_labels=ini_labels)


if __name__ == '__main__':
    kitti_viewer()
