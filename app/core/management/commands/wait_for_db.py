    """
    Django command for the db to be available
    """
    
    from django.core.management.base import BaseCommand
    
    class Command(BaseCommand):
        """ Django wait for db command """
        
        def handle(self, *args: Any, **options: Any):
            pass