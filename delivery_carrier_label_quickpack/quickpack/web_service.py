# Copyright 2021 Denis Leemann (Camptocamp SA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

_logger = logging.getLogger(__name__)

class PostlogisticsWebService(object):
    """ Connector with Quickpac for label with API
    
    TODO ADD DOC AND KNOWN LINKS TO APIs

    Allows to generate labels
    """