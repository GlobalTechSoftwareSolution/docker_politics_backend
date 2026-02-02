#!/usr/bin/env python
"""
Script to populate denormalized user fields in ActiveInfo and PendingInfo tables
"""
import os
import sys
import django
from django.conf import settings

# Add the project directory to Python path
sys.path.append('/Users/manibharadwaj/Developer/compnay/cloned/politics/politics_backend/politics_backend')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'politics_backend.settings')
django.setup()

from users.models import ActiveInfo, PendingInfo, User

def populate_denormalized_data():
    print("Populating denormalized user data...")
    
    # Populate ActiveInfo table
    print("Updating ActiveInfo records...")
    active_info_count = 0
    for active_info in ActiveInfo.objects.all():
        # Update submitted_by fields
        if active_info.submitted_by_id and not active_info.submitted_by_name:
            try:
                submitted_user = User.objects.get(id=active_info.submitted_by_id)
                active_info.submitted_by_name = submitted_user.fullname or submitted_user.email
                active_info.submitted_by_email = submitted_user.email
            except User.DoesNotExist:
                # If user doesn't exist, try to find a random active user
                random_user = User.objects.filter(is_approved=True).first()
                if random_user:
                    active_info.submitted_by_id = random_user.id
                    active_info.submitted_by_name = random_user.fullname or random_user.email
                    active_info.submitted_by_email = random_user.email
        
        # Update approved_by fields
        if active_info.approved_by_id and not active_info.approved_by_name:
            try:
                approved_user = User.objects.get(id=active_info.approved_by_id)
                active_info.approved_by_name = approved_user.fullname or approved_user.email
                active_info.approved_by_email = approved_user.email
            except User.DoesNotExist:
                # If user doesn't exist, try to find a random superuser
                super_user = User.objects.filter(is_superuser=True).first()
                if super_user:
                    active_info.approved_by_id = super_user.id
                    active_info.approved_by_name = super_user.fullname or super_user.email
                    active_info.approved_by_email = super_user.email
        
        active_info.save()
        active_info_count += 1
        if active_info_count % 10 == 0:
            print(f"Updated {active_info_count} ActiveInfo records...")
    
    # Populate PendingInfo table
    print("Updating PendingInfo records...")
    pending_info_count = 0
    for pending_info in PendingInfo.objects.all():
        if pending_info.submitted_by_id and not pending_info.submitted_by_name:
            try:
                submitted_user = User.objects.get(id=pending_info.submitted_by_id)
                pending_info.submitted_by_name = submitted_user.fullname or submitted_user.email
                pending_info.submitted_by_email = submitted_user.email
            except User.DoesNotExist:
                # If user doesn't exist, try to find a random active user
                random_user = User.objects.filter(is_approved=True).first()
                if random_user:
                    pending_info.submitted_by_id = random_user.id
                    pending_info.submitted_by_name = random_user.fullname or random_user.email
                    pending_info.submitted_by_email = random_user.email
            
            pending_info.save()
            pending_info_count += 1
            if pending_info_count % 10 == 0:
                print(f"Updated {pending_info_count} PendingInfo records...")
    
    print(f"Completed! Updated {active_info_count} ActiveInfo and {pending_info_count} PendingInfo records.")

if __name__ == '__main__':
    populate_denormalized_data()