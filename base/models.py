from django.db import models

# Create your models here.

REQUEST_CHOICES = (
    ("nc", "New Creation"),
    ("pd","Pending"),
    
)


class Request(models.Model):
    username = models.CharField(max_length=500)
    request_type = models.CharField(max_length=500)  # Dropdown
    application = models.CharField(max_length=500)   # Dropdown
    windows_id = models.CharField(max_length=200)    
    current_branch = models.CharField(max_length=500) # Dropdown
    current_role = models.CharField(max_length=300)
    line_manager = models.CharField(max_length=200)
    approved_by_line_manager = models.BooleanField(default=False)
    zonal = models.CharField(max_length=200)
    approved_by_zonal = models.BooleanField(default=False)
    approved_by_internal_control = models.BooleanField(default=False)
    request_status=models.CharField(max_length=200, default="New")


    # comments
    requester_comment = models.CharField(max_length=200000, blank=True, null=True)
    zonal_comment = models.CharField(max_length=200000, blank=True, null=True)
    line_manager_comment = models.CharField(max_length=200000, blank=True, null=True)
    internal_control_comment = models.CharField(max_length=200000, blank=True, null=True)


    # dates and time
    date_approved_by_zonal = models.DateTimeField(blank=True, null=True)
    date_approved_by_line_manager =models.DateTimeField(blank=True, null=True)
    date_modified_by_internal_control = models.DateTimeField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)




    def __str__(self):
        return f"{self.request_type} from {self.username}"
