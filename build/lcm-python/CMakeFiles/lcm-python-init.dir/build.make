# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


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

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pi/boat

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi/boat/build

# Utility rule file for lcm-python-init.

# Include the progress variables for this target.
include lcm-python/CMakeFiles/lcm-python-init.dir/progress.make

lcm-python/CMakeFiles/lcm-python-init: lib/python2.7/dist-packages/lcm/__init__.py


lib/python2.7/dist-packages/lcm/__init__.py: ../lcm-python/lcm/__init__.py
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/pi/boat/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating ../lib/python2.7/dist-packages/lcm/__init__.py"
	cd /home/pi/boat/build/lcm-python && /usr/bin/cmake -E make_directory /home/pi/boat/build/lib/python2.7/dist-packages/lcm
	cd /home/pi/boat/build/lcm-python && /usr/bin/cmake -E copy /home/pi/boat/lcm-python/lcm/__init__.py /home/pi/boat/build/lib/python2.7/dist-packages/lcm/__init__.py

lcm-python-init: lcm-python/CMakeFiles/lcm-python-init
lcm-python-init: lib/python2.7/dist-packages/lcm/__init__.py
lcm-python-init: lcm-python/CMakeFiles/lcm-python-init.dir/build.make

.PHONY : lcm-python-init

# Rule to build all files generated by this target.
lcm-python/CMakeFiles/lcm-python-init.dir/build: lcm-python-init

.PHONY : lcm-python/CMakeFiles/lcm-python-init.dir/build

lcm-python/CMakeFiles/lcm-python-init.dir/clean:
	cd /home/pi/boat/build/lcm-python && $(CMAKE_COMMAND) -P CMakeFiles/lcm-python-init.dir/cmake_clean.cmake
.PHONY : lcm-python/CMakeFiles/lcm-python-init.dir/clean

lcm-python/CMakeFiles/lcm-python-init.dir/depend:
	cd /home/pi/boat/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pi/boat /home/pi/boat/lcm-python /home/pi/boat/build /home/pi/boat/build/lcm-python /home/pi/boat/build/lcm-python/CMakeFiles/lcm-python-init.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lcm-python/CMakeFiles/lcm-python-init.dir/depend

