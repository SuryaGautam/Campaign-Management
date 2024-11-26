from django.contrib import admin
from .models import Agent, Campaign, CampaignResult

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'voice_id', 'updated') 
    search_fields = ('name', 'language')  
    
@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'campaign_type', 'phone_number', 'status')
    list_filter = ('campaign_type', 'status') 
    search_fields = ('name',)

@admin.register(CampaignResult)
class CampaignResultAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'cost', 'outcome', 'call_duration')
    search_fields = ('name', 'phone')
