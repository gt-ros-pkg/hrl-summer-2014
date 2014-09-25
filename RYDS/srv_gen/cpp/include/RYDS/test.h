/* Auto-generated by genmsg_cpp for file /home/mrich7/fuerte_workspace/RYDS/srv/test.srv */
#ifndef RYDS_SERVICE_TEST_H
#define RYDS_SERVICE_TEST_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "ros/service_traits.h"




namespace RYDS
{
template <class ContainerAllocator>
struct testRequest_ {
  typedef testRequest_<ContainerAllocator> Type;

  testRequest_()
  : x(0)
  {
  }

  testRequest_(const ContainerAllocator& _alloc)
  : x(0)
  {
  }

  typedef int64_t _x_type;
  int64_t x;


  typedef boost::shared_ptr< ::RYDS::testRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::RYDS::testRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct testRequest
typedef  ::RYDS::testRequest_<std::allocator<void> > testRequest;

typedef boost::shared_ptr< ::RYDS::testRequest> testRequestPtr;
typedef boost::shared_ptr< ::RYDS::testRequest const> testRequestConstPtr;


template <class ContainerAllocator>
struct testResponse_ {
  typedef testResponse_<ContainerAllocator> Type;

  testResponse_()
  {
  }

  testResponse_(const ContainerAllocator& _alloc)
  {
  }


  typedef boost::shared_ptr< ::RYDS::testResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::RYDS::testResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct testResponse
typedef  ::RYDS::testResponse_<std::allocator<void> > testResponse;

typedef boost::shared_ptr< ::RYDS::testResponse> testResponsePtr;
typedef boost::shared_ptr< ::RYDS::testResponse const> testResponseConstPtr;

struct test
{

typedef testRequest Request;
typedef testResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct test
} // namespace RYDS

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::RYDS::testRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::RYDS::testRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::RYDS::testRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b429044e1360891965aa67e074722c0e";
  }

  static const char* value(const  ::RYDS::testRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xb429044e13608919ULL;
  static const uint64_t static_value2 = 0x65aa67e074722c0eULL;
};

template<class ContainerAllocator>
struct DataType< ::RYDS::testRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "RYDS/testRequest";
  }

  static const char* value(const  ::RYDS::testRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::RYDS::testRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "int64 x\n\
\n\
";
  }

  static const char* value(const  ::RYDS::testRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::RYDS::testRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::RYDS::testResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::RYDS::testResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::RYDS::testResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const  ::RYDS::testResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::RYDS::testResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "RYDS/testResponse";
  }

  static const char* value(const  ::RYDS::testResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::RYDS::testResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
\n\
\n\
";
  }

  static const char* value(const  ::RYDS::testResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::RYDS::testResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::RYDS::testRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.x);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct testRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::RYDS::testResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct testResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<RYDS::test> {
  static const char* value() 
  {
    return "b429044e1360891965aa67e074722c0e";
  }

  static const char* value(const RYDS::test&) { return value(); } 
};

template<>
struct DataType<RYDS::test> {
  static const char* value() 
  {
    return "RYDS/test";
  }

  static const char* value(const RYDS::test&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<RYDS::testRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b429044e1360891965aa67e074722c0e";
  }

  static const char* value(const RYDS::testRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<RYDS::testRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "RYDS/test";
  }

  static const char* value(const RYDS::testRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<RYDS::testResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b429044e1360891965aa67e074722c0e";
  }

  static const char* value(const RYDS::testResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<RYDS::testResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "RYDS/test";
  }

  static const char* value(const RYDS::testResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // RYDS_SERVICE_TEST_H

