# django-timelinejs3

## a django app for http://timeline3.knightlab.com/

### currently in alpha state because it was developed on friday midnight...

* clone it
* set up your localsettings.py, rename .template and fill
* migrate with ```python manage.py migrate```
* add a url like
```
url(r'^timeline/$', timeline_views.IndexView.as_view(), name='timeline_index'),
url(r'^timeline/data/$', timeline_views.index_data, name='timeline_index_data'),
```
and add events in django admin


## Todo
* write Tests
* add forms for adding new events via frontend
* use timeline primary key to render multiple timelines (on one page or seperated)
