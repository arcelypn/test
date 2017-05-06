import pexpect
child = pexpect.spawn("telnet 54.250.239.250 32773")
child.sendline("\r\n")
child.expect(">")
child.sendline("enable")
child.expect("#"
child.sendline("config t")
child.expect("#")
child.sendline("hostanme R1")
child.expect("#")
child.sendline("end")
child..expect("#")
