# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/dave/git/hrl-summer-2014/Histogram/snapshot

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/dave/git/hrl-summer-2014/Histogram/snapshot/build

# Utility rule file for ROSBUILD_gensrv_py.

# Include the progress variables for this target.
include CMakeFiles/ROSBUILD_gensrv_py.dir/progress.make

CMakeFiles/ROSBUILD_gensrv_py: ../src/snapshot/srv/__init__.py

../src/snapshot/srv/__init__.py: ../src/snapshot/srv/_CompareHisto.py
	$(CMAKE_COMMAND) -E cmake_progress_report /home/dave/git/hrl-summer-2014/Histogram/snapshot/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating ../src/snapshot/srv/__init__.py"
	/opt/ros/fuerte/share/rospy/rosbuild/scripts/gensrv_py.py --initpy /home/dave/git/hrl-summer-2014/Histogram/snapshot/srv/CompareHisto.srv

../src/snapshot/srv/_CompareHisto.py: ../srv/CompareHisto.srv
../src/snapshot/srv/_CompareHisto.py: /opt/ros/fuerte/share/rospy/rosbuild/scripts/gensrv_py.py
../src/snapshot/srv/_CompareHisto.py: /opt/ros/fuerte/share/roslib/bin/gendeps
../src/snapshot/srv/_CompareHisto.py: ../manifest.xml
../src/snapshot/srv/_CompareHisto.py: /opt/ros/fuerte/share/roslang/manifest.xml
../src/snapshot/srv/_CompareHisto.py: /opt/ros/fuerte/share/rospy/manifest.xml
../src/snapshot/srv/_CompareHisto.py: /opt/ros/fuerte/share/std_msgs/manifest.xml
	$(CMAKE_COMMAND) -E cmake_progress_report /home/dave/git/hrl-summer-2014/Histogram/snapshot/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating ../src/snapshot/srv/_CompareHisto.py"
	/opt/ros/fuerte/share/rospy/rosbuild/scripts/gensrv_py.py --noinitpy /home/dave/git/hrl-summer-2014/Histogram/snapshot/srv/CompareHisto.srv

ROSBUILD_gensrv_py: CMakeFiles/ROSBUILD_gensrv_py
ROSBUILD_gensrv_py: ../src/snapshot/srv/__init__.py
ROSBUILD_gensrv_py: ../src/snapshot/srv/_CompareHisto.py
ROSBUILD_gensrv_py: CMakeFiles/ROSBUILD_gensrv_py.dir/build.make
.PHONY : ROSBUILD_gensrv_py

# Rule to build all files generated by this target.
CMakeFiles/ROSBUILD_gensrv_py.dir/build: ROSBUILD_gensrv_py
.PHONY : CMakeFiles/ROSBUILD_gensrv_py.dir/build

CMakeFiles/ROSBUILD_gensrv_py.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean.cmake
.PHONY : CMakeFiles/ROSBUILD_gensrv_py.dir/clean

CMakeFiles/ROSBUILD_gensrv_py.dir/depend:
	cd /home/dave/git/hrl-summer-2014/Histogram/snapshot/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/dave/git/hrl-summer-2014/Histogram/snapshot /home/dave/git/hrl-summer-2014/Histogram/snapshot /home/dave/git/hrl-summer-2014/Histogram/snapshot/build /home/dave/git/hrl-summer-2014/Histogram/snapshot/build /home/dave/git/hrl-summer-2014/Histogram/snapshot/build/CMakeFiles/ROSBUILD_gensrv_py.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/ROSBUILD_gensrv_py.dir/depend
