FILE(REMOVE_RECURSE
  "../srv_gen"
  "../src/RYDS/srv"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_lisp"
  "../srv_gen/lisp/handler.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_handler.lisp"
  "../srv_gen/lisp/test.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_test.lisp"
  "../srv_gen/lisp/CompareHisto.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_CompareHisto.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
