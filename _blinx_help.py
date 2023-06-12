cmds = host_eval('CodeBoot.prototype.cb.extractCommands(window.location.href).filter(function (cmd) { return typeof(cmd)==="string" && cmd.startsWith("~~blinx-"); })')

alert('Welcome to BLINX!\n'+repr(cmds))
