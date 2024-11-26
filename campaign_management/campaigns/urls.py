from django.urls import path
from . import views

urlpatterns = [
    path('agents/', views.AgentListCreateView.as_view(), name='agent-list'),
    path('agents/<int:pk>/', views.AgentDetailView.as_view(), name='agent-detail'),
    path('campaigns/', views.CampaignListCreateView.as_view(), name='campaign-list'),
    path('campaigns/<int:pk>/', views.CampaignDetailView.as_view(), name='campaign-detail'),
    path('results/', views.CampaignResultListCreateView.as_view(), name='result-list'),
    path('results/<int:pk>/', views.CampaignResultDetailView.as_view(), name='result-detail'),
]
