from codeboot import app

app.hide()

write_file("blinx_config.py", 'blinx_id = "BLINX' + str(app.params.get('blinx-blx', "000")) + '"')

document.body.innerHTML = read_file('https://raw.githubusercontent.com/codeboot-org/blinx/main/_blinx_help.html')

document.querySelector("#button-open-fr").setAttribute("onclick", lambda e: app.show())
document.querySelector("#button-open-en").setAttribute("onclick", lambda e: app.show())

document.body.setAttribute('lang', app.lang)
