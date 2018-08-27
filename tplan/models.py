from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class Protocol(models.Model):
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'
    PRIORITY_CHOICES = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    division = models.CharField(max_length=200)
    request = models.CharField(max_length=100,verbose_name='Requested By')
    keyword = models.CharField(max_length=200)
    disease_state = models.CharField(max_length=200)
    number_of_cycles = models.IntegerField()
    duration_of_cycles = models.IntegerField()
    date_request = models.DateField()
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, )
    citation = models.URLField(blank=True,null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Protocol, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('protocol_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

class Med(models.Model):
    protocol = models.ForeignKey(Protocol,on_delete=models.CASCADE,related_name='meds')
    brand_name = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=100)
    dose = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    volume = models.CharField(max_length=100)
    diluent = models.CharField(max_length=100)
    admin_route = models.CharField(max_length=100)
    rate_duration = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    cycle = models.CharField(max_length=100)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.generic_name

class PreMed(models.Model):
    protocol = models.ForeignKey(Protocol,on_delete=models.CASCADE,related_name='premeds')
    brand_name = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=100)
    dose = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    admin_route = models.CharField(max_length=100)
    volume = models.CharField(max_length=100)
    diluent = models.CharField(max_length=100)
    rate_duration = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    cycle = models.CharField(max_length=100)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.generic_name

class PrnMed(models.Model):
    protocol = models.ForeignKey(Protocol,on_delete=models.CASCADE,related_name='prnmeds')
    brand_name = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=100)
    dose = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    prn_indication = models.CharField(max_length=100)
    admin_route = models.CharField(max_length=100)
    volume = models.CharField(max_length=100)
    diluent = models.CharField(max_length=100)
    rate_duration = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    cycle = models.CharField(max_length=100)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.generic_name

class Hydration(models.Model):
    protocol = models.ForeignKey(Protocol,on_delete=models.CASCADE,related_name='hydrations')
    fluid_name = models.CharField(max_length=100)
    volume = models.CharField(max_length=100)
    additive_name = models.CharField(max_length=100)
    additive_dose = models.CharField(max_length=100)
    rate_duration = models.CharField(max_length=100)
    administration_time = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    cycle = models.CharField(max_length=100)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.fluid_name

class Lab(models.Model):
    protocol = models.ForeignKey(Protocol, on_delete=models.CASCADE,related_name='labs')
    lab = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    cycle = models.CharField(max_length=100)

    def __str__(self):
        return self.lab

class Condition(models.Model):
    protocol = models.ForeignKey(Protocol, on_delete=models.CASCADE,related_name='conditions')
    condition = models.CharField(max_length=300)
    cycle_day = models.CharField(max_length=200)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.condition

class HomeMeds(models.Model):
    YES = 'Yes'
    NO = 'No'
    DAW_CHOICES = (
        (YES, 'Yes'),
        (NO, 'No'),
    )
    protocol = models.ForeignKey(Protocol, on_delete=models.CASCADE,related_name='homemeds')
    brand_name = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=100)
    dose = models.CharField(max_length=100)
    admin_route = models.CharField(max_length=100,verbose_name='Route')
    frequency = models.CharField(max_length=100)
    sig = models.CharField(max_length=500)
    qty = models.CharField(max_length=50)
    refills = models.CharField(max_length=50)
    dispense_as_writtern = models.CharField(max_length=6, choices=DAW_CHOICES, )
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.brand_name
