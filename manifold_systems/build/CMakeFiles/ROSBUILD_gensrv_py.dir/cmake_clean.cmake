FILE(REMOVE_RECURSE
  "../srv_gen"
  "../src/manifold_systems/srv"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/manifold_systems/srv/__init__.py"
  "../src/manifold_systems/srv/_Converse.py"
  "../src/manifold_systems/srv/_Compute.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
