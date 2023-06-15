#!/usr/bin/env python3

from listenbrainz.labs_api.labs.api.recording_lookup_base import RecordingLookupBaseQuery


class ArtistCreditRecordingLookupQuery(RecordingLookupBaseQuery):

    def names(self):
        return "acr-lookup", "MusicBrainz Artist Credit Recording lookup"

    def inputs(self):
        return ['[artist_credit_name]', '[recording_name]']

    def introduction(self):
        return """This lookup performs an semi-exact string match on Artist Credit and Recording. The given parameters will have non-word
                  characters removed, unaccented and lower cased before being looked up in the database."""

    def get_lookup_string(self, param) -> str:
        return param["[artist_credit_name]"] + param["[recording_name]"]

    def get_table_name(self) -> str:
        return "mapping.canonical_musicbrainz_data"
