"""Forms for playlist app."""

from turtle import title
from wtforms import SelectField, StringField, FloatField, IntegerField
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    
name = StringField("Playlist Name")
description = StringField("Description")
id = IntegerField("Id of playlist")
    # Add the necessary code to use this form


class SongForm(FlaskForm):
    """Form for adding songs."""
id 
title
artist
    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
