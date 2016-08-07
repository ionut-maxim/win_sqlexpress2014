#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2016, Ionut Maxim <ionut@ionutmaxim.ro>, and others
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# this is a windows documentation stub.  actual code lives in the .ps1
# file of the same name

DOCUMENTATION = '''
---
module: win_elevatedpackage
version_added: "1.7"
author: Ionut Maxim
short_description: Installs/Uninstalls an installable package, from a local file using a scheduled task
description:
     - Installs or uninstalls a package.
     - 'Optionally uses a product_id to check if the package needs installing. You can find product ids for installed programs in the windows registry either in C(HKLM:Software\\Microsoft\\Windows\CurrentVersion\\Uninstall) or for 32 bit programs C(HKLM:Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall)'
options:
  path:
    description:
      - Location of the package to be installed
    required: true
  product_code:
    description:
      - product id of the installed package (used for checking if already installed)
      - You can find product ids for installed programs in the windows registry either in C(HKLM:Software\\Microsoft\\Windows\CurrentVersion\\Uninstall) or for 32 bit programs C(HKLM:Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall)'
    required: true
  arguments:
    description:
      - Any arguments the installer needs
    default: null
    required: false
'''

EXAMPLES = '''
# Playbook example
- name: Install the vc thingy
  win_package:
    name="Microsoft Visual C thingy"
    path="http://download.microsoft.com/download/1/6/B/16B06F60-3B20-4FF2-B699-5E9B7962F9AE/VSU_4/vcredist_x64.exe"
    Product_Id="{CF2BEA3C-26EA-32F8-AA9B-331F7E34BA97}"
    Arguments="/install /passive /norestart"
'''