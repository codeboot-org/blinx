from codeboot_app import app

app.hide()

write_file("blinx_config.py", 'blinx_id = "BLINX' + str(app.params.get('blinx-blx', "000")) + '"')

document.body.innerHTML = read_file('https://raw.githubusercontent.com/codeboot-org/blinx/main/_blinx_help.html')

def add_example():
    code = ('from chart import chart\n'
            'from time import sleep\n'
            '\n'
            'blinx_id = "BLINX' + str(app.params.get('blinx-blx', "000")) + '"\n'
            '\n'
            'while True:\n'
            '    data = read_file("http://" + blinx_id + ".local/temp.csv")\n'
            '    chart(data)\n'
            '    sleep(1)\n')

    write_file("example.py", code)
    show_file("example.py")

def switch_to_codeboot(e):
    document.body.innerHTML = ""
    app.clear_console()
    add_example()
    app.show()

document.querySelector("#button-open-fr").addEventListener("click", switch_to_codeboot)
document.querySelector("#button-open-en").addEventListener("click", switch_to_codeboot)

document.body.setAttribute('lang', app.lang)
