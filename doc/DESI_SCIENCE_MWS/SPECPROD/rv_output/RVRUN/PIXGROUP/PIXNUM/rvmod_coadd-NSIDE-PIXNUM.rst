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

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
TMPLCON0 desi_b           str  spectral configuration
TMPLREV0 v200312          str  template revision
TMPLSVR0 0.0.3            str  software version used to generate template files
TMPLCON1 desi_r           str  spectral configuration
TMPLREV1 v200312          str  template revision
TMPLSVR1 0.0.3            str  software version used to generate template files
TMPLCON2 desi_z           str  spectral configuration
TMPLREV2 v200312          str  template revision
TMPLSVR2 0.0.3            str  software version used to generate template files
RVS_CONF config.yaml      str  config file name
RVS_CMD  -minsn=10        str  Arguments
CHECKSUM j0YQj0XOj0XOj0XO str  HDU checksum updated 2020-03-16T08:46:33
DATASUM  0                str  data unit checksum updated 2020-03-16T08:46:33
======== ================ ==== ==============================================

Empty HDU.


HDU1
----

EXTNAME = B_WAVELENGTH

Wavelengths of the B arm data.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2751             int
CHECKSUM eFA5fC13eC83eC83 str  HDU checksum updated 2020-04-29T14:35:10
DATASUM  979185614        str  data unit checksum updated 2020-04-29T14:35:10
======== ================ ==== ==============================================

Data: FITS image [float64, 2751]

HDU2
----

EXTNAME = B_MODEL

Models of the B arm data (arranged in a 2d array, the second dimension for different stars)

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2751             int
NAXIS2   14               int
CHECKSUM CnqCEkoBCkoBCkoB str  HDU checksum updated 2020-04-29T14:35:10
DATASUM  931133553        str  data unit checksum updated 2020-04-29T14:35:10
======== ================ ==== ==============================================

Data: FITS image [float64, 2751x14]

HDU3
----

EXTNAME = R_WAVELENGTH

Wavelengths of the R arm data.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2326             int
CHECKSUM eOD2fMA1eMA1eMA1 str  HDU checksum updated 2020-04-29T14:35:10
DATASUM  456732359        str  data unit checksum updated 2020-04-29T14:35:10
======== ================ ==== ==============================================

Data: FITS image [float64, 2326]

HDU4
----

EXTNAME = R_MODEL

Models of the R arm data (arranged in a 2d array, the second dimension for different stars)


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2326             int
NAXIS2   14               int
CHECKSUM cKADfH8BcHABcH7B str  HDU checksum updated 2020-04-29T14:35:10
DATASUM  2973169384       str  data unit checksum updated 2020-04-29T14:35:10
======== ================ ==== ==============================================

Data: FITS image [float64, 2326x14]

HDU5
----

EXTNAME = Z_WAVELENGTH

Wavelengths of the Z arm data.


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2881             int
CHECKSUM PcGEPbFBPbFBPbFB str  HDU checksum updated 2020-04-29T14:35:10
DATASUM  3106662670       str  data unit checksum updated 2020-04-29T14:35:10
======== ================ ==== ==============================================

Data: FITS image [float64, 2881]

HDU6
----

EXTNAME = Z_MODEL

Models of the Z arm data (arranged in a 2d array, the second dimension for different stars)

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2881             int
NAXIS2   14               int
CHECKSUM JTpgKTmgJTmgJTmg str  HDU checksum updated 2020-04-29T14:35:10
DATASUM  2255969852       str  data unit checksum updated 2020-04-29T14:35:10
======== ================ ==== ==============================================

Data: FITS image [float64, 2881x14]

HDU7
----

EXTNAME = FIBERMAP

Copy of the fibermap

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

================================= ======= ===== ===========
Name                              Type    Units Description
================================= ======= ===== ===========
TARGETID                          int64
PETAL_LOC                         int16
DEVICE_LOC                        int32
LOCATION                          int64
FIBER                             int32
FIBERSTATUS                       int32
TARGET_RA                         float64
TARGET_DEC                        float64
PMRA                              float32
PMDEC                             float32
PMRA_IVAR                         float32
PMDEC_IVAR                        float32
REF_EPOCH                         float32
LAMBDA_REF                        float32
FA_TARGET                         int64
FA_TYPE                           binary
OBJTYPE                           char[3]
FIBERASSIGN_X                     float32
FIBERASSIGN_Y                     float32
NUMTARGET                         int16
PRIORITY                          int32
SUBPRIORITY                       float64
OBSCONDITIONS                     int32
NUMOBS_MORE                       int32
RELEASE                           int16
BRICKID                           int32
BRICKNAME                         char[8]
BRICK_OBJID                       int32
MORPHTYPE                         char[4]
TARGET_RA_IVAR                    float32
TARGET_DEC_IVAR                   float32
EBV                               float32
FLUX_G                            float32
FLUX_R                            float32
FLUX_Z                            float32
FLUX_IVAR_G                       float32
FLUX_IVAR_R                       float32
FLUX_IVAR_Z                       float32
MW_TRANSMISSION_G                 float32
MW_TRANSMISSION_R                 float32
MW_TRANSMISSION_Z                 float32
FRACFLUX_G                        float32
FRACFLUX_R                        float32
FRACFLUX_Z                        float32
FRACMASKED_G                      float32
FRACMASKED_R                      float32
FRACMASKED_Z                      float32
FRACIN_G                          float32
FRACIN_R                          float32
FRACIN_Z                          float32
NOBS_G                            int16
NOBS_R                            int16
NOBS_Z                            int16
PSFDEPTH_G                        float32
PSFDEPTH_R                        float32
PSFDEPTH_Z                        float32
GALDEPTH_G                        float32
GALDEPTH_R                        float32
GALDEPTH_Z                        float32
FLUX_W1                           float32
FLUX_W2                           float32
FLUX_W3                           float32
FLUX_W4                           float32
FLUX_IVAR_W1                      float32
FLUX_IVAR_W2                      float32
FLUX_IVAR_W3                      float32
FLUX_IVAR_W4                      float32
MW_TRANSMISSION_W1                float32
MW_TRANSMISSION_W2                float32
MW_TRANSMISSION_W3                float32
MW_TRANSMISSION_W4                float32
ALLMASK_G                         int16
ALLMASK_R                         int16
ALLMASK_Z                         int16
FIBERFLUX_G                       float32
FIBERFLUX_R                       float32
FIBERFLUX_Z                       float32
FIBERTOTFLUX_G                    float32
FIBERTOTFLUX_R                    float32
FIBERTOTFLUX_Z                    float32
WISEMASK_W1                       binary
WISEMASK_W2                       binary
MASKBITS                          int16
FRACDEV                           float32
FRACDEV_IVAR                      float32
SHAPEDEV_R                        float32
SHAPEDEV_E1                       float32
SHAPEDEV_E2                       float32
SHAPEDEV_R_IVAR                   float32
SHAPEDEV_E1_IVAR                  float32
SHAPEDEV_E2_IVAR                  float32
SHAPEEXP_R                        float32
SHAPEEXP_E1                       float32
SHAPEEXP_E2                       float32
SHAPEEXP_R_IVAR                   float32
SHAPEEXP_E1_IVAR                  float32
SHAPEEXP_E2_IVAR                  float32
REF_ID                            int64
REF_CAT                           char[2]
GAIA_PHOT_G_MEAN_MAG              float32
GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR  float32
GAIA_PHOT_BP_MEAN_MAG             float32
GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR float32
GAIA_PHOT_RP_MEAN_MAG             float32
GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR float32
GAIA_PHOT_BP_RP_EXCESS_FACTOR     float32
GAIA_ASTROMETRIC_EXCESS_NOISE     float32
GAIA_DUPLICATED_SOURCE            logical
GAIA_ASTROMETRIC_SIGMA5D_MAX      float32
GAIA_ASTROMETRIC_PARAMS_SOLVED    logical
PARALLAX                          float32
PARALLAX_IVAR                     float32
PHOTSYS                           char[1]
CMX_TARGET                        int64
PRIORITY_INIT                     int64
NUMOBS_INIT                       int64
HPXPIXEL                          int64
BLOBDIST                          float32
FIBERFLUX_IVAR_G                  float32
FIBERFLUX_IVAR_R                  float32
FIBERFLUX_IVAR_Z                  float32
DESI_TARGET                       int64
BGS_TARGET                        int64
MWS_TARGET                        int64
NUM_ITER                          int64
FIBER_X                           float64
FIBER_Y                           float64
DELTA_X                           float64
DELTA_Y                           float64
FIBER_RA                          float64
FIBER_DEC                         float64
NIGHT                             int32
EXPID                             int32
MJD                               float64
TILEID                            int32
================================= ======= ===== ===========


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
