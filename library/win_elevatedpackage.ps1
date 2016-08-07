#!powershell
# (c) 2016, Ionut Maxim <ionut@ionutmaxim.ro>
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

# WANT_JSON
# POWERSHELL_COMMON

#region DSC

$params = Parse-Args $args;
$path = Get-AnsibleParam -obj $params -name "path" -failifempty $true
$arguments = Get-AnsibleParam -obj $params -name "arguments"
$product_code = Get-AnsibleParam -obj $params -name "product_code" -failifempty $true

$Action = New-ScheduledTaskAction -Execute $path -Argument $arguments
$Principal = New-ScheduledTaskPrincipal -RunLevel Highest -UserId 'System' -LogonType S4U
$Setting = New-ScheduledTaskSettingsSet
$Task = New-ScheduledTask -Action $Action -Principal $Principal -Description 'Elevated Package' -Settings $Setting
Register-ScheduledTask -InputObject $Task -TaskName $product_code

$RC = Start-ScheduledTask -TaskName $product_code
while (1)
{
    $stat = schtasks /query /tn $product_code | 
                Select-String "$product_code.*?\s(\w+)\s*$" | 
                Foreach {$_.Matches[0].Groups[1].value}
    if ($stat -ne 'Running')
    {
        "Task completed"
        break
    }
    "Waiting for task to complete"
    Start-Sleep 5
}

If (Test-Path "HKLM:\Sofware\Microsoft\Windows\CurrentVersion\Uninstall\$product_code") {
    Exit-Json $result
}