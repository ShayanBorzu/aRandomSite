from django.contrib import admin
from .models import Contact
# Register your models here.
from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'is_read', 'sent_at')
    list_editable = ('is_read',)
    search_fields = ('full_name', 'email', 'subject', 'message')
    list_filter = ('is_read', 'sent_at')
    list_display_links = ('full_name', 'email')
    date_hierarchy = 'sent_at'
    readonly_fields = ('sent_at',)
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('full_name', 'email', 'phone_number')
        }),
        ('Message Details', {
            'fields': ('subject', 'message')
        }),
        ('Status & Metadata', {
            'fields': ('is_read', 'sent_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_as_read', 'mark_as_unread']
    
    # Admin actions with decorators
    @admin.action(description='✓ Mark selected as read')
    def mark_as_read(self, request, queryset):
        """Mark selected messages as read"""
        updated = queryset.update(is_read=True)
        self.message_user(request, f'{updated} message(s) marked as read.')
    
    @admin.action(description='✗ Mark selected as unread')
    def mark_as_unread(self, request, queryset):
        """Mark selected messages as unread"""
        updated = queryset.update(is_read=False)
        self.message_user(request, f'{updated} message(s) marked as unread.')
        
    admin.site.site_header = "Contact Messages Admin"
    admin.site.site_title = "Contact Admin"
    admin.site.index_title = "Manage Contact Messages"
