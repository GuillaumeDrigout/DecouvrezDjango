from django.contrib import admin

# Register your models here.
from .models import Booking, Contact, Album, Artist


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ['created_at', 'contacted']


class BookingInline(admin.TabularInline):
    verbose_name = "Réservation"
    verbose_name_plural = "Réservations"
    model = Booking
    fieldsets = [
      (None, {'fields': ['album', 'contacted']})
    ]  # list columns
    extra = 0


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInline, ]  # list of bookings made by a contact


class AlbumArtistInline(admin.TabularInline):
    verbose_name = "Disque"
    verbose_name_plural = "Disques"
    model = Album.artists.through  # the query goes through an intermediate table.
    extra = 1


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumArtistInline, ]


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ['reference', 'title']
