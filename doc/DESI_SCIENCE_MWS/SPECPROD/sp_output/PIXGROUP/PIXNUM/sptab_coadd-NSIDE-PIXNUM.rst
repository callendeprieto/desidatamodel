===========
sptab_coadd
===========

:Summary: *This is the table with stellar parameters and abundances for coadds*
:Naming Convention: ``sptab_coadd-{NSIDE}-{PIXNUM}.fits``, where the first number
    is the NSIDE, and the second indicates the healpixel
:Regex: ``sptab_coadd-[0-9]{3}-[0-9]{5}.fits`` 
:File Type: FITS, 500 KB  

Contents
========

====== ======== ======== =======================
Number EXTNAME  Type     Contents
====== ======== ======== =======================
HDU0_           IMAGE    *Empty (primary header)*
HDU1_  SPTAB    BINTABLE *Stellar Param.table*
HDU2_  FIBERMAP BINTABLE *Brief Description*
====== ======== ======== =======================


FITS Header Units
=================

HDU0
----

*Primary HDU.*

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

EXTNAME = SPTAB

*Binary table with stellar parameters and abundances.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

====== ============= ==== =====================
KEY    Example Value Type Comment
====== ============= ==== =====================
NAXIS1 356           int  length of dimension 1
NAXIS2 42            int  length of dimension 2
====== ============= ==== =====================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== =========== ====== =======================================================================
Name       Type        Units  Description
========== =========== ====== =======================================================================
SUCCESS    int64              Bit indicating whether the code has likely produced useful results
TARGETID   int64              DESI targetid
FIBER      int32              DESI fiber
TEFF       float64     K      Effective temperature (K)
LOGG       float64            Surface gravity (g in cm/s**2)
FEH        float64            Metallicity [Fe/H] = log10(N(Fe)/N(H)) - log10(N(Fe)/N(H))sun
ALPHAFE    float64            Alpha-to-iron ratio [alpha/Fe]
LOG10MICRO float64            Log10 of Microturbulence (km/s)
PARAM      float64[5]         Array of atmospheric parameters ([Fe/H], [a/Fe], log10micro, Teff,logg)
COVAR      float64[25]        Covariance matrix for ([Fe/H], [a/Fe], log10micro, Teff,logg)
ELEM       float64[2]         Elemental abundance ratios to iron [elem/Fe]
ELEM_ERR   float64[2]         Uncertainties in the elemental abundance ratios to iron
CHISQ_TOT  float64            Total chi**2
SNR_MED    float64            Median signal-to-ratio
RV_ADOP    float64     km s-1 Adopted Radial Velocity (km/s)
========== =========== ====== =======================================================================

HDU2
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

