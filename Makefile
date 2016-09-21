TOPDIR = ./

EXPORT_WIDTH  = 1024

images_dia = $(wildcard figures/*.dia)
images_png = $(images_dia:.dia=.png)
datauris = code/hack-4/full.py.datauri \
	   code/hack-5/full.py.datauri \
	   code/hack-6.py.datauri      \
           code/hack-7.py.datauri      \
	   code/hack-8.py.datauri

code/hack-4/full.py.datauri: MIMETYPE="text/plain;charset=us-ascii"
code/hack-5/full.py.datauri: MIMETYPE="text/plain;charset=us-ascii"
code/hack-6.py.datauri: MIMETYPE="text/plain;charset=us-ascii"
code/hack-7.py.datauri: MIMETYPE="text/plain;charset=us-ascii"
code/hack-8.py.datauri: MIMETYPE="text/plain;charset=us-ascii"

all: hack-4-split hack-5-split slides.html

hack-4-split:
	python $(TOPDIR)/scripts/split.py code/hack-4.py

hack-5-split:
	python $(TOPDIR)/scripts/split.py code/hack-5.py

slides.html: $(images_png) $(datauris)

clean:
	rm -f $(images_png)
	rm -f $(datauris)
	rm -f slides.html
	rm -fr code/hack-4
	rm -fr code/hack-5

include $(TOPDIR)/stylesheets/Makefile.rules
