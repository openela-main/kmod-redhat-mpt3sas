%define kmod_name		mpt3sas
%define kmod_vendor		redhat
%define kmod_rpm_name		kmod-redhat-mpt3sas
%define kmod_driver_version	35.101.00.00_dup8.3
%define kmod_driver_epoch	%{nil}
%define kmod_rpm_release	1
%define kmod_kernel_version	4.18.0-240.el8
%define kmod_kernel_version_min	%{nil}
%define kmod_kernel_version_dep	%{nil}
%define kmod_kbuild_dir		drivers/scsi/mpt3sas
%define kmod_dependencies       %{nil}
%define kmod_dist_build_deps	%{nil}
%define kmod_build_dependencies	%{nil}
%define kmod_provides           %{nil}
%define kmod_devel_package	0
%define kmod_devel_src_paths	%{nil}
%define kmod_install_path	extra/kmod-redhat-mpt3sas
%define kernel_pkg		kernel
%define kernel_devel_pkg	kernel-devel
%define kernel_modules_pkg	kernel-modules

%{!?dist: %define dist .el8_3}
%{!?make_build: %define make_build make}

%if "%{kmod_kernel_version_dep}" == ""
%define kmod_kernel_version_dep %{kmod_kernel_version}
%endif

%if "%{kmod_dist_build_deps}" == ""
%if (0%{?rhel} > 7) || (0%{?centos} > 7)
%define kmod_dist_build_deps redhat-rpm-config kernel-abi-whitelists elfutils-libelf-devel kernel-rpm-macros kmod
%else
%define kmod_dist_build_deps redhat-rpm-config kernel-abi-whitelists
%endif
%endif

Source0:	%{kmod_name}-%{kmod_vendor}-%{kmod_driver_version}.tar.bz2
# Source code patches
Patch0:	0001-scsi-scsi-mpt3sas-Fix-spelling-mistake.patch
Patch1:	0002-scsi-scsi-mpt3sas-Fix-unlock-imbalance.patch
Patch2:	0003-scsi-scsi-mpt3sas-Fix-error-returns-in-BRM_status_sh.patch
Patch3:	0004-scsi-scsi-mpt3sas-Fix-set-but-unused-variable.patch
Patch4:	0005-scsi-scsi-mpt3sas-Fix-kdoc-comments-format.patch
Patch5:	0006-scsi-scsi-mpt3sas-Memset-config_cmds.reply-buffer-wi.patch
Patch6:	0007-scsi-scsi-mpt3sas-Dump-system-registers-for-debuggin.patch
Patch7:	0008-scsi-scsi-mpt3sas-Cancel-the-running-work-during-hos.patch
Patch8:	0009-scsi-scsi-mpt3sas-Rename-and-export-interrupt-mask-u.patch
Patch9:	0010-scsi-scsi-mpt3sas-Add-functions-to-check-if-any-cmd-.patch
Patch10:	0011-scsi-scsi-mpt3sas-Postprocessing-of-target-and-LUN-r.patch
Patch11:	0012-scsi-scsi-mpt3sas-Update-driver-version-to-35.100.00.patch
Patch12:	0013-scsi-scsi-mpt3sas-Remove-superfluous-memset.patch
Patch13:	0014-scsi-scsi-mpt3sas-Remove-pci-dma-compat-wrapper-API.patch
Patch14:	0015-scsi-scsi-mpt3sas-Don-t-call-disable_irq-from-IRQ-po.patch
Patch15:	0016-scsi-scsi-mpt3sas-Detect-tampered-Aero-and-Sea-adapt.patch
Patch16:	0017-scsi-scsi-mpt3sas-Fix-sync-irqs.patch
Patch17:	0018-scsi-scsi-mpt3sas-A-small-correction-in-_base_proces.patch
Patch18:	0019-scsi-scsi-mpt3sas-Fix-timeouts-observed-while-reenab.patch
Patch19:	0020-scsi-scsi-mpt3sas-Define-hba_port-structure.patch
Patch20:	0021-scsi-scsi-mpt3sas-Allocate-memory-for-hba_port-objec.patch
Patch21:	0022-scsi-scsi-mpt3sas-Rearrange-_scsih_mark_responding_s.patch
Patch22:	0023-scsi-scsi-mpt3sas-Update-hba_port-s-sas_address-phy_.patch
Patch23:	0024-scsi-scsi-mpt3sas-Get-device-objects-using-sas_addre.patch
Patch24:	0025-scsi-scsi-mpt3sas-Rename-transport_del_phy_from_an_e.patch
Patch25:	0026-scsi-scsi-mpt3sas-Get-sas_device-objects-using-devic.patch
Patch26:	0027-scsi-scsi-mpt3sas-Update-hba_port-objects-after-host.patch
Patch27:	0028-scsi-scsi-mpt3sas-Set-valid-PhysicalPort-in-SMPPassT.patch
Patch28:	0029-scsi-scsi-mpt3sas-Handling-HBA-vSES-device.patch
Patch29:	0030-scsi-scsi-mpt3sas-Add-bypass_dirty_port_flag-paramet.patch
Patch30:	0031-scsi-scsi-mpt3sas-Handle-vSES-vphy-object-during-HBA.patch
Patch31:	0032-scsi-scsi-mpt3sas-Add-module-parameter-multipath_on_.patch
Patch32:	0033-scsi-scsi-mpt3sas-Bump-driver-version-to-35.101.00.0.patch
Patch33:	9000-version-bump.patch

%define findpat %( echo "%""P" )
%define __find_requires /usr/lib/rpm/redhat/find-requires.ksyms
%define __find_provides /usr/lib/rpm/redhat/find-provides.ksyms %{kmod_name} %{?epoch:%{epoch}:}%{version}-%{release}
%define sbindir %( if [ -d "/sbin" -a \! -h "/sbin" ]; then echo "/sbin"; else echo %{_sbindir}; fi )
%define dup_state_dir %{_localstatedir}/lib/rpm-state/kmod-dups
%define kver_state_dir %{dup_state_dir}/kver
%define kver_state_file %{kver_state_dir}/%{kmod_kernel_version}.%(arch)
%define dup_module_list %{dup_state_dir}/rpm-kmod-%{kmod_name}-modules

Name:		kmod-redhat-mpt3sas
Version:	%{kmod_driver_version}
Release:	%{kmod_rpm_release}%{?dist}
%if "%{kmod_driver_epoch}" != ""
Epoch:		%{kmod_driver_epoch}
%endif
Summary:	mpt3sas kernel module for Driver Update Program
Group:		System/Kernel
License:	GPLv2
URL:		https://www.kernel.org/
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:	%kernel_devel_pkg = %kmod_kernel_version
%if "%{kmod_dist_build_deps}" != ""
BuildRequires:	%{kmod_dist_build_deps}
%endif
ExclusiveArch:	x86_64
%global kernel_source() /usr/src/kernels/%{kmod_kernel_version}.$(arch)

%global _use_internal_dependency_generator 0
%if "%{?kmod_kernel_version_min}" != ""
Provides:	%kernel_modules_pkg >= %{kmod_kernel_version_min}.%{_target_cpu}
%else
Provides:	%kernel_modules_pkg = %{kmod_kernel_version_dep}.%{_target_cpu}
%endif
Provides:	kmod-%{kmod_name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(post):	%{sbindir}/weak-modules
Requires(postun):	%{sbindir}/weak-modules
Requires:	kernel >= 4.18.0-240.el8

Requires:	kernel < 4.18.0-241.el8
%if 0
Requires: firmware(%{kmod_name}) = ENTER_FIRMWARE_VERSION
%endif
%if "%{kmod_build_dependencies}" != ""
BuildRequires:  %{kmod_build_dependencies}
%endif
%if "%{kmod_dependencies}" != ""
Requires:       %{kmod_dependencies}
%endif
%if "%{kmod_provides}" != ""
Provides:       %{kmod_provides}
%endif
# if there are multiple kmods for the same driver from different vendors,
# they should conflict with each other.
Conflicts:	kmod-%{kmod_name}

%description
mpt3sas kernel module for Driver Update Program

%if 0

%package -n kmod-redhat-mpt3sas-firmware
Version:	ENTER_FIRMWARE_VERSION
Summary:	mpt3sas firmware for Driver Update Program
Provides:	firmware(%{kmod_name}) = ENTER_FIRMWARE_VERSION
%if "%{kmod_kernel_version_min}" != ""
Provides:	%kernel_modules_pkg >= %{kmod_kernel_version_min}.%{_target_cpu}
%else
Provides:	%kernel_modules_pkg = %{kmod_kernel_version_dep}.%{_target_cpu}
%endif
%description -n  kmod-redhat-mpt3sas-firmware
mpt3sas firmware for Driver Update Program


%files -n kmod-redhat-mpt3sas-firmware
%defattr(644,root,root,755)
%{FIRMWARE_FILES}

%endif

# Development package
%if 0%{kmod_devel_package}
%package -n kmod-redhat-mpt3sas-devel
Version:	%{kmod_driver_version}
Requires:	kernel >= 4.18.0-240.el8

Requires:	kernel < 4.18.0-241.el8
Summary:	mpt3sas development files for Driver Update Program

%description -n  kmod-redhat-mpt3sas-devel
mpt3sas development files for Driver Update Program


%files -n kmod-redhat-mpt3sas-devel
%defattr(644,root,root,755)
/lib/modules/%{kmod_rpm_name}-%{kmod_driver_version}/
%endif

%post
modules=( $(find /lib/modules/%{kmod_kernel_version}.%(arch)/%{kmod_install_path} | grep '\.ko$') )
printf '%s\n' "${modules[@]}" | %{sbindir}/weak-modules --add-modules --no-initramfs

mkdir -p "%{kver_state_dir}"
touch "%{kver_state_file}"

exit 0

%posttrans
# We have to re-implement part of weak-modules here because it doesn't allow
# calling initramfs regeneration separately
if [ -f "%{kver_state_file}" ]; then
	kver_base="%{kmod_kernel_version_dep}"
	kvers=$(ls -d "/lib/modules/${kver_base%%.*}"*)

	for k_dir in $kvers; do
		k="${k_dir#/lib/modules/}"

		tmp_initramfs="/boot/initramfs-$k.tmp"
		dst_initramfs="/boot/initramfs-$k.img"

		# The same check as in weak-modules: we assume that the kernel present
		# if the symvers file exists.
		if [ -e "/boot/symvers-$k.gz" ] || [ -e "$k_dir/symvers.gz" ]; then
			/usr/bin/dracut -f "$tmp_initramfs" "$k" || exit 1
			cmp -s "$tmp_initramfs" "$dst_initramfs"
			if [ "$?" = 1 ]; then
				mv "$tmp_initramfs" "$dst_initramfs"
			else
				rm -f "$tmp_initramfs"
			fi
		fi
	done

	rm -f "%{kver_state_file}"
	rmdir "%{kver_state_dir}" 2> /dev/null
fi

rmdir "%{dup_state_dir}" 2> /dev/null

exit 0

%preun
if rpm -q --filetriggers kmod 2> /dev/null| grep -q "Trigger for weak-modules call on kmod removal"; then
	mkdir -p "%{kver_state_dir}"
	touch "%{kver_state_file}"
fi

mkdir -p "%{dup_state_dir}"
rpm -ql kmod-redhat-mpt3sas-%{kmod_driver_version}-%{kmod_rpm_release}%{?dist}.$(arch) | \
	grep '\.ko$' > "%{dup_module_list}"

%postun
if rpm -q --filetriggers kmod 2> /dev/null| grep -q "Trigger for weak-modules call on kmod removal"; then
	initramfs_opt="--no-initramfs"
else
	initramfs_opt=""
fi

modules=( $(cat "%{dup_module_list}") )
rm -f "%{dup_module_list}"
printf '%s\n' "${modules[@]}" | %{sbindir}/weak-modules --remove-modules $initramfs_opt

rmdir "%{dup_state_dir}" 2> /dev/null

exit 0

%files
%defattr(644,root,root,755)
/lib/modules/%{kmod_kernel_version}.%(arch)
/etc/depmod.d/%{kmod_name}.conf
%doc /usr/share/doc/%{kmod_rpm_name}/greylist.txt



%prep
%setup -n %{kmod_name}-%{kmod_vendor}-%{kmod_driver_version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
set -- *
mkdir source
mv "$@" source/
mkdir obj

%build
rm -rf obj
cp -r source obj

PWD_PATH="$PWD"
%if "%{workaround_no_pwd_rel_path}" != "1"
PWD_PATH=$(realpath --relative-to="%{kernel_source}" . 2>/dev/null || echo "$PWD")
%endif
%{make_build} -C %{kernel_source} V=1 M="$PWD_PATH/obj/%{kmod_kbuild_dir}" \
	NOSTDINC_FLAGS="-I$PWD_PATH/obj/include -I$PWD_PATH/obj/include/uapi %{nil}" \
	EXTRA_CFLAGS="%{nil}" \
	%{nil}
# mark modules executable so that strip-to-file can strip them
find obj/%{kmod_kbuild_dir} -name "*.ko" -type f -exec chmod u+x '{}' +

whitelist="/lib/modules/kabi-current/kabi_whitelist_%{_target_cpu}"
for modules in $( find obj/%{kmod_kbuild_dir} -name "*.ko" -type f -printf "%{findpat}\n" | sed 's|\.ko$||' | sort -u ) ; do
	# update depmod.conf
	module_weak_path=$(echo "$modules" | sed 's/[\/]*[^\/]*$//')
	if [ -z "$module_weak_path" ]; then
		module_weak_path=%{name}
	else
		module_weak_path=%{name}/$module_weak_path
	fi
	echo "override $(echo $modules | sed 's/.*\///')" \
	     "$(echo "%{kmod_kernel_version_dep}" |
	        sed 's/\.[^\.]*$//;
		     s/\([.+?^$\/\\|()\[]\|\]\)/\\\0/g').*" \
		     "weak-updates/$module_weak_path" >> source/depmod.conf

	# update greylist
	nm -u obj/%{kmod_kbuild_dir}/$modules.ko | sed 's/.*U //' |  sed 's/^\.//' | sort -u | while read -r symbol; do
		grep -q "^\s*$symbol\$" $whitelist || echo "$symbol" >> source/greylist
	done
done
sort -u source/greylist | uniq > source/greylist.txt

%install
export INSTALL_MOD_PATH=$RPM_BUILD_ROOT
export INSTALL_MOD_DIR=%{kmod_install_path}
PWD_PATH="$PWD"
%if "%{workaround_no_pwd_rel_path}" != "1"
PWD_PATH=$(realpath --relative-to="%{kernel_source}" . 2>/dev/null || echo "$PWD")
%endif
make -C %{kernel_source} modules_install \
	M=$PWD_PATH/obj/%{kmod_kbuild_dir}
# Cleanup unnecessary kernel-generated module dependency files.
find $INSTALL_MOD_PATH/lib/modules -iname 'modules.*' -exec rm {} \;

install -m 644 -D source/depmod.conf $RPM_BUILD_ROOT/etc/depmod.d/%{kmod_name}.conf
install -m 644 -D source/greylist.txt $RPM_BUILD_ROOT/usr/share/doc/%{kmod_rpm_name}/greylist.txt
%if 0
%{FIRMWARE_FILES_INSTALL}
%endif
%if 0%{kmod_devel_package}
install -m 644 -D $PWD/obj/%{kmod_kbuild_dir}/Module.symvers $RPM_BUILD_ROOT/lib/modules/%{kmod_rpm_name}-%{kmod_driver_version}/build/Module.symvers

if [ -n "%{kmod_devel_src_paths}" ]; then
	for i in %{kmod_devel_src_paths}; do
		mkdir -p "$RPM_BUILD_ROOT/lib/modules/%{kmod_rpm_name}-%{kmod_driver_version}/build/$(dirname "$i")"
		cp -rv "$PWD/source/$i" \
			"$RPM_BUILD_ROOT/lib/modules/%{kmod_rpm_name}-%{kmod_driver_version}/build/$i"
	done
fi
%endif



%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Jan 12 2021 Eugene Syromiatnikov <esyr@redhat.com> 35.101.00.00_dup8.3-1
- bfcc924fa05e36abe7a039ac5ec2be581e20c288
- mpt3sas kernel module for Driver Update Program
- Resolves: #bz1915214
