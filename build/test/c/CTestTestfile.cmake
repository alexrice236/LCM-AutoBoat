# CMake generated Testfile for 
# Source directory: /home/pi/boat/test/c
# Build directory: /home/pi/boat/build/test/c
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(C::memq_test "/home/pi/boat/build/test/c/test-c-memq_test")
set_tests_properties(C::memq_test PROPERTIES  _BACKTRACE_TRIPLES "/home/pi/boat/test/c/CMakeLists.txt;18;add_test;/home/pi/boat/test/c/CMakeLists.txt;0;")
add_test(C::eventlog_test "/home/pi/boat/build/test/c/test-c-eventlog_test")
set_tests_properties(C::eventlog_test PROPERTIES  _BACKTRACE_TRIPLES "/home/pi/boat/test/c/CMakeLists.txt;19;add_test;/home/pi/boat/test/c/CMakeLists.txt;0;")
add_test(C::client_server "/usr/bin/python" "/home/pi/boat/test/c/../run_client_server_test.py" "/home/pi/boat/build/test/c/test-c-server" "/home/pi/boat/build/test/c/test-c-client")
set_tests_properties(C::client_server PROPERTIES  _BACKTRACE_TRIPLES "/home/pi/boat/test/c/CMakeLists.txt;22;add_test;/home/pi/boat/test/c/CMakeLists.txt;0;")
