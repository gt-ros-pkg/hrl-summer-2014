; Auto-generated. Do not edit!


(cl:in-package snapshot-srv)


;//! \htmlinclude CompareHisto-request.msg.html

(cl:defclass <CompareHisto-request> (roslisp-msg-protocol:ros-message)
  ((C
    :reader C
    :initarg :C
    :type cl:integer
    :initform 0))
)

(cl:defclass CompareHisto-request (<CompareHisto-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CompareHisto-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CompareHisto-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name snapshot-srv:<CompareHisto-request> is deprecated: use snapshot-srv:CompareHisto-request instead.")))

(cl:ensure-generic-function 'C-val :lambda-list '(m))
(cl:defmethod C-val ((m <CompareHisto-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader snapshot-srv:C-val is deprecated.  Use snapshot-srv:C instead.")
  (C m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CompareHisto-request>) ostream)
  "Serializes a message object of type '<CompareHisto-request>"
  (cl:let* ((signed (cl:slot-value msg 'C)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CompareHisto-request>) istream)
  "Deserializes a message object of type '<CompareHisto-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'C) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CompareHisto-request>)))
  "Returns string type for a service object of type '<CompareHisto-request>"
  "snapshot/CompareHistoRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CompareHisto-request)))
  "Returns string type for a service object of type 'CompareHisto-request"
  "snapshot/CompareHistoRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CompareHisto-request>)))
  "Returns md5sum for a message object of type '<CompareHisto-request>"
  "d2c556f88afc596e8c98cf52cd60a2a5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CompareHisto-request)))
  "Returns md5sum for a message object of type 'CompareHisto-request"
  "d2c556f88afc596e8c98cf52cd60a2a5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CompareHisto-request>)))
  "Returns full string definition for message of type '<CompareHisto-request>"
  (cl:format cl:nil "int64 C~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CompareHisto-request)))
  "Returns full string definition for message of type 'CompareHisto-request"
  (cl:format cl:nil "int64 C~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CompareHisto-request>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CompareHisto-request>))
  "Converts a ROS message object to a list"
  (cl:list 'CompareHisto-request
    (cl:cons ':C (C msg))
))
;//! \htmlinclude CompareHisto-response.msg.html

(cl:defclass <CompareHisto-response> (roslisp-msg-protocol:ros-message)
  ((R
    :reader R
    :initarg :R
    :type cl:integer
    :initform 0))
)

(cl:defclass CompareHisto-response (<CompareHisto-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CompareHisto-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CompareHisto-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name snapshot-srv:<CompareHisto-response> is deprecated: use snapshot-srv:CompareHisto-response instead.")))

(cl:ensure-generic-function 'R-val :lambda-list '(m))
(cl:defmethod R-val ((m <CompareHisto-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader snapshot-srv:R-val is deprecated.  Use snapshot-srv:R instead.")
  (R m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CompareHisto-response>) ostream)
  "Serializes a message object of type '<CompareHisto-response>"
  (cl:let* ((signed (cl:slot-value msg 'R)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CompareHisto-response>) istream)
  "Deserializes a message object of type '<CompareHisto-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'R) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CompareHisto-response>)))
  "Returns string type for a service object of type '<CompareHisto-response>"
  "snapshot/CompareHistoResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CompareHisto-response)))
  "Returns string type for a service object of type 'CompareHisto-response"
  "snapshot/CompareHistoResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CompareHisto-response>)))
  "Returns md5sum for a message object of type '<CompareHisto-response>"
  "d2c556f88afc596e8c98cf52cd60a2a5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CompareHisto-response)))
  "Returns md5sum for a message object of type 'CompareHisto-response"
  "d2c556f88afc596e8c98cf52cd60a2a5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CompareHisto-response>)))
  "Returns full string definition for message of type '<CompareHisto-response>"
  (cl:format cl:nil "int64 R~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CompareHisto-response)))
  "Returns full string definition for message of type 'CompareHisto-response"
  (cl:format cl:nil "int64 R~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CompareHisto-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CompareHisto-response>))
  "Converts a ROS message object to a list"
  (cl:list 'CompareHisto-response
    (cl:cons ':R (R msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'CompareHisto)))
  'CompareHisto-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'CompareHisto)))
  'CompareHisto-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CompareHisto)))
  "Returns string type for a service object of type '<CompareHisto>"
  "snapshot/CompareHisto")