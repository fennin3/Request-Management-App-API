from django.urls import  path
from  . import views
from .apiViews import  *


urlpatterns = [
    path('', views.login, name='login'),
    path('request-form/', views.request_form, name="request_form" ),
    path('dashboard/', views.dashboard, name="dashboard"),

    # Login
    path("login/", UserLoginView.as_view(), name="login"),
    # path("logout/<username>/", UserLogout.as_view(), name="logout"),

    # Creating a requests
    path("create-request/", CreateRequestView.as_view(), name="create_request"),

    # Requester
    path("requester-requests/<username>/", ListRequestsForARequester.as_view(), name="requester_requests"),
    path("request-details/<id>/", RetriveRequest.as_view(), name="request_detail"),


    # Approving/Denying

    path("zonal-approval/<id>/", ApproveDenyRequestZonal.as_view(), name="zonal_approval"),
    path("line-manager-approval/<id>/", ApproveDenyRequestLineManager.as_view(), name="line_manager_approval"),
    path("internal-control-approval/<id>/", ApproveDenyRequestInterControl.as_view(), name="internal_control_approval"),

    # Retrieving requests
    path("get-zonal-requests/<email>/", RetrieveZonalRequestsView.as_view(), name="zonal_requests"),
    path("get-line-manager-requests/<email>/", RetrieveLineManagerRequestsView.as_view(), name="line_manager_requests"),
    path("get-internal-control-requests/", RetrieveInternalControlRequestsView.as_view(), name="internal_control_requests"),
]
