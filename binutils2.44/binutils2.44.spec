Name: binutils
Version: 2.44
Release: 1%{dist}
License: GNU GPL
Summary: The GNU Binutils are a collection of binary tools.
URL: https://www.gnu.org/software/binutils/

Source0: %{name}-%{version}.tar.gz

%description
The GNU Binutils are a collection of binary tools. The main ones are:

ld - the GNU linker.
as - the GNU assembler.
gold - a new, faster, ELF only linker.

BuildRequires: make

%prep
%setup -qC

%build

mkdir -p build

pushd build

../configure --prefix=$LFS/tools \
             --with-sysroot=$LFS \
             --target=$LFS_TGT   \
             --disable-nls       \
             --enable-gprofng=no \
             --disable-werror    \
             --enable-new-dtags  \
             --enable-default-hash-style=gnu

%make_build
popd

%install

pushd build
%make_install
popd

%files

%changelog
* Fri Jun 27 2025 Nathan Rowe <naterowe2002@gmail.com> - 4.1.1-1
- Initial build of binutils 4.1.1 for an LFS system