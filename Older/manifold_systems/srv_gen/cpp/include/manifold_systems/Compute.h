/* Auto-generated by genmsg_cpp for file /home/caleb/ros_workspace/sandbox/manifold_systems/srv/Compute.srv */
#ifndef MANIFOLD_SYSTEMS_SERVICE_COMPUTE_H
#define MANIFOLD_SYSTEMS_SERVICE_COMPUTE_H
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




namespace manifold_systems
{
template <class ContainerAllocator>
struct ComputeRequest_ {
  typedef ComputeRequest_<ContainerAllocator> Type;

  ComputeRequest_()
  : fx(0.0)
  , fy(0.0)
  , fz(0.0)
  , tx(0.0)
  , ty(0.0)
  , tz(0.0)
  {
  }

  ComputeRequest_(const ContainerAllocator& _alloc)
  : fx(0.0)
  , fy(0.0)
  , fz(0.0)
  , tx(0.0)
  , ty(0.0)
  , tz(0.0)
  {
  }

  typedef double _fx_type;
  double fx;

  typedef double _fy_type;
  double fy;

  typedef double _fz_type;
  double fz;

  typedef double _tx_type;
  double tx;

  typedef double _ty_type;
  double ty;

  typedef double _tz_type;
  double tz;


  typedef boost::shared_ptr< ::manifold_systems::ComputeRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::manifold_systems::ComputeRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ComputeRequest
typedef  ::manifold_systems::ComputeRequest_<std::allocator<void> > ComputeRequest;

typedef boost::shared_ptr< ::manifold_systems::ComputeRequest> ComputeRequestPtr;
typedef boost::shared_ptr< ::manifold_systems::ComputeRequest const> ComputeRequestConstPtr;


template <class ContainerAllocator>
struct ComputeResponse_ {
  typedef ComputeResponse_<ContainerAllocator> Type;

  ComputeResponse_()
  : x(0.0)
  , y(0.0)
  {
  }

  ComputeResponse_(const ContainerAllocator& _alloc)
  : x(0.0)
  , y(0.0)
  {
  }

  typedef double _x_type;
  double x;

  typedef double _y_type;
  double y;


  typedef boost::shared_ptr< ::manifold_systems::ComputeResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::manifold_systems::ComputeResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ComputeResponse
typedef  ::manifold_systems::ComputeResponse_<std::allocator<void> > ComputeResponse;

typedef boost::shared_ptr< ::manifold_systems::ComputeResponse> ComputeResponsePtr;
typedef boost::shared_ptr< ::manifold_systems::ComputeResponse const> ComputeResponseConstPtr;

struct Compute
{

typedef ComputeRequest Request;
typedef ComputeResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct Compute
} // namespace manifold_systems

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::manifold_systems::ComputeRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::manifold_systems::ComputeRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::manifold_systems::ComputeRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "e6da1f4bb463d64b2399f31589512a6f";
  }

  static const char* value(const  ::manifold_systems::ComputeRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xe6da1f4bb463d64bULL;
  static const uint64_t static_value2 = 0x2399f31589512a6fULL;
};

template<class ContainerAllocator>
struct DataType< ::manifold_systems::ComputeRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "manifold_systems/ComputeRequest";
  }

  static const char* value(const  ::manifold_systems::ComputeRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::manifold_systems::ComputeRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "float64 fx\n\
float64 fy\n\
float64 fz\n\
float64 tx\n\
float64 ty\n\
float64 tz\n\
\n\
";
  }

  static const char* value(const  ::manifold_systems::ComputeRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::manifold_systems::ComputeRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::manifold_systems::ComputeResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::manifold_systems::ComputeResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::manifold_systems::ComputeResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "209f516d3eb691f0663e25cb750d67c1";
  }

  static const char* value(const  ::manifold_systems::ComputeResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x209f516d3eb691f0ULL;
  static const uint64_t static_value2 = 0x663e25cb750d67c1ULL;
};

template<class ContainerAllocator>
struct DataType< ::manifold_systems::ComputeResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "manifold_systems/ComputeResponse";
  }

  static const char* value(const  ::manifold_systems::ComputeResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::manifold_systems::ComputeResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "float64 x\n\
float64 y\n\
\n\
\n\
";
  }

  static const char* value(const  ::manifold_systems::ComputeResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::manifold_systems::ComputeResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::manifold_systems::ComputeRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.fx);
    stream.next(m.fy);
    stream.next(m.fz);
    stream.next(m.tx);
    stream.next(m.ty);
    stream.next(m.tz);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ComputeRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::manifold_systems::ComputeResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.x);
    stream.next(m.y);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ComputeResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<manifold_systems::Compute> {
  static const char* value() 
  {
    return "b41c040ce5a6875183b2d3d611a6f73d";
  }

  static const char* value(const manifold_systems::Compute&) { return value(); } 
};

template<>
struct DataType<manifold_systems::Compute> {
  static const char* value() 
  {
    return "manifold_systems/Compute";
  }

  static const char* value(const manifold_systems::Compute&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<manifold_systems::ComputeRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b41c040ce5a6875183b2d3d611a6f73d";
  }

  static const char* value(const manifold_systems::ComputeRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<manifold_systems::ComputeRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "manifold_systems/Compute";
  }

  static const char* value(const manifold_systems::ComputeRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<manifold_systems::ComputeResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b41c040ce5a6875183b2d3d611a6f73d";
  }

  static const char* value(const manifold_systems::ComputeResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<manifold_systems::ComputeResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "manifold_systems/Compute";
  }

  static const char* value(const manifold_systems::ComputeResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // MANIFOLD_SYSTEMS_SERVICE_COMPUTE_H

