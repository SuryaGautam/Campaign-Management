from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=100)
    voice_id = models.CharField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Campaign(models.Model):
    INBOUND = "Inbound"
    OUTBOUND = "Outbound"
    TYPE_CHOICES = [(INBOUND, "Inbound"), (OUTBOUND, "Outbound")]

    RUNNING = "Running"
    PAUSED = "Paused"
    COMPLETED = "Completed"
    STATUS_CHOICES = [(RUNNING, "Running"), (PAUSED, "Paused"), (COMPLETED, "Completed")]

    name = models.CharField(max_length=255)
    campaign_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=RUNNING)
    agents = models.ManyToManyField(Agent, related_name="campaigns")

    def __str__(self):
        return self.name

class CampaignResult(models.Model):
    name = models.CharField(max_length=255)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="results")
    phone = models.CharField(max_length=15)
    cost = models.FloatField()
    outcome = models.CharField(max_length=100)
    call_duration = models.FloatField()
    recording = models.URLField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    transcription = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
