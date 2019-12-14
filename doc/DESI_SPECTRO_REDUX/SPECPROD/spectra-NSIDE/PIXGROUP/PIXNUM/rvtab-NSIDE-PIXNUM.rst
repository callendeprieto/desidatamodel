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

This HDU has no non-standard required keywords.

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

========== ======= ====== ====================================================
Name       Type    Units  Description
========== ======= ====== ====================================================
VRAD       float64 km s-1 Radial velocity
VRAD_ERR   float64 km s-1 Radial velocity error
LOGG       float64        Log of surface gravity
TEFF       float64 K      Effective temperature
ALPHAFE    float64        [alpha/Fe] from template fitting
FEH        float64        [Fe/H] from template fitting
VSINI      float64 km s-1 Stellar rotation velocity
NEXP       int32
CHISQ_TOT  float64        Total chi-square for all arms
CHISQ_B    float64        Chi-square in the B arm
CHISQ_C_B  float64        Chi-square in the B arm after fitting continuum only
CHISQ_R    float64        Chi-square in the R arm
CHISQ_C_R  float64        Chi-square in the R arm after fitting continuum only
CHISQ_Z    float64        Chi-square in the Z arm
CHISQ_C_Z  float64        Chi-square in the Z arm after fitting continuum only
FIBER      int32
REF_ID     int64
TARGET_RA  float64
TARGET_DEC float64
TARGETID   int32          DESI targetid
EXPID      int64          DESI exposure id
SN_B       float32        Median S/N B arm
SN_R       float32        Median S/N R arm
SN_Z       float32        Median S/N Z arm
SUCCESS    logical        Did we succeed or fail
========== ======= ====== ====================================================

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
