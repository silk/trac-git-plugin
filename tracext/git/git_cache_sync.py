# -*- coding: iso-8859-1 -*-
#
# Copyright (C) 2011, Grzegorz Sobański <silk@boktor.net>
#
# See COPYING for distribution information

from trac.core import *
from trac.admin import IAdminCommandProvider
from trac.util import TracError, shorten_line
from trac.util.datefmt import FixedOffset, to_timestamp, format_datetime
from trac.util.text import to_unicode
from trac.versioncontrol.api import \
     Changeset, Node, Repository, IRepositoryConnector, NoSuchChangeset, NoSuchNode, \
     IRepositoryProvider, RepositoryManager
from trac.wiki import IWikiSyntaxProvider
from trac.versioncontrol.cache import CachedRepository, CachedChangeset
from trac.versioncontrol.web_ui import IPropertyRenderer
from trac.config import BoolOption, IntOption, PathOption, Option
from trac.web.chrome import Chrome

from genshi.builder import tag

from datetime import datetime
import sys
import os


class GitCacheSync(Component):

    implements(IAdminCommandProvider)


    def get_admin_commands(self):
        yield ('git changeset_added',
               '<repos> <rev> [rev] [...]',
               """Notify git plugin about new changesets in repository,
               so it can rebuild its cache.""",
               None, self._do_changeset_added)

    def _do_changeset_added(self, repo_name, *revs):
        rm = RepositoryManager(self.env)
        repos = rm.get_repository(repo_name)
        # TODO: verify that it is a git repository
        repos.add_changesets(revs)




