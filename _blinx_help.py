#cmds = host_eval('CodeBoot.prototype.cb.extractCommands(window.location.href).filter(function (cmd) { return typeof(cmd)==="string" && cmd.startsWith("~~blinx-"); })')

html = read_file('https://raw.githubusercontent.com/codeboot-org/blinx/main/_blinx_help.html')

document.body.innerHTML = html

document.body.setAttribute('lang', document.querySelector('.cb-vm').getAttribute('lang'))
