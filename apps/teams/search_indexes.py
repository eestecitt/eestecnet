from apps.teams.models import Team

__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
from haystack import indexes




class TeamIndex(indexes.SearchIndex, indexes.Indexable):
    ''' Search index for accounts. Currently only searching by full name. '''
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Team
