# CMake generated Testfile for 
# Source directory: /home/dyros21/260126_tw_ws/src/kindr_ros/kindr_ros
# Build directory: /home/dyros21/260126_tw_ws/build/kindr_ros
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_kindr_ros_gtest_test_kindr_ros "/home/dyros21/260126_tw_ws/build/kindr_ros/catkin_generated/env_cached.sh" "/usr/bin/python3" "/opt/ros/noetic/share/catkin/cmake/test/run_tests.py" "/home/dyros21/260126_tw_ws/build/kindr_ros/test_results/kindr_ros/gtest-test_kindr_ros.xml" "--working-dir" "/home/dyros21/260126_tw_ws/src/kindr_ros/kindr_ros/test" "--return-code" "/home/dyros21/260126_tw_ws/devel/.private/kindr_ros/lib/kindr_ros/test_kindr_ros --gtest_output=xml:/home/dyros21/260126_tw_ws/build/kindr_ros/test_results/kindr_ros/gtest-test_kindr_ros.xml")
set_tests_properties(_ctest_kindr_ros_gtest_test_kindr_ros PROPERTIES  _BACKTRACE_TRIPLES "/opt/ros/noetic/share/catkin/cmake/test/tests.cmake;160;add_test;/opt/ros/noetic/share/catkin/cmake/test/gtest.cmake;98;catkin_run_tests_target;/opt/ros/noetic/share/catkin/cmake/test/gtest.cmake;37;_catkin_add_google_test;/home/dyros21/260126_tw_ws/src/kindr_ros/kindr_ros/CMakeLists.txt;38;catkin_add_gtest;/home/dyros21/260126_tw_ws/src/kindr_ros/kindr_ros/CMakeLists.txt;0;")
subdirs("gtest")
