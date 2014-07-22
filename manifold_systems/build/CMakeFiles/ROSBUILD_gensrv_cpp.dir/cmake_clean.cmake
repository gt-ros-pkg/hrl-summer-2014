FILE(REMOVE_RECURSE
  "../srv_gen"
  "../src/manifold_systems/srv"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_cpp"
  "../srv_gen/cpp/include/manifold_systems/Converse.h"
  "../srv_gen/cpp/include/manifold_systems/Compute.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
