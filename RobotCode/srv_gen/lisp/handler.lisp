; Auto-generated. Do not edit!


(cl:in-package RobotCode-srv)


;//! \htmlinclude handler-request.msg.html

(cl:defclass <handler-request> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:integer
    :initform 0))
)

(cl:defclass handler-request (<handler-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <handler-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'handler-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name RobotCode-srv:<handler-request> is deprecated: use RobotCode-srv:handler-request instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <handler-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader RobotCode-srv:x-val is deprecated.  Use RobotCode-srv:x instead.")
  (x m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <handler-request>) ostream)
  "Serializes a message object of type '<handler-request>"
  (cl:let* ((signed (cl:slot-value msg 'x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <handler-request>) istream)
  "Deserializes a message object of type '<handler-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'x) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<handler-request>)))
  "Returns string type for a service object of type '<handler-request>"
  "RobotCode/handlerRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'handler-request)))
  "Returns string type for a service object of type 'handler-request"
  "RobotCode/handlerRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<handler-request>)))
  "Returns md5sum for a message object of type '<handler-request>"
  "b429044e1360891965aa67e074722c0e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'handler-request)))
  "Returns md5sum for a message object of type 'handler-request"
  "b429044e1360891965aa67e074722c0e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<handler-request>)))
  "Returns full string definition for message of type '<handler-request>"
  (cl:format cl:nil "int64 x~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'handler-request)))
  "Returns full string definition for message of type 'handler-request"
  (cl:format cl:nil "int64 x~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <handler-request>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <handler-request>))
  "Converts a ROS message object to a list"
  (cl:list 'handler-request
    (cl:cons ':x (x msg))
))
;//! \htmlinclude handler-response.msg.html

(cl:defclass <handler-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass handler-response (<handler-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <handler-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'handler-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name RobotCode-srv:<handler-response> is deprecated: use RobotCode-srv:handler-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <handler-response>) ostream)
  "Serializes a message object of type '<handler-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <handler-response>) istream)
  "Deserializes a message object of type '<handler-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<handler-response>)))
  "Returns string type for a service object of type '<handler-response>"
  "RobotCode/handlerResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'handler-response)))
  "Returns string type for a service object of type 'handler-response"
  "RobotCode/handlerResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<handler-response>)))
  "Returns md5sum for a message object of type '<handler-response>"
  "b429044e1360891965aa67e074722c0e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'handler-response)))
  "Returns md5sum for a message object of type 'handler-response"
  "b429044e1360891965aa67e074722c0e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<handler-response>)))
  "Returns full string definition for message of type '<handler-response>"
  (cl:format cl:nil "~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'handler-response)))
  "Returns full string definition for message of type 'handler-response"
  (cl:format cl:nil "~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <handler-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <handler-response>))
  "Converts a ROS message object to a list"
  (cl:list 'handler-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'handler)))
  'handler-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'handler)))
  'handler-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'handler)))
  "Returns string type for a service object of type '<handler>"
  "RobotCode/handler")