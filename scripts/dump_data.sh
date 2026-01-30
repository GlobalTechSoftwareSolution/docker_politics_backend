#!/bin/bash
# Dump local SQLite data to JSON

cd /Users/manibharadwaj/Developer/compnay/cloned/politics/politics_backend/politics_backend

echo "Dumping Users..."
python manage.py dumpdata users.User --indent 2 > users_data.json

echo "Dumping PendingInfo..."
python manage.py dumpdata users.PendingInfo --indent 2 > pending_info_data.json

echo "Dumping ActiveInfo..."
python manage.py dumpdata users.ActiveInfo --indent 2 > active_info_data.json

echo "Data dumped successfully!"
echo "Files created:"
echo "- users_data.json"
echo "- pending_info_data.json" 
echo "- active_info_data.json"