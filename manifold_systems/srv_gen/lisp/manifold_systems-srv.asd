
(cl:in-package :asdf)

(defsystem "manifold_systems-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Converse" :depends-on ("_package_Converse"))
    (:file "_package_Converse" :depends-on ("_package"))
    (:file "Compute" :depends-on ("_package_Compute"))
    (:file "_package_Compute" :depends-on ("_package"))
  ))