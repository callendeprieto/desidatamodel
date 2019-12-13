=====
rvmod
=====

:Summary: This is the file with the best fit model spectra 
:Naming Convention: ``rvmod-64-120.fits``, where the first number is the NSIDE, and second one healpix number
:Regex: ``rvmod-[0-9]+-[0-9]+.fits`` 
:File Type: FITS, 100 MB  

Contents
========

====== ============ ======== ===================
Number EXTNAME      Type     Contents
====== ============ ======== ===================
HDU0_               IMAGE    Empty
HDU1_  B_WAVELENGTH IMAGE    Wavelength of the B arm
HDU2_  B_MODEL      IMAGE    Model spectrum of the B arm
HDU3_  R_WAVELENGTH IMAGE    Wavelength of the R arm
HDU4_  R_MODEL      IMAGE    Model spectrum of the R arm
HDU5_  Z_WAVELENGTH IMAGE    Wavelength of the Z arm
HDU6_  Z_MODEL      IMAGE    Model spectrum of the Z arm
HDU7_  FIBERMAP     BINTABLE Copy of the FIBERMAP
====== ============ ======== ===================


FITS Header Units
=================

HDU0
----


This HDU has no non-standard required keywords.

Empty HDU.

HDU1
----

EXTNAME = B_WAVELENGTH

Wavelengths of the B arm data.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======
KEY    Example Value Type Comment
====== ============= ==== =======
NAXIS1 2751          int
====== ============= ==== =======

Data: FITS image [float64, 2751]

HDU2
----

EXTNAME = B_MODEL

Models of the B arm data (arranged in a 2d array, the second dimension for different stars)

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======
KEY    Example Value Type Comment
====== ============= ==== =======
NAXIS1 2751          int
NAXIS2 1             int
====== ============= ==== =======

Data: FITS image [float64, 2751x1]

HDU3
----

EXTNAME = R_WAVELENGTH

Wavelengths of the R arm data.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======
KEY    Example Value Type Comment
====== ============= ==== =======
NAXIS1 2326          int
====== ============= ==== =======

Data: FITS image [float64, 2326]

HDU4
----

EXTNAME = R_MODEL

Models of the R arm data (arranged in a 2d array, the second dimension for different stars)


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======
KEY    Example Value Type Comment
====== ============= ==== =======
NAXIS1 2326          int
NAXIS2 1             int
====== ============= ==== =======

Data: FITS image [float64, 2326x1]

HDU5
----

EXTNAME = Z_WAVELENGTH

Wavelengths of the Z arm data.


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======
KEY    Example Value Type Comment
====== ============= ==== =======
NAXIS1 2881          int
====== ============= ==== =======

Data: FITS image [float64, 2881]

HDU6
----

EXTNAME = Z_MODEL

Models of the Z arm data (arranged in a 2d array, the second dimension for different stars)

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======
KEY    Example Value Type Comment
====== ============= ==== =======
NAXIS1 2881          int
NAXIS2 1             int
====== ============= ==== =======

Data: FITS image [float64, 2881x1]

HDU7
----

EXTNAME = FIBERMAP

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 361           int  length of dimension 1
NAXIS2 1             int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================= ======= ===== ===========
Name              Type    Units Description
================= ======= ===== ===========
TARGETID          int32
DESI_TARGET       int64
BGS_TARGET        int64
MWS_TARGET        int64
SECONDARY_TARGET  int64
TARGET_RA         float64
TARGET_DEC        float64
TARGET_RA_IVAR    float64
TARGET_DEC_IVAR   float64
BRICKID           float64
BRICK_OBJID       int64
MORPHTYPE         char[4]
PRIORITY          int32
SUBPRIORITY       float64
REF_ID            int64
PMRA              float32
PMDEC             float32
REF_EPOCH         float32
PMRA_IVAR         float32
PMDEC_IVAR        float32
RELEASE           int16
FLUX_G            float32
FLUX_R            float32
FLUX_Z            float32
FLUX_W1           float32
FLUX_W2           float32
FLUX_IVAR_G       float32
FLUX_IVAR_R       float32
FLUX_IVAR_Z       float32
FLUX_IVAR_W1      float32
FLUX_IVAR_W2      float32
FIBERFLUX_G       float32
FIBERFLUX_R       float32
FIBERFLUX_Z       float32
FIBERFLUX_W1      float32
FIBERFLUX_W2      float32
FIBERTOTFLUX_G    float32
FIBERTOTFLUX_R    float32
FIBERTOTFLUX_Z    float32
FIBERTOTFLUX_W1   float32
FIBERTOTFLUX_W2   float32
MW_TRANSMISSION_G float32
MW_TRANSMISSION_R float32
MW_TRANSMISSION_Z float32
EBV               float32
PHOTSYS           char[1]
OBSCONDITIONS     int32
NUMOBS_INIT       int64
PRIORITY_INIT     int64
NUMOBS_MORE       int32
HPXPIXEL          int64
FIBER             int32
PETAL_LOC         int32
DEVICE_LOC        int32
LOCATION          int32
FIBERSTATUS       int32
OBJTYPE           char[3]
LAMBDA_REF        float32
FIBERASSIGN_X     float32
FIBERASSIGN_Y     float32
FA_TARGET         int64
FA_TYPE           binary
NUMTARGET         int16
FIBER_RA          float64
FIBER_DEC         float64
FIBER_RA_IVAR     float32
FIBER_DEC_IVAR    float32
PLATEMAKER_X      float32
PLATEMAKER_Y      float32
PLATEMAKER_RA     float32
PLATEMAKER_DEC    float32
NUM_ITER          int32
SPECTROID         int32
EXPID             int64
================= ======= ===== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
