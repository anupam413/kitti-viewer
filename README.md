
# 3D Detection & Tracking Viewer
This project was developed for view 3D object detection and tracking results.
It supports rendering 3D bounding boxes as car models and rendering boxes on images.

## Prepare data 
* Kitti detection dataset
```
# For Kitti Detection Dataset         
└── kitti_detection
       ├── testing 
       |      ├──calib
       |      ├──image_2
       |      ├──label_2
       |      └──velodyne      
       └── training
              ├──calib
              ├──image_2
              ├──label_2
              └──velodyne 
```
* Kitti tracking dataset
```
# For Kitti Tracking Dataset         
└── kitti_tracking
       ├── testing 
       |      ├──calib
       |      |    ├──0000.txt
       |      |    ├──....txt
       |      |    └──0028.txt
       |      ├──image_02
       |      |    ├──0000
       |      |    ├──....
       |      |    └──0028
       |      ├──label_02
       |      |    ├──0000.txt
       |      |    ├──....txt
       |      |    └──0028.txt
       |      └──velodyne
       |           ├──0000
       |           ├──....
       |           └──0028      
       └── training # the structure is same as testing set
              ├──calib
              ├──image_02
              ├──label_02
              └──velodyne 
```
