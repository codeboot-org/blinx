from codeboot_app import app

# Display Blinx help page
app.hide()
document.body.innerHTML = read_file('https://raw.githubusercontent.com/codeboot-org/blinx/main/_blinx_help.html')

# Event handlers
def add_example():
    blinx_config_filename = "blinx_config.py"
    blinx_example_filename = "blinx_temp.py"

    # Create file with blinx configuration from app parameters
    blinx_config_code = ('id = "BLINX' + str(app.params.get('blinx-blx', "000")) + '"\n'
                         'url = "http://" + id + ".local/"\n')
    write_file(blinx_config_filename, blinx_config_code)

    # Create file with blinx usage example
    blinx_example_code = ('from chart import chart\n'
                          'from time import sleep\n'
                          '\n'
                          'import blinx_config\n'
                          '\n'
                          'while True:\n'
                          '    data = read_file(blinx_config.url + "temp,humid.csv")\n'
                          '    chart(data, x_axis="time", y_axis="value")\n'
                          '    sleep(1)\n')

    write_file(blinx_example_filename, blinx_example_code)

    # Open files
    show_file(blinx_config_filename)
    show_file(blinx_example_filename)

def switch_to_codeboot(e):
    document.body.innerHTML = ""
    app.clear_console()
    add_example()
    app.show()

# Add event handlers
document.querySelector("#button-open-fr").addEventListener("click", switch_to_codeboot)
document.querySelector("#button-open-en").addEventListener("click", switch_to_codeboot)

# Set language
document.body.setAttribute('lang', app.lang)
