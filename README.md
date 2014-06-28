curveextract
============

About
-----

Extracts arrays of x and y values from an image of a curve.


How to use
----------

1. Crop your image, so that only the curve is visible and the axes coincide with the margin.
2. Run ``./curveextract.py -f <picture> -x <xrange> -y <yrange> -o output.pdf``.

Example
-------

The command
``./curveextract.py --file log1.jpeg --yrange '0.1 20' --xrange '0 20' --log True``
creates the file extracted.
