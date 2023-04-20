%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-ros2-ouster
Version:        0.5.0
Release:        3%{?dist}%{?release_suffix}
Summary:        ROS ros2_ouster package

License:        Apache-2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       libtins-devel
Requires:       pcl
Requires:       pcl-tools
Requires:       ros-iron-builtin-interfaces
Requires:       ros-iron-geometry-msgs
Requires:       ros-iron-launch
Requires:       ros-iron-launch-ros
Requires:       ros-iron-ouster-msgs
Requires:       ros-iron-pcl-conversions
Requires:       ros-iron-rclcpp
Requires:       ros-iron-rclcpp-components
Requires:       ros-iron-rclcpp-lifecycle
Requires:       ros-iron-sensor-msgs
Requires:       ros-iron-std-srvs
Requires:       ros-iron-tf2-geometry-msgs
Requires:       ros-iron-tf2-ros
Requires:       ros-iron-visualization-msgs
Requires:       ros-iron-ros-workspace
BuildRequires:  libtins-devel
BuildRequires:  pcl
BuildRequires:  pcl-tools
BuildRequires:  ros-iron-ament-cmake
BuildRequires:  ros-iron-builtin-interfaces
BuildRequires:  ros-iron-geometry-msgs
BuildRequires:  ros-iron-launch
BuildRequires:  ros-iron-launch-ros
BuildRequires:  ros-iron-ouster-msgs
BuildRequires:  ros-iron-pcl-conversions
BuildRequires:  ros-iron-rclcpp
BuildRequires:  ros-iron-rclcpp-components
BuildRequires:  ros-iron-rclcpp-lifecycle
BuildRequires:  ros-iron-sensor-msgs
BuildRequires:  ros-iron-std-srvs
BuildRequires:  ros-iron-tf2-geometry-msgs
BuildRequires:  ros-iron-tf2-ros
BuildRequires:  ros-iron-visualization-msgs
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-iron-ament-lint-auto
BuildRequires:  ros-iron-ament-lint-common
%endif

%description
ROS2 Drivers for the Ouster OS-1 Lidar

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/iron" \
    -DAMENT_PREFIX_PATH="/opt/ros/iron" \
    -DCMAKE_PREFIX_PATH="/opt/ros/iron" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Thu Apr 20 2023 Steve Macenski <stevenmacenski@gmail.com> - 0.5.0-3
- Autogenerated by Bloom

* Tue Mar 21 2023 Steve Macenski <stevenmacenski@gmail.com> - 0.5.0-2
- Autogenerated by Bloom

