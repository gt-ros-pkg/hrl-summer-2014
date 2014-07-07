FILE(REMOVE_RECURSE
  "../srv_gen"
  "../src/RobotCode/srv"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/RobotCode/srv/__init__.py"
  "../src/RobotCode/srv/_handler.py"
  "../src/RobotCode/srv/_test.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
