import flir_image_extractor
fir = flir_image_extractor.FlirImageExtractor()
fir.process_image('examples/ax8.jpg')
fir.plot()
