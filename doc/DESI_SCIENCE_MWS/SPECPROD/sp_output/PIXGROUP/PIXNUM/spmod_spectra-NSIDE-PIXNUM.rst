=============
spmod_spectra
=============

:Summary: Table with observed and best-fitting spectra 
:Naming Convention: ``spmod_{NSIDE}-{PIXNUM}.fits``, where the first 
    number is {NSIDE} and the second indicates the healpix number
:Regex: ``spmod_spectra-[0-9]{3}-[0-9]{5}.fits`` 
:File Type: FITS, 100 MB  
Contents
========

====== ============ ======== ===================================
Number EXTNAME      Type     Contents
====== ============ ======== ===================================
HDU0_               IMAGE    Empty (primary header)
HDU1_  B_WAVELENGTH IMAGE    B band wavelength array
HDU2_  B_MODEL      BINTABLE B band spectra (obs, err, fit, flx)
HDU3_  R_WAVELENGTH IMAGE    R band wavelength array
HDU4_  R_MODEL      BINTABLE R band spectra (obs, err, fit, flx)
HDU5_  Z_WAVELENGTH IMAGE    Z band wavelength array
HDU6_  Z_MODEL      BINTABLE Z band spectra (obs, err, fit, flx)
HDU7_  FIBERMAP     BINTABLE Fibermap table
====== ============ ======== ===================================


FITS Header Units
=================

HDU0
----

*Primary header.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== =================== ==== ========================
KEY      Example Value       Type Comment
======== =================== ==== ========================
DATE     2021-09-17T17:11:58 str  Date of creation
FCONFIG  desi-n.yaml         str  Config. file for piferre
NUMPY    1.17.4              str  Numpy version
ASTROPY  4.0                 str  Astropy version
MATPLOTL 3.1.2               str  Matplotlib version
SCIPY    1.3.3               str  Scipy version
YAML     5.3.1               str  YAML version
PYTHON   3.8.10              str  Python version
PIFERRE  0.1.0               str  Piferre version
FERRE    4.8.12              str  FERRE version
======== =================== ==== =========================

Empty HDU.

HDU1
----

EXTNAME = B_WAVELENGTH

*Wavelengths of the B arm data*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======
KEY    Example Value Type Comment
====== ============= ==== =======
NAXIS1 4759          int
====== ============= ==== =======

Data: FITS image [float64, 4759]

HDU2
----

EXTNAME = B_MODEL

*Models of the B arm data (arranged in a 2d array, the second dimension for 
different stars)*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 152288        int  length of dimension 1
NAXIS2 42            int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

==== ============= ===== =======================
Name Type          Units Description
==== ============= ===== =======================
obs  float64[4759]       Observed spectra as fit
err  float64[4759]       Error in spectra as fit
flx  float64[4759]       Absolute model flux
fit  float64[4759]       Best-fitting model
==== ============= ===== =======================

HDU3
----

EXTNAME = R_WAVELENGTH

*Wavelengths of the R arm data*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======
KEY    Example Value Type Comment
====== ============= ==== =======
NAXIS1 4231          int
====== ============= ==== =======

Data: FITS image [float64, 4231]

HDU4
----

EXTNAME = R_MODEL

*Models of the R arm data (arranged in a 2d array, the second dimension for 
different stars)*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 135392        int  length of dimension 1
NAXIS2 42            int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

==== ============= ===== =======================
Name Type          Units Description
==== ============= ===== =======================
obs  float64[4231]       Observed spectra as fit
err  float64[4231]       Error in spectra as fit
flx  float64[4231]       Absolute model flux
fit  float64[4231]       Best-fitting model
==== ============= ===== =======================

HDU5
----

EXTNAME = Z_WAVELENGTH

*Wavelengths of the Z arm data*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =======
KEY    Example Value Type Comment
====== ============= ==== =======
NAXIS1 4797          int
====== ============= ==== =======

Data: FITS image [float64, 4797]

HDU6
----

EXTNAME = Z_MODEL

*Models of the Z arm data (arranged in a 2d array, the second dimension for 
different stars)*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 153504        int  length of dimension 1
NAXIS2 42            int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

==== ============= ===== =======================
Name Type          Units Description
==== ============= ===== =======================
obs  float64[4797]       Observed spectra as fit
err  float64[4797]       Error in spectra as fit
flx  float64[4797]       Absolute model flux
fit  float64[4797]       Best-fitting model
==== ============= ===== =======================

HDU7
----

EXTNAME = FIBERMAP

*Copy of the fibermap*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 317           int  length of dimension 1
NAXIS2 42            int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========================== ======= ===== ===========
Name                       Type    Units Description
========================== ======= ===== ===========
TARGETID                   int64
COADD_FIBERSTATUS          int32
TARGET_RA                  float64
TARGET_DEC                 float64
PMRA                       float32
PMDEC                      float32
REF_EPOCH                  float32
FA_TARGET                  int64
FA_TYPE                    binary
OBJTYPE                    char[3]
SUBPRIORITY                float64
OBSCONDITIONS              int32
RELEASE                    int16
BRICKID                    int32
BRICK_OBJID                int32
MORPHTYPE                  char[4]
FLUX_G                     float32
FLUX_R                     float32
FLUX_Z                     float32
FLUX_IVAR_G                float32
FLUX_IVAR_R                float32
FLUX_IVAR_Z                float32
MASKBITS                   int16
REF_ID                     int64
REF_CAT                    char[2]
GAIA_PHOT_G_MEAN_MAG       float32
GAIA_PHOT_BP_MEAN_MAG      float32
GAIA_PHOT_RP_MEAN_MAG      float32
PARALLAX                   float32
BRICKNAME                  char[8]
EBV                        float32
FLUX_W1                    float32
FLUX_W2                    float32
FLUX_IVAR_W1               float32
FLUX_IVAR_W2               float32
FIBERFLUX_G                float32
FIBERFLUX_R                float32
FIBERFLUX_Z                float32
FIBERTOTFLUX_G             float32
FIBERTOTFLUX_R             float32
FIBERTOTFLUX_Z             float32
SERSIC                     float32
SHAPE_R                    float32
SHAPE_E1                   float32
SHAPE_E2                   float32
PHOTSYS                    char[1]
PRIORITY_INIT              int64
NUMOBS_INIT                int64
DESI_TARGET                int64
BGS_TARGET                 int64
MWS_TARGET                 int64
SCND_TARGET                int64
PLATE_RA                   float64
PLATE_DEC                  float64
COADD_NUMEXP               int16
COADD_EXPTIME              float32
COADD_NUMNIGHT             int16
COADD_NUMTILE              int16
MEAN_DELTA_X               float32
RMS_DELTA_X                float32
MEAN_DELTA_Y               float32
RMS_DELTA_Y                float32
MEAN_FIBER_RA              float64
STD_FIBER_RA               float32
MEAN_FIBER_DEC             float64
STD_FIBER_DEC              float32
MEAN_PSF_TO_FIBER_SPECFLUX float32
========================== ======= ===== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*

