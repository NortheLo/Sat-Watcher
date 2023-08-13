#!/bin/bash

function install_debian() {
	local debian_deps="build-essential cmake g++ pkgconf libfftw3-dev "\ 
										"libvolk2-dev libpng-dev libluajit-5.1-dev libnng-dev "\
										"librtlsdr-dev libhackrf-dev libairspy-dev libairspyhf-dev "\
										"libglew-dev libglfw3-dev libzstd-dev ocl-icd-opencl-dev"     
	sudo apt install $debian_deps -y && build_satdump
}

function install_rh() {
	local rh_deps="git cmake g++ fftw-devel volk-devel libpng-devel luajit-devel \
	  						nng-devel rtl-sdr-devel hackrf-devel airspyone_host-devel glew-devel \
								glfw-devel libzstd-devel ocl-icd"
	sudo dnf install $rh_deps -y && build_satdump
}

function build_satdump() {
	git clone https://github.com/altillimity/satdump.git
	cd satdump 
	mkdir build && cd build 
	cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr ..
	make -j`nproc`
	ln -s ../pipelines .
	ln -s ../resources .
	ln -s ../satdump_cfg.json .
	sudo make install
}

function help() {
	echo "This is a helper script to automate the build process of satdump and other tools for receiving satelite images"
	echo "To build for an Red Hat based system type: ./sat-script.sh install_rh"
	echo "To build for an Debian based system type: ./sat-script.sh install_debian"
}

"${@:-help}"
