# SPDX-FileCopyrightText: 2023 Sunip K. Mukherjee
#
# SPDX-License-Identifier: Apache-2.0

project('iri20py', 'c',
  version : '1.0',
  license: 'BSD-3',
  meson_version: '>=0.64.0',
  default_options : ['warning_level=2'],
)

add_languages('fortran')

py_mod = import('python')
py = py_mod.find_installation(pure: false)
py_dep = py.dependency()

install_dir = join_paths(py.get_install_dir(), 'iri20py')

fortran_srcs = [
  'src/IRI2020/dfp.f90',
  'src/IRI2020/cira.f',
  'src/IRI2020/igrf.f',
  'src/IRI2020/iridreg.f',
  'src/IRI2020/iriflip.f',
  'src/IRI2020/irifun.f',
  'src/IRI2020/irisub.f',
  'src/IRI2020/iritec.f',
  'src/IRI2020/rocdrift.f',
]

py.install_sources(
    'src/iri20py/__init__.py',
    subdir: 'iri20py',
    pure: false,
)

install_subdir(
    'src/IRI2020/data',
    install_dir: install_dir,
    strip_directory: false,
)

shared_library('iri20pyfort',
  fortran_srcs,
  fortran_args : ['-cpp', '-march=native', '-ffast-math', '-DIRI20DIR="'+join_paths(install_dir, 'data')+'"', '-std=legacy'],
  install : true,
  install_dir: install_dir,
)