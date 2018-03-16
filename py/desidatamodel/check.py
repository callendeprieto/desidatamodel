# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""
===================
desidatamodel.check
===================

Check actual files against the data model for validity.
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
# The line above will help with 2to3 support.
import os
import re

from desiutil.log import log, DEBUG

from . import PY3, DataModelError
from .stub import Stub


class DataModel(object):
    """Simple object to store data model data and metadata.

    Parameters
    ----------
    filename : :class:`str`
        The full path of the data model file.
    section : :class:`str`
        The full path to the section of the data model containing the file.

    Attributes
    ----------
    d2r : :class:`dict`
        A mapping of human-readable metavariables to regular expressions.
    hduline : regular expression
        Matches HDU section headers.
    refline : regular expression
        Matches lines that contain cross-references.
    regexpline : regular expression
        Matches lines that contain regular expressions.
    tableboundary : regular expression
        Matches table borders.
    """

    d2r = {'BRICKNAME': '[0-9]+[pm][0-9]+',  # e.g. 3319p140
           'EXPID': '[0-9]{8}',  # zero-padded eight digit number.
           'NIGHT': '[0-9]{8}',  # YYYYMMDD
           'CAMERA': '[brz][0-9]',  # e.g. b0, r7
           'PIXPROD': '[a-z0-9_-]+',  # e.g. alpha-3
           'PRODNAME': '[a-z0-9_-]+',  # e.g. dc3c
           'SPECPROD': '[a-z0-9_-]+',  # replacement for PRODNAME
           'NSIDE': '[0-9]+',  # Healpix sides, e.g. 64
           'PIXGROUP': '[0-9]+',  # Healpix group, e.g. 53
           'PIXNUM': '[0-9]+',  # Healpix pixel, e.g. 5302
           }
    hduline = re.compile(r'HDU\d+$')
    regexpline = re.compile(r':?regexp?:', re.I)
    refline = re.compile(r'See :doc:`[^<]+<([^>]+)>`')
    tableboundary = re.compile(r'[= ]+$')

    def __init__(self, filename, section):
        self.filename = filename
        self.section = section
        self.ref = None
        self.regexp = None
        self.hdumeta = None
        self.prototype = None
        return

    def get_regexp(self, root, error=False):
        """Obtain the regular expression used to match files on disk.

        Parameters
        ----------
        root : :class:`str`
            Path to real files on disk.
        error : :class:`bool`, optional
            If ``True``, failure to find a regular expression raises an
            exception instead of just a warning.

        Returns
        -------
        regular expression
            The regular expression found, or ``None`` if not found.
            The regular expression is also stored internally.

        Raises
        ------
        :class:`~desimodel.DataModelError`
            If `error` is set and problems with the data model file are
            detected.
        """
        with open(self.filename) as dm:
            for le in dm.readlines():
                if PY3:
                    line = le
                else:
                    line = le.decode('utf-8')
                if line.startswith('See :doc:'):
                    self.ref = self._cross_reference(line)
                    log.debug("Cross reference detected %s -> %s.",
                              self.filename, self.ref)
                    break
                if self.regexpline.match(line) is not None:
                    d = os.path.dirname(self.filename).replace(self.section,
                                                               root)
                    for k in self.d2r:
                        d = d.replace(k, self.d2r[k])
                    r = line.strip().split()[1].replace('``', '')
                    self.regexp = re.compile(os.path.join(d, r))
                    break
        if self.regexp is None and self.ref is not None:
            with open(self.ref) as dm:
                for le in dm.readlines():
                    if PY3:
                        line = le
                    else:
                        line = le.decode('utf-8')
                    #
                    # Hopefully cross-references are not nested.
                    #
                    # if line.startswith('See :doc:'):
                    #     self.ref = self._cross_reference(line)
                    #     break
                    if self.regexpline.match(line) is not None:
                        d = os.path.dirname(self.filename).replace(self.section,
                                                                   root)
                        for k in self.d2r:
                            d = d.replace(k, self.d2r[k])
                        r = line.strip().split()[1].replace('``', '')
                        self.regexp = re.compile(os.path.join(d, r))
                        break
        if self.regexp is None:
            m = "%s has no file regexp!"
            if error:
                log.critical(m, self.filename)
                raise DataModelError(m % self.filename)
            else:
                log.warning(m, self.filename)
        return self.regexp

    def _cross_reference(self, line):
        """Obtain the path to a file referred to in another file.

        Parameters
        ----------
        line : :class:`str`
            Line from `filename` that *is* the cross-reference.

        Returns
        -------
        :class:`str`
            The path to the referenced file.
        """
        ref = None
        m = self.refline.match(line)
        if m is not None:
            r = os.path.abspath(os.path.join(os.path.dirname(self.filename),
                                             m.groups()[0]))
            if not r.endswith('.rst'):
                r += '.rst'
            if os.path.exists(r):
                ref = r
        return ref

    def _extract_columns(self, row, columns):
        """Given column sizes, extract the data in each column.

        Assumes a reStructuredText-compatible table.

        Parameters
        ----------
        row : :class:`str`
            A table row.
        columns : :class:`list`
            The sizes of the columns.

        Returns
        -------
        :func:`tuple`
            A tuple containing the extracted data.
        """
        lbound = [0] + [sum(columns[:i])+i for i in range(1, len(columns))]
        ubound = [lbound[i] + c for i, c in enumerate(columns)]
        data = [row[lbound[i]:ubound[i]].strip() for i in range(len(columns))]
        return tuple(data)

    def extract_metadata(self, error=False):
        """Extract metadata from a data model file.

        Parameters
        ----------
        error : :class:`bool`, optional
            If ``True``, failure to extract certain required metadata raises an
            exception.

        Returns
        -------
        :class:`list`
            Metadata in a form similar to :class:`~desidatamodel.stub.Stub`
            metadata.

        Raises
        ------
        :class:`~desimodel.DataModelError`
            If `error` is set.
        """
        metafile = self.filename
        if self.ref is not None:
            metafile = self.ref
        with open(metafile) as f:
            data = f.read()
            if not PY3:
                data = data.decode('utf-8')
        lines = data.split('\n')
        hdu_sections = [i for i, l in enumerate(lines)
                        if self.hduline.match(l) is not None]
        self.hdumeta = list()
        for k in range(len(hdu_sections)):
            try:
                section = lines[hdu_sections[k]:hdu_sections[k+1]]
            except IndexError:
                section = lines[hdu_sections[k]:]
            meta = dict()
            meta['title'] = section[0]
            if 'Empty HDU.' in section:
                meta['extension'] = 'IMAGE'
                meta['format'] = 'Empty HDU.'
            image_data = [l for l in section if l.startswith('Data:')]
            if image_data:
                meta['extension'] = 'IMAGE'
                meta['format'] = image_data[0]
            try:
                rdtc = section.index('Required Data Table Columns')
            except ValueError:
                rdtc = None
            if rdtc is not None:
                meta['extension'] = 'BINTABLE'
                table = [i for i, l in enumerate(section[rdtc:])
                         if self.tableboundary.match(l) is not None][1:3]
                columns = list(map(len, section[rdtc:][table[0]].split()))
                table_lines = section[rdtc:][table[0]+1:table[1]]
                meta['format'] = [self._extract_columns(t, columns)
                                  for t in table_lines]
            try:
                meta['extname'] = [l.split()[2] for l in section
                                   if l.startswith('EXTNAME = ')][0]
            except IndexError:
                meta['extname'] = ''
                m = "HDU %d in %s has no EXTNAME!"
                if error:
                    log.critical(m, k, metafile)
                    raise DataModelError(m % (k, metafile))
                else:
                    log.warning(m, k, metafile)
            try:
                rhk = section.index('Required Header Keywords')
            except ValueError:
                meta['keywords'] = []
            else:
                table = [i for i, l in enumerate(section[rhk:])
                         if self.tableboundary.match(l) is not None][1:3]
                columns = list(map(len, section[rhk:][table[0]].split()))
                table_lines = section[rhk:][table[0]+1:table[1]]
                meta['keywords'] = [self._extract_columns(t, columns)
                                    for t in table_lines]
            self.hdumeta.append(meta)
        return self.hdumeta

    def validate_prototype(self, error=False):
        """Compares a model's prototype data file to the data models.

        Parameters
        ----------
        error : :class:`bool`, optional
            If ``True``, failure to extract certain required metadata raises an
            exception.

        Notes
        -----
        * Use set theory to compare the data headers to model headers.  This should
          automatically find missing headers, extraneous headers, etc.
        """
        if self.prototype is None:
            #
            # A warning should have been issued already, so just skip silently.
            #
            return
        stub = Stub(self.prototype)
        try:
            stub_meta = stub.hdumeta
        except KeyError as e:
            log.warning("Prototype file %s threw KeyError: %s.",
                        self.prototype, e)
        modelmeta = self.extract_metadata(error=error)
        #
        # Check number of headers.
        #
        if stub.nhdr != len(modelmeta):
            log.warning("Prototype file %s has the wrong number of " +
                        "sections (HDUs) according to %s.",
                        self.prototype, self.filename)
            return
        for i in range(stub.nhdr):
            dkw = stub_meta[i]['keywords']
            mkw = modelmeta[i]['keywords']
            #
            # Check number of keywords.
            #
            if len(dkw) != len(mkw):
                log.warning("Prototype file %s has the wrong number of " +
                            "HDU%d keywords according to %s.",
                            self.prototype, i, self.filename)
                return
            #
            # If number of keywords is correct, check them individually.
            #
            for j in range(len(dkw)):
                if dkw[j][0] != mkw[j][0]:
                    log.warning("Prototype file %s has a keyword " +
                                "mismatch (%s != %s) in HDU%d according to " +
                                "%s.", self.prototype, dkw[j][0], mkw[j][0], i,
                                self.filename)
            #
            # Check the extension type.
            #
            dex = stub_meta[i]['extension']
            try:
                mex = modelmeta[i]['extension']
            except KeyError:
                mex = "Extension type not found"
            if dex != mex:
                log.warning("Prototype file %s has an extension type " +
                            "mismatch in HDU%d (%s != %s) " +
                            "according to %s.",
                            self.prototype, i, dex, mex, self.filename)
                return
            #
            # Check for EXTNAME
            #
            dexex = stub_meta[i]['extname']
            mexex = modelmeta[i]['extname']
            if dexex == '':
                log.warning("Prototype file %s has no EXTNAME in HDU%d.",
                            self.prototype, i)
            if (dexex != '' and mexex != '' and dexex != mexex):
                log.warning("Prototype file %s has an EXTNAME mismatch " +
                            "in HDU%d (%s != %s) " +
                            "according to %s.",
                            self.prototype, i, dexex, mexex, self.filename)
            #
            # If the extension type is correct, check the contents of the
            # extension.
            #
            dexf = stub_meta[i]['format']
            try:
                mexf = modelmeta[i]['format']
            except KeyError:
                mexf = "Extension format not found"
            if dex == 'IMAGE':
                try:
                    icomma = dexf.index(',')
                except ValueError:
                    icomma = len(dexf)
                if dexf[:icomma] != mexf[:icomma]:
                    log.warning("Prototype file %s has an extension " +
                                "format mismatch in HDU%d " +
                                "according to %s.",
                                self.prototype, i, self.filename)
            else:
                dexf = dexf[1:]  # Get rid of header line.
                if len(dexf) != len(mexf):
                    log.warning("Prototype file %s has the wrong " +
                                "number of HDU%d columns according to %s.",
                                self.prototype, i, self.filename)
                else:
                    for j in range(len(dexf)):
                        if dexf[j][0] != mexf[j][0]:
                            log.warning("Prototype file %s has a " +
                                        "column name mismatch (%s != %s) " +
                                        "in HDU%d according to %s.",
                                        self.prototype, dexf[j][0], mexf[j][0],
                                        i, self.filename)
        return

def scan_model(section):
    """Find all data model files in a top-level directory.

    Parameters
    ----------
    section : :class:`str`
        Full path to a section of the data model.

    Returns
    -------
    :class:`list`
        The data model files found.
    """
    scan = list()
    for dirpath, dirnames, filenames in os.walk(section):
        scan += [DataModel(os.path.join(dirpath, f), section)
                 for f in filenames
                 if f.endswith('.rst') and f != 'index.rst']
    return scan


def files_to_regexp(root, files, error=False):
    """Convert a list of data model files into a list of regular expressions.

    Parameters
    ----------
    root : :class:`str`
        Path to real files on disk.
    files : :class:`list`
        List of files obtained from the data model.
    error : :class:`bool`, optional
        If ``True``, failure to find a regular expression raises an
        exception instead of just a warning.

    Raises
    ------
    :class:`~desimodel.DataModelError`
        If `error` is set and data model files with malformed regular
        expressions are detected.
    """
    for f in files:
        f.get_regexp(root, error)
    return


def collect_files(root, files):
    """Scan a directory tree for files that correspond to data model files.

    Parameters
    ----------
    root : :class:`str`
        Path to real files on disk.
    files : :class:`list`
        A list of data model files.

    Notes
    -----
    Files are analyzed using this algorithm:

    * The first file that matches a regexp becomes the 'prototype' for that
      data model file.
    * If no files match a data model file, then files of that type are
      'missing'.
    * If a file does not match any regular expression, it is 'extraneous'.
    * If a file matches a regular expression that already has a prototype,
      it is 'ignored'.
    """
    ignore_directories = ('logs', 'scripts')
    include_extensions = ('.fits', '.fits.fz')
    for dirpath, dirnames, filenames in os.walk(root):
        for d in ignore_directories:
            try:
                dirnames.remove(d)
            except ValueError:
                pass
        include_filenames = list()
        for e in include_extensions:
            include_filenames += [f for f in filenames if f.endswith(e)]
        for f in include_filenames:
            extraneous_file = True
            fullname = os.path.join(dirpath, f)
            for r in files:
                if r.regexp is not None:
                    m = r.regexp.match(fullname)
                    if m is not None:
                        extraneous_file = False
                        if r.prototype is None:
                            r.prototype = fullname
            if extraneous_file:
                log.warning("Extraneous file detected: %s", fullname)
    #
    # Scan for missing files, but don't penalize (here) data models that
    # don't have a valid regular expression.  Files with bad regexeps will
    # be flagged elsewhere.
    #
    for r in files:
        if r.regexp is not None and r.prototype is None:
            log.warning("No files found matching %s!", r.filename)
    return


def validate_prototypes(files, error=False):
    """Compares a set of prototype data files to their data models.

    Parameters
    ----------
    files : :class:`list`
        A list of data model files.
    error : :class:`bool`, optional
        If ``True``, failure to extract certain required metadata raises an
        exception.

    Notes
    -----
    * Use set theory to compare the data headers to model headers.  This should
      automatically find missing headers, extraneous headers, etc.
    """
    for f in files:
        f.validate_prototype(error=error)
    return


def main():
    """Entry point for the check_model script.

    Returns
    -------
    :class:`int`
        An integer suitable for passing to :func:`sys.exit`.
    """
    from sys import argv
    from argparse import ArgumentParser
    desc = """Check actual files against the data model for validity.
"""
    parser = ArgumentParser(description=desc, prog=os.path.basename(argv[0]))
    parser.add_argument('-d', '--datamodel-dir', dest='desidatamodel',
                        metavar='DIR',
                        help='Override the value of DESIDATAMODEL.')
    parser.add_argument('-W', '--warning-is-error', dest='error',
                        action='store_true',
                        help=('Data model errors raise exceptions, ' +
                              'not warnings.'))
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true',
                        help='Set log level to DEBUG.')
    parser.add_argument('section', metavar='DIR',
                        help='Set the section of the data model.')
    parser.add_argument('directory', metavar='DIR',
                        help='Check files in this top-level directory.')
    options = parser.parse_args()
    if options.verbose:
        log.setLevel(DEBUG)
    if 'DESIDATAMODEL' in os.environ:
        data_model_root = os.environ['DESIDATAMODEL']
    else:
        if options.desidatamodel is not None:
            data_model_root = options.desidatamodel
        else:
            log.critical(("DESIDATAMODEL is not defined. " +
                          "Cannot find data model files!"))
            return 1
    section = os.path.join(data_model_root, 'doc', options.section)
    files = scan_model(section)
    files_to_regexp(options.directory, files, error=options.error)
    collect_files(options.directory, files)
    validate_prototypes(files, error=options.error)
    return 0
