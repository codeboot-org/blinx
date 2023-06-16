from codeboot import app

app.hide()

write_file("blinx_config.py", 'blinx_id = "BLINX' + str(app.params.get('blinx-blx', "000")) + '"')

document.body.innerHTML = read_file('https://raw.githubusercontent.com/codeboot-org/blinx/main/_blinx_help.html')

def switch_to_codeboot(e):
    document.body.innerHTML = ""
    app.show()

document.querySelector("#button-open-fr").addEventListener("click", switch_to_codeboot)
document.querySelector("#button-open-en").addEventListener("click", switch_to_codeboot)

document.body.setAttribute('lang', app.lang)
