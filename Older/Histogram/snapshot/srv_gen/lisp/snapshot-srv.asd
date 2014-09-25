
(cl:in-package :asdf)

(defsystem "snapshot-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "CompareHisto" :depends-on ("_package_CompareHisto"))
    (:file "_package_CompareHisto" :depends-on ("_package"))
  ))