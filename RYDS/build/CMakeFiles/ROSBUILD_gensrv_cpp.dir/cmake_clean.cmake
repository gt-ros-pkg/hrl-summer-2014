FILE(REMOVE_RECURSE
  "../srv_gen"
  "../src/RYDS/srv"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_cpp"
  "../srv_gen/cpp/include/RYDS/handler.h"
  "../srv_gen/cpp/include/RYDS/test.h"
  "../srv_gen/cpp/include/RYDS/CompareHisto.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
