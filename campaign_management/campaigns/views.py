from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Agent, Campaign, CampaignResult
from .serializers import AgentSerializer, CampaignSerializer, CampaignResultSerializer

class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

class AgentListCreateView(ListCreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    pagination_class = StandardPagination

class AgentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class CampaignListCreateView(ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    pagination_class = StandardPagination

class CampaignDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class CampaignResultListCreateView(ListCreateAPIView):
    queryset = CampaignResult.objects.all()
    serializer_class = CampaignResultSerializer
    pagination_class = StandardPagination

class CampaignResultDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CampaignResult.objects.all()
    serializer_class = CampaignResultSerializer
