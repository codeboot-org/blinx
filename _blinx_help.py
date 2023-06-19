from codeboot_app import app

# Display Blinx help page
app.hide()
document.body.innerHTML = read_file('https://raw.githubusercontent.com/codeboot-org/blinx/main/_blinx_help.html')

# i18n code
example_code = {}
example_code['en'] = ('import blinx_config  # see blinx_config.py\n'
                      '\n'
                      'while True:\n'
                      '    data = read_file(blinx_config.url + "temp,humid.csv")\n'
                      '    chart(data, x_axis="time", y_axis="value")\n')
example_code['fr'] = ('import blinx_config  # voir le fichier blinx.config.py\n'
                      '\n'
                      'while True:\n'
                      '    data = read_file(blinx_config.url + "temp,humid.csv")\n'
                      '    chart(data, x_axis="temps", y_axis="valeur")\n')

def get_example_code():
    return example_code.get(app.lang) or example_code['en']

# Event handlers
def add_example():
    blinx_config_filename = "blinx_config.py"
    blinx_example_filename = "blinx_temp.py"

    # Create file with blinx configuration from app parameters
    blinx_config_code = ('id = "BLINX' + str(app.params.get('blinx-blx', "000")) + '"\n'
                         'url = "http://" + id + ".local/"\n')
    write_file(blinx_config_filename, blinx_config_code)

    # Create file with blinx usage example
    blinx_example_code = get_example_code()
    write_file(blinx_example_filename, blinx_example_code)

    # Open files
    show_file(blinx_config_filename)
    show_file(blinx_example_filename, focus=True)

def switch_to_codeboot(e):
    document.body.innerHTML = ""
    app.clear_console()
    app.show()

def switch_to_codeboot_and_open_example(e):
    switch_to_codeboot(e)
    add_example()

# Add event handlers
document.querySelector("#button-open-fr").addEventListener("click", switch_to_codeboot)
document.querySelector("#button-open-en").addEventListener("click", switch_to_codeboot)
document.querySelector("#button-example-fr").addEventListener("click", switch_to_codeboot_and_open_example)
document.querySelector("#button-example-en").addEventListener("click", switch_to_codeboot_and_open_example)

# Set language
document.body.setAttribute('lang', app.lang)
