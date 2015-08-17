# django-timelinejs3

## currently in pre-alpha state because it was develop on friday midnight...

* clone it
* set your localsettings.py, rename .template and fill
* migrate with ```python manage.py migrate```
* add a url like
```
url(r'^timeline/$', timeline_views.IndexView.as_view(), name='timeline_index'),
url(r'^timeline/data/$', timeline_views.index_data, name='timeline_index_data'),
```
and add events in django admin


## Todo
* make settings configurable via django admin
* add forms for adding new events via frontend
* use timeline primary key to rende multiple timelines (on one page or seperated)
