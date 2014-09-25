FILE(REMOVE_RECURSE
  "../srv_gen"
  "../src/RYDS/srv"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/RYDS/srv/__init__.py"
  "../src/RYDS/srv/_handler.py"
  "../src/RYDS/srv/_test.py"
  "../src/RYDS/srv/_CompareHisto.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
