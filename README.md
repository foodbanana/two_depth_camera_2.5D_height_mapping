# ROS 2.5D height Mapping with RealSense Camera (d435)

이 프로젝트는 서울대학교 박재흥 교수님 Dyros 연구실에서 차준혁 박사과정님의 지도를 받으며 동계인턴을 진행한 것입니다. 참고로 d435f 카메라는 IMU 데이터가 없어 rviz상에서는 카메라가 고정되어 있다고 설정했습니다. (추후 tocabi의 imu센서 데이터를 입력으로 넣어줄 예정입니다)

depth camera의 point cloud 데이터를 이용해 height map을 만드는 코드입니다. 
set IMU data as zero because we used RealSense D435f camera for odometry (Pose With Covariance)
It can also be used without odometry to generate elevation maps

This is the main Robot-Centric Elevation Mapping node. It uses the distance sensor measurements and the pose and covariance of the robot to generate an elevation map with variance estimates.

deactivate pose data, allowing the node to be launched with the camera motionless.


### 실제 구동 사진
![실제 구동 사진](https://github.com/foodbanana/one_depth_camera_2.5D_height_mapping/blob/main/depth_image.png)
### 사진 + height map 사진
![사진 넣기](https://github.com/foodbanana/one_depth_camera_2.5D_height_mapping/blob/main/Screenshot%20from%202026-02-12%2013-50-38.png)

### step0.의존성(사전 다운로드)
- [ROS noetic](http://wiki.ros.org/ROS/Installation)
- [Realsense](https://github.com/IntelRealSense/realsense-ros/tree/ros1-legacy) (ROS Wrapper for Intel® RealSense™ Devices)
- [Grid Map](https://github.com/anybotics/grid_map) (grid map library for mobile robots)
- [kindr](http://github.com/anybotics/kindr) (kinematics and dynamics library for robotics),
- [kindr_ros](https://github.com/anybotics/kindr_ros) (ROS wrapper for kindr),
- [Point Cloud Library (PCL)](http://pointclouds.org/) (point cloud processing),
- [Eigen](http://eigen.tuxfamily.org) (linear algebra library)
- [Message Logger](https://github.com/ANYbotics/message_logger) (An Interface for Message Logging)
- [ANY Node](https://github.com/ANYbotics/any_node) (Set of wrapper packages to handle multi-threaded ROS nodes)
- [그 외] 터미널에 rosdep install --from-paths src --ignore-src -r -s 명령어를 쳐가며 의존성을 설치하는 것을 권장합니다

위의 의존성 파일들을 모두 완료하면 위의 rosdep install --from-paths src --ignore-src -r -s 명령어를 쳤을 때 아무것도 출력되지 않습니다. 그러면 그 후

    ```bash
    cd ~/<workspace이름>
    rosdep install --from-paths src --ignore-src -r -y
    ```
을 실행하면 됩니다




### step1. 코드 설치과정

1. 레포지토리 복사

    ```bash
    cd ~/<workspace이름>/src
    git clone https://github.com/foodbanana/one_depth_camera_2.5D_height_mapping.git
    ```

2. 패키지 빌드

    ```bash
    cd ~/<workspace이름>
    catkin_make

    source devel/setup.bash
    ```

### step2. 코드 실행
1. rtabmap 이용해서 카메라가 움직인다고 설정 시 (메인코드)
    ```bash
    roslaunch elevation_mapping elevationMap_realsense_d435i.launch pose:=true traversability:=false
    ```

2. rtabmap 이용해서 카메라가 움직임이 없고 base_link만 움직인다고 설정 시
    ```bash
    roslaunch elevation_mapping elevationMap_realsense_d435i.launch pose:=false traversability:=false
    ```


실행 시 rviz 화면이 뜨면 TF 설정을 올바르게 해주면 실행이 가능합니다

### step3. 세부 설정
1. map 크기 및 resolution
<작업폴더경로>/src/elevation-mapping-realsense-d435i/elevation_mapping/config/sensor_processors/realsense_d435i_rtabmap_pose.yaml
를 들어가면 line34부터 관련 값들이 존재한다






## License
[MIT License](LICENSE)

## 참고 및 도움
https://github.com/SobhanGhayedzadeh/elevation-mapping-realsense-d435i/blob/main/README.md

## 제 메일
christy201@daum.net
