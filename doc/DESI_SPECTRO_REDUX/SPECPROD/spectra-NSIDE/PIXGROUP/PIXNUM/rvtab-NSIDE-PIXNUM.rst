=====
rvtab
=====

:Summary: This is the table with radial velocity measurements
:Naming Convention: ``rvtab-64-1200.fits``, where the first number is the nside of 
  HEALPIXel  and the second number is the healpixel number
:Regex: ``rvtab-[0-9]+-[0-9]+.fits`` 
:File Type: FITS, 33 KB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ======== ======== ===================
Number EXTNAME  Type     Contents
====== ======== ======== ===================
HDU0_           IMAGE    Empty
HDU1_  RVTAB    BINTABLE RV table
HDU2_  FIBERMAP BINTABLE Copy of the fibermap for fitted sources
====== ======== ======== ===================


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

EXTNAME = RVTAB

The HDU has radial velocity measurements by the rv pipeline

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 181           int  length of dimension 1
NAXIS2 1             int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=========== ======= ====== =====================================================
Name        Type    Units  Description
=========== ======= ====== =====================================================
VRAD        float64 km s-1 Radial velocity
VRAD_ERR    float64 km s-1 Radial velocity error
VRAD_SKEW   float64        Radial velocity posterior skewness
VRAD_KURT   float64        Radial velocity posterior kurtosis
LOGG        float64        Log of surface gravity
TEFF        float64 K      Effective temperature
ALPHAFE     float64        [alpha/Fe] from template fitting
FEH         float64        [Fe/H] from template fitting
VSINI       float64 km s-1 Stellar rotation velocity
NEXP        int64
CHISQ_TOT   float64        Total chi-square for all arms
CHISQ_C_TOT float64        Total chi-square for all arms for polynomial only fit
CHISQ_B     float64        Chi-square in the B arm
CHISQ_C_B   float64        Chi-square in the B arm after fitting continuum only
CHISQ_R     float64        Chi-square in the R arm
CHISQ_C_R   float64        Chi-square in the R arm after fitting continuum only
CHISQ_Z     float64        Chi-square in the Z arm
CHISQ_C_Z   float64        Chi-square in the Z arm after fitting continuum only
RVS_WARN    int64          RVSpecFit warning flag
FIBER       int32
REF_ID      int64
TARGET_RA   float64
TARGET_DEC  float64
TARGETID    int64          DESI targetid
EXPID       int32          DESI exposure id
SN_B        float32        Median S/N in the B arm
SN_R        float32        Median S/N in the R arm
SN_Z        float32        Median S/N in the Z arm
SUCCESS     logical        Did we succeed or fail
=========== ======= ====== =====================================================

HDU2
----

EXTNAME = FIBERMAP

This is simply a copy of the FIBERMAP

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
