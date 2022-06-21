# CMake generated Testfile for 
# Source directory: /home/pi/boat/test/java
# Build directory: /home/pi/boat/build/test/java
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(Java::client_server "/usr/bin/python" "/home/pi/boat/test/java/../run_client_server_test.py" "/home/pi/boat/build/test/c/test-c-server" "/usr/bin/java" "-cp" "/home/pi/boat/build/test/java/lcm-test.jar:/home/pi/boat/build/test/types/lcm-test-types.jar:/home/pi/boat/build/lcm-java/lcm.jar:/home/pi/boat/build/test/java/hamcrest-core-1.3/hamcrest-core-1.3.jar:/home/pi/boat/build/test/java/junit-4.11/junit-4.11.jar" "LcmTestClient")
set_tests_properties(Java::client_server PROPERTIES  _BACKTRACE_TRIPLES "/home/pi/boat/test/java/CMakeLists.txt;25;add_test;/home/pi/boat/test/java/CMakeLists.txt;0;")
subdirs("hamcrest-core-1.3")
subdirs("junit-4.11")
