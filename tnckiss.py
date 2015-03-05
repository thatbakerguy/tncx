import kiss

k = kiss.KISS('/dev/ttyUSB0', 1200)
k.start()  # inits the TNC, optionally passes KISS config flags.
k.read(callback=print)
