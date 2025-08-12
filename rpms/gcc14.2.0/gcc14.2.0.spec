Name: gcc
Version: 14.2.0
Release: 1%{dist}
License: GNU GPL
Summary: The GNU Binutils are a collection of binary tools.
URL: https://gcc.gnu.org/

Source0: %{name}-%{version}.tar.gz
Source1: mpfr-4.2.1.tar.xz
Source2: gmp-6.3.0.tar.xz
Source3: mpc-1.3.1.tar.gz

BuildRequires: gcc
BuildRequires: make

%description
The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Ada, and Go. It also includes libraries for these languages.

%prep
# Unpack the source tarballs
%setup -q -n %{name}-%{version}
%setup -q -T -D -a 1 -n %{name}-%{version} \
    -a 2 -n %{name}-%{version} \
    -a 3 -n %{name}-%{version}

# Change the directory names to match the expected structure
mv mpfr-4.2.1 mpfr
mv gmp-6.3.0 gmp
mv mpc-1.3.1 mpc
%build
# Set LFS and LFS_TGT variables if not already set
: ${LFS:=/mnt/lfs}
: ${LFS_TGT:=$(uname -m)-lfs-linux-gnu}


# Set the default directory for 64-bit libraries to lib
case $(uname -m) in
x86_64)
    sed -e '/m64=/s/lib64/lib/' \
        -i.orig gcc/config/i386/t-linux64
    ;;
esac
# Create a build directory
mkdir -p build

pushd build

../configure                  \
    --target=$LFS_TGT         \
    --prefix=$LFS/tools       \
    --with-glibc-version=2.41 \
    --with-sysroot=$LFS       \
    --with-newlib             \
    --without-headers         \
    --enable-default-pie      \
    --enable-default-ssp      \
    --disable-nls             \
    --disable-shared          \
    --disable-multilib        \
    --disable-threads         \
    --disable-libatomic       \
    --disable-libgomp         \
    --disable-libquadmath     \
    --disable-libssp          \
    --disable-libvtv          \
    --disable-libstdcxx       \
    --enable-languages=c,c++

%make_build
popd

%install

pushd build
%make_install
popd

# Create the limits.h header file
cd ..
cat gcc/limitx.h gcc/glimits.h gcc/limity.h > \
    %{buildroot}/$(dirname $($LFS_TGT-gcc -print-libgcc-file-name))/include/limits.h
%files

%changelog
* Mon Aug 11 2025 Nathan Rowe <naterowe2002@gmail.com> - 4.1.1-1
- Initial build of binutils 4.1.1 for an LFS system
