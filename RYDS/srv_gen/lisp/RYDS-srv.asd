
(cl:in-package :asdf)

(defsystem "RYDS-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "handler" :depends-on ("_package_handler"))
    (:file "_package_handler" :depends-on ("_package"))
    (:file "test" :depends-on ("_package_test"))
    (:file "_package_test" :depends-on ("_package"))
    (:file "CompareHisto" :depends-on ("_package_CompareHisto"))
    (:file "_package_CompareHisto" :depends-on ("_package"))
  ))