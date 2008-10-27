# -*- coding: utf-8 -*-
##
## This file is part of CDS Invenio.
## Copyright (C) 2002, 2003, 2004, 2005, 2006, 2007, 2008 CERN.
##
## CDS Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## CDS Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with CDS Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
"""BibFormat element - Prints brief HTML picture and links to resources
"""
__revision__ = "$Id$"

def format(bfo):
    """
    Prints html image and link to photo resources.
    """
    from invenio.config import CFG_SITE_URL

    resources = bfo.fields("8564_")
    out = ""
    for resource in resources:

        if resource.get("x", "") == "icon" and resource.get("u", "") == "":
            out += '<a href="'+CFG_SITE_URL+'/record/'+bfo.control_field("001")+ \
                   '?ln='+ bfo.lang + '"><img src="' + resource.get("q", "").replace(" ","") \
                   + '" alt="" border="0"/></a>'

    return out

def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0
