FILE(REMOVE_RECURSE
  "../srv_gen"
  "../src/RobotCode/srv"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_lisp"
  "../srv_gen/lisp/handler.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_handler.lisp"
  "../srv_gen/lisp/test.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_test.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
