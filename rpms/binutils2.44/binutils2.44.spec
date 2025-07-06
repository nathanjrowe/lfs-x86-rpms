Name: binutils
Version: 2.44
Release: 1%{dist}
License: GNU GPL
Summary: The GNU Binutils are a collection of binary tools.
URL: https://www.gnu.org/software/binutils/

Source0: %{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

%description
The GNU Binutils are a collection of binary tools. The main ones are:

ld - the GNU linker.
as - the GNU assembler.
gold - a new, faster, ELF only linker.

%prep
%setup -q -n %{name}-%{version}

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
/tools/bin/addr2line
/tools/bin/ar
/tools/bin/as
/tools/bin/c++filt
/tools/bin/elfedit
/tools/bin/gprof
/tools/bin/ld
/tools/bin/ld.bfd
/tools/bin/nm
/tools/bin/objcopy
/tools/bin/objdump
/tools/bin/ranlib
/tools/bin/readelf
/tools/bin/size
/tools/bin/strings
/tools/bin/strip
/tools/include/ansidecl.h
/tools/include/bfd.h
/tools/include/bfdlink.h
/tools/include/ctf-api.h
/tools/include/ctf.h
/tools/include/diagnostics.h
/tools/include/dis-asm.h
/tools/include/plugin-api.h
/tools/include/sframe-api.h
/tools/include/sframe.h
/tools/include/symcat.h
/tools/lib/bfd-plugins/libdep.so
/tools/lib/libbfd.a
/tools/lib/libbfd.la
/tools/lib/libctf-nobfd.a
/tools/lib/libctf-nobfd.la
/tools/lib/libctf.a
/tools/lib/libctf.la
/tools/lib/libopcodes.a
/tools/lib/libopcodes.la
/tools/lib/libsframe.a
/tools/lib/libsframe.la
/tools/share/info/as.info
/tools/share/info/bfd.info
/tools/share/info/binutils.info
/tools/share/info/ctf-spec.info
/tools/share/info/dir
/tools/share/info/gprof.info
/tools/share/info/ld.info
/tools/share/info/ldint.info
/tools/share/info/sframe-spec.info
/tools/share/man/man1/addr2line.1
/tools/share/man/man1/ar.1
/tools/share/man/man1/as.1
/tools/share/man/man1/c++filt.1
/tools/share/man/man1/dlltool.1
/tools/share/man/man1/elfedit.1
/tools/share/man/man1/gprof.1
/tools/share/man/man1/ld.1
/tools/share/man/man1/nm.1
/tools/share/man/man1/objcopy.1
/tools/share/man/man1/objdump.1
/tools/share/man/man1/ranlib.1
/tools/share/man/man1/readelf.1
/tools/share/man/man1/size.1
/tools/share/man/man1/strings.1
/tools/share/man/man1/strip.1
/tools/share/man/man1/windmc.1
/tools/share/man/man1/windres.1
/tools/x86_64-pc-linux-gnu/bin/ar
/tools/x86_64-pc-linux-gnu/bin/as
/tools/x86_64-pc-linux-gnu/bin/ld
/tools/x86_64-pc-linux-gnu/bin/ld.bfd
/tools/x86_64-pc-linux-gnu/bin/nm
/tools/x86_64-pc-linux-gnu/bin/objcopy
/tools/x86_64-pc-linux-gnu/bin/objdump
/tools/x86_64-pc-linux-gnu/bin/ranlib
/tools/x86_64-pc-linux-gnu/bin/readelf
/tools/x86_64-pc-linux-gnu/bin/strip
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.x
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xbn
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xc
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xce
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xcer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xd
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xdc
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xdce
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xdcer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xde
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xder
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xdw
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xdwe
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xdwer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xe
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xn
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xr
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xs
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xsc
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xsce
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xscer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xse
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xser
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xsw
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xswe
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xswer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xu
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xw
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xwe
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf32_x86_64.xwer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.x
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xbn
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xc
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xce
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xcer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xd
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xdc
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xdce
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xdcer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xde
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xder
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xdw
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xdwe
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xdwer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xe
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xn
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xr
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xs
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xsc
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xsce
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xscer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xse
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xser
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xsw
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xswe
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xswer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xu
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xw
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xwe
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_i386.xwer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.x
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xbn
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xc
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xce
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xcer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xd
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xdc
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xdce
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xdcer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xde
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xder
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xdw
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xdwe
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xdwer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xe
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xn
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xr
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xs
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xsc
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xsce
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xscer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xse
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xser
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xsw
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xswe
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xswer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xu
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xw
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xwe
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_iamcu.xwer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.x
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xbn
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xc
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xce
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xcer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xd
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xdc
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xdce
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xdcer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xde
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xder
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xdw
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xdwe
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xdwer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xe
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xn
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xr
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xs
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xsc
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xsce
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xscer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xse
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xser
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xsw
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xswe
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xswer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xu
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xw
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xwe
/tools/x86_64-pc-linux-gnu/lib/ldscripts/elf_x86_64.xwer
/tools/x86_64-pc-linux-gnu/lib/ldscripts/stamp
/usr/lib/debug/tools/bin/addr2line-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/bin/ar-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/bin/as-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/bin/c++filt-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/bin/elfedit-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/bin/gprof-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/bin/ld-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/bin/ld.bfd-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/bin/nm-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/bin/objcopy-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/bin/objdump-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/bin/ranlib-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/bin/readelf-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/bin/size-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/bin/strings-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/bin/strip-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/lib/bfd-plugins/libdep.so-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/x86_64-pc-linux-gnu/bin/ar-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/x86_64-pc-linux-gnu/bin/as-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/x86_64-pc-linux-gnu/bin/ld-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/x86_64-pc-linux-gnu/bin/ld.bfd-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/x86_64-pc-linux-gnu/bin/nm-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/x86_64-pc-linux-gnu/bin/objcopy-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/x86_64-pc-linux-gnu/bin/objdump-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/x86_64-pc-linux-gnu/bin/ranlib-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/x86_64-pc-linux-gnu/bin/readelf-2.44-1.el8.x86_64.debug
/usr/lib/debug/tools/x86_64-pc-linux-gnu/bin/strip-2.44-1.el8.x86_64.debug

%changelog
* Fri Jun 27 2025 Nathan Rowe <naterowe2002@gmail.com> - 4.1.1-1
- Initial build of binutils 4.1.1 for an LFS system
