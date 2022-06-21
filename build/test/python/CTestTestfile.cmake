# CMake generated Testfile for 
# Source directory: /home/pi/boat/test/python
# Build directory: /home/pi/boat/build/test/python
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(Python::bool_test "/usr/bin/cmake" "-E" "env" "PYTHONPATH=/home/pi/boat/build/test/types:/home/pi/boat/build/lib/python2.7/dist-packages" "/usr/bin/python" "/home/pi/boat/test/python/bool_test.py")
set_tests_properties(Python::bool_test PROPERTIES  _BACKTRACE_TRIPLES "/home/pi/boat/test/python/CMakeLists.txt;17;add_test;/home/pi/boat/test/python/CMakeLists.txt;22;add_python_test;/home/pi/boat/test/python/CMakeLists.txt;0;")
add_test(Python::byte_array_test "/usr/bin/cmake" "-E" "env" "PYTHONPATH=/home/pi/boat/build/test/types:/home/pi/boat/build/lib/python2.7/dist-packages" "/usr/bin/python" "/home/pi/boat/test/python/byte_array_test.py")
set_tests_properties(Python::byte_array_test PROPERTIES  _BACKTRACE_TRIPLES "/home/pi/boat/test/python/CMakeLists.txt;17;add_test;/home/pi/boat/test/python/CMakeLists.txt;23;add_python_test;/home/pi/boat/test/python/CMakeLists.txt;0;")
add_test(Python::lcm_file_test "/usr/bin/cmake" "-E" "env" "PYTHONPATH=/home/pi/boat/build/test/types:/home/pi/boat/build/lib/python2.7/dist-packages" "/usr/bin/python" "/home/pi/boat/test/python/lcm_file_test.py")
set_tests_properties(Python::lcm_file_test PROPERTIES  _BACKTRACE_TRIPLES "/home/pi/boat/test/python/CMakeLists.txt;17;add_test;/home/pi/boat/test/python/CMakeLists.txt;24;add_python_test;/home/pi/boat/test/python/CMakeLists.txt;0;")
add_test(Python::lcm_memq_test "/usr/bin/cmake" "-E" "env" "PYTHONPATH=/home/pi/boat/build/test/types:/home/pi/boat/build/lib/python2.7/dist-packages" "/usr/bin/python" "/home/pi/boat/test/python/lcm_memq_test.py")
set_tests_properties(Python::lcm_memq_test PROPERTIES  _BACKTRACE_TRIPLES "/home/pi/boat/test/python/CMakeLists.txt;17;add_test;/home/pi/boat/test/python/CMakeLists.txt;25;add_python_test;/home/pi/boat/test/python/CMakeLists.txt;0;")
add_test(Python::lcm_thread_test "/usr/bin/cmake" "-E" "env" "PYTHONPATH=/home/pi/boat/build/test/types:/home/pi/boat/build/lib/python2.7/dist-packages" "/usr/bin/python" "/home/pi/boat/test/python/lcm_thread_test.py")
set_tests_properties(Python::lcm_thread_test PROPERTIES  _BACKTRACE_TRIPLES "/home/pi/boat/test/python/CMakeLists.txt;17;add_test;/home/pi/boat/test/python/CMakeLists.txt;26;add_python_test;/home/pi/boat/test/python/CMakeLists.txt;0;")
add_test(Python::client_server "/usr/bin/cmake" "-E" "env" "PYTHONPATH=/home/pi/boat/build/test/types:/home/pi/boat/build/lib/python2.7/dist-packages" "/usr/bin/python" "/home/pi/boat/test/run_client_server_test.py" "/home/pi/boat/build/test/c/test-c-server" "/usr/bin/python" "/home/pi/boat/test/python/client.py")
set_tests_properties(Python::client_server PROPERTIES  _BACKTRACE_TRIPLES "/home/pi/boat/test/python/CMakeLists.txt;17;add_test;/home/pi/boat/test/python/CMakeLists.txt;28;add_python_test;/home/pi/boat/test/python/CMakeLists.txt;0;")
