FILE(REMOVE_RECURSE
  "../srv_gen"
  "../src/RobotCode/srv"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_cpp"
  "../srv_gen/cpp/include/RobotCode/handler.h"
  "../srv_gen/cpp/include/RobotCode/test.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
