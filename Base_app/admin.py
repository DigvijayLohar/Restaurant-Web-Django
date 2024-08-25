from django.contrib import admin
from Base_app.models import Book_table1,Items,ItemList,Aboutus,Feedback


admin.site.register(Book_table1)
admin.site.register(Items)
admin.site.register(ItemList)
admin.site.register(Aboutus)
admin.site.register(Feedback)

class BookTable1Admin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Number', 'Date', 'Person')  # Display fields in the admin list view
    search_fields = ('Name', 'Email')                             # Searchable fields

# Alternatively, you can register the model like this:
# admin.site.register(Book_table1, BookTable1Admin)
